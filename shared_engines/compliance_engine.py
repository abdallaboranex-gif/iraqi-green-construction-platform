import json
import os

class IraqiSoilValidationEngine:
    def __init__(self, rules_file_path="soil_rules.json"):
        """تحميل قواعد فحص التربة من ملف الـ JSON المرفوع"""
        self.rules_file_path = rules_file_path
        self.rules = self._load_rules()

    def _load_rules(self):
        if os.path.exists(self.rules_file_path):
            with open(self.rules_file_path, 'r', encoding='utf-8') as f:
                return json.load(f).get("Soil_Investigation_Rules", {}).get("Rules", [])
        return []

    def validate_soil_report(self, submission_data):
        """المحرك البرمجي لمطابقة المدخلات مع المحددات الكودية الحاكمة"""
        report = {"status": "PASSED", "failures": [], "warnings": []}
        
        # 1. فحص استثناءات طلبات الترميم البسيط والديكور
        if submission_data.get("project_type") in ["ترميم بسيط", "ديكور"] and not submission_data.get("adds_structural_load", False):
            report["summary"] = "✅ مستثنى: طلبات الترميم والديكور الخفيفة مستثناة كودياً من فحص التربة."
            return report

        # تحويل القواعد إلى قاموس سريع للوصول للقيم الافتراضية
        rules_dict = {r["Element_Name"]: r for r in self.rules}

        # 2. فحص صلاحية التقرير إدارياً وقانونياً (Rule 1 & Rule 13)
        if submission_data.get("soil_report_status") != "معتمد ومجاز ومصادق":
            report["failures"].append("❌ تقرير فحص التربة المرفق غير معتمد أو غير مصادق قانونياً من نقابة المهندسين.")
        
        if submission_data.get("report_age_months", 0) > rules_dict.get("Soil_Report_Age", {}).get("Required_Value", 24):
            report["failures"].append("❌ تقرير فحص الأرض منتهي الصلاحية الزمنية (تجاوز 24 شهراً).")

        # 3. فحص عدد الحفر الاختبارية بناءً على المساحة (Rule 2)
        area = submission_data.get("total_land_area_m2", 0)
        actual_bh = submission_data.get("actual_boreholes_count", 0)
        
        # استثناء المساحات الصغيرة جداً
        if area <= 150 and submission_data.get("total_floors", 1) <= 2:
            required_bh = 1  # يكتفى بحفرة واحدة مأذونة كودياً بشرط ألا تكون أرض دفان
        else:
            required_bh = 2 if area <= 400 else 3
            
        if actual_bh < required_bh:
            report["failures"].append(f"❌ عدد الحفر الاستكشافية الميدانية ({actual_bh}) غير كافٍ هندسياً. الحد الأدنى المطلوب لهذه المساحة هو ({required_bh}) حفرة.")

        # 4. فحص أعماق الحفر (Rule 3 & Rule 4) - شرط الأبراج والسراديب الحرج
        actual_depth = submission_data.get("actual_borehole_depth_meters", 0.0)
        has_basement = submission_data.get("has_basement", False)
        floors = submission_data.get("total_floors", 1)

        if (floors >= 4 or has_basement) and actual_depth < 15.0:
            report["failures"].append(f"❌ عمق فحص التربة قصير جداً ({actual_depth}م) ولا يتناسب مع منشأ ثقيل/سرداب. الكود يفرض عمقاً حرجاً لا يقل عن 15 متر.")
        elif actual_depth < rules_dict.get("Borehole_Depth_Shallow", {}).get("Required_Value", 6.0):
            report["failures"].append(f"❌ عمق الحفرة الاختبارية الحالي ({actual_depth}م) أقل من الحد الأدنى المقبول كودياً للأبنية الخفيفة (6 أمتar).")

        # 5. الفحوصات الكيميائية والبيئات العدوانية (Rule 5 & Rule 8) - قيد صلاح الدين والأنبار
        so3_pct = submission_data.get("actual_so3_percentage", 0.0)
        if so3_pct > rules_dict.get("Soil_Sulphate_Content_SO3", {}).get("Required_Value", 5.0):
            report["warnings"].append(f"⚠️ تنبيه كيميائي: نسبة الكبريتات ({so3_pct}%) تصنف التربة كبيئة عدوانية. النظام يلزم برمجياً باستخدام سمنت مقاوم طراز الفئة الخامسة (Type V) وعزل الأسس.")

        gypsum_pct = submission_data.get("actual_gypsum_percentage", 0.0)
        gov = submission_data.get("governorate", "")
        if gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"] and gypsum_pct > rules_dict.get("Soil_Gypsum_Content", {}).get("Required_Value", 10.75):
            report["failures"].append(f"❌ خطر تربة انهيارية في {gov}: نسبة الجبس ({gypsum_pct}%) تتجاوز الحد الآمن كودياً (10.75%). يُلزم الكود برفض التأسيس التقليدي وإجبار المصمم على معالجة التربة بالإحلال أو الركائز العميقة.")

        # 6. فحص درجة الحدل الميداني (Rule 9)
        compaction = submission_data.get("actual_compaction_degree_percentage", 100.0)
        if compaction < rules_dict.get("Soil_Compaction_Degree", {}).get("Required_Value", 95.0):
            report["failures"].append(f"❌ درجة حدل وتربيط تربة التأسيس الميدانية ({compaction}%) دون الحد الأدنى المقر كودياً (95%). يجب إعادة حدل الأرض ميكانيكياً ورشها بالماء.")

        # تحديد النتيجة النهائية
        if report["failures"]:
            report["status"] = "FAILED"
            report["summary"] = f"❌ تم رفض المعاملة رقمياً لوجود {len(report['failures'])} مخالفات حرجة لمدونة فحص التربة العراقية والقوانين البلديّة."
        else:
            report["summary"] = "✅ المعاملة مستوفية تماماً لكافة الشروط الكودية والفحوصات المختبرية لمدونة التربة والأسس."

        return report
