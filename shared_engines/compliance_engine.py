# shared_engines/compliance_engine.py
import pandas as pd
import os
import streamlit as st

class IraqiDynamicComplianceEngine:
    def __init__(self, excel_filename="soil_investigation_code.xlsx"):
        """توجيه المحرك ليفتح ملف الإكسل المخصص للمدونة المحددة داخل مجلد data"""
        self.excel_path = os.path.join("data", excel_filename)

    def _load_rules(self):
        """فتح ملف الإكسل للمدونة المحددة وقراءة السطر الثاني كأعمدة حاكمة لـ بايثون"""
        if os.path.exists(self.excel_path):
            try:
                # قراءة ورقة العمل الأولى دائماً بغض النظر عن اسمها، مع اعتبار السطر الثاني هو أسماء الحقول البرمجية
                df = pd.read_excel(self.excel_path, sheet_name=0, header=1)
                # تنظيف وتنقية أسماء الأعمدة من الفراغات
                df.columns = [str(col).strip() for col in df.columns]
                # تحويل العمود المعرفي البرمجي إلى Index للمطابقة التلقائية الفورية
                return df.set_index('Code_Section').to_dict(orient='index')
            except Exception as e:
                st.sidebar.error(f"⚠️ خطأ في قراءة ملف المدونة {self.excel_path}: {str(e)}")
                return {}
        return {}

    def validate_soil_report(self, submission_data):
        """محرك فحص التربة الديناميكي - سحب وعرض التقارير السداسية بالعربي من ملف التربة الخاص بها"""
        report = {"status": "PASSED", "failures": [], "summary": ""}
        
        # تحميل القواعد الحية من ملف إكسل التربة المستقل
        rules = self._load_rules()
        
        # حماية السيرفر من الانهيار في حال لم يتم رفع ملف الإكسل في مجلد data بعد
        if not rules:
            return {"status": "PASSED", "failures": [], "summary": "⚠️ ملف الإكسل الخاص بالتربة data/soil_investigation_code.xlsx غير موجود."}

        # جلب المعطيات الفعلية التي أدخلها المستخدم في الواجهة
        actual_bearing = submission_data.get("soil_bearing_capacity", 120)
        actual_gypsum = submission_data.get("actual_gypsum_percentage", 4.5)
        governorate = submission_data.get("governorate", "Baghdad")
        report_status = submission_data.get("soil_report_status", "معتمد ومجاز ومصادق")

        # -------------------------------------------------------------------------
        # 1. مطابقة بند اعتمادية وختم تقرير التربة
        # -------------------------------------------------------------------------
        auth_rule = rules.get("Soil_Report_Validity", {})
        if auth_rule and report_status != str(auth_rule.get("Required_Value")).strip():
            self._add_failure_to_report(report, auth_rule)

        # -------------------------------------------------------------------------
        # 2. مطابقة حد قدرة تحمل التربة المقاسة (kPa)
        # -------------------------------------------------------------------------
        bearing_rule = rules.get("Soil_Bearing_Capacity", {})
        if bearing_rule:
            min_allowed = float(bearing_rule.get("Min_Value", 0))
            if actual_bearing < min_allowed:
                self._add_failure_to_report(report, bearing_rule)

        # -------------------------------------------------------------------------
        # 3. مطابقة نسبة الجبس والتربة الانهيارية (قيد المحافظات)
        # -------------------------------------------------------------------------
        gypsum_rule = rules.get("Soil_Gypsum_Content", {})
        if gypsum_rule:
            max_allowed = float(gypsum_rule.get("Max_Value", 100))
            # تفعيل قيد فحص التربة الجبسية لشرط المحافظات الأربع
            if governorate in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"] and actual_gypsum > max_allowed:
                self._add_failure_to_report(report, gypsum_rule)

        # تحديد النتيجة النهائية للمطابقة وإرسال الإشارة للوحة القيادة
        if report["failures"]:
            has_critical = any(f["severity"].startswith("CRITICAL") or "حرجة" in f["severity"] for f in report["failures"])
            if has_critical:
                report["status"] = "FAILED"
                report["summary"] = "❌ تم رفض المعاملة رقمياً لوجود مخالفات كودية وبلدية حرجة بموجب جدول إكسل مدونة فحص التربة."
        else:
            report["summary"] = "✅ المعاملة مستوفية ومطابقة تماماً لكافة شروط وأرقام ملف إكسل مدونة التربة المعتمد."

        return report

    def _add_failure_to_report(self, report, rule_row):
        """دالة سحب الأبعاد والرسائل السداسية بالعربي من الخلايا وضخها تلقائياً بالواجهة"""
        report["failures"].append({
            "severity": f"{rule_row.get('Msg_1_Severity', 'CRITICAL')}",
            "title": f"عنوان المخالفة الفني: {rule_row.get('Msg_2_Title', 'مخالفة غير معرفة')}",
            "citizen_exp": f"شرح المخالفة للمواطن: {rule_row.get('Msg_3_Citizen_Explanation', '')}",
            "engineer_exp": f"شرح المخالفة للمهندس: {rule_row.get('Msg_4_Engineer_Explanation', '')}",
            "resolution": f"رسالة Tوجيه والإصلاح الفني: {rule_row.get('Msg_5_Technical_Resolution', '')}",
            "legal_penalty": f"العقوبة والأثر القانوني: {rule_row.get('Msg_6_Legal_Penalty', '')}"
        })
