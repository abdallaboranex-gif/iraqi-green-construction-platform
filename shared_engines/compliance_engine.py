# shared_engines/compliance_engine.py
import pandas as pd
import os
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

class IraqiDynamicComplianceEngine:
    def __init__(self, excel_filename="soil_testing.xlsx"):
        """توجيه المحرك ليفتح ملف الإكسل المخصص للمدونة المحددة داخل مجلد data"""
        self.excel_path = os.path.join("data", excel_filename)

    def _load_rules(self):
        """فتح ملف الإكسل للمدونة المحددة وقراءة السطر الثاني كأعمدة حاكمة لـ بايثون"""
        if os.path.exists(self.excel_path):
            try:
                df = pd.read_excel(self.excel_path, sheet_name=0, header=1)
                df.columns = [str(col).strip() for col in df.columns]
                return df.set_index('Code_Section').to_dict(orient='index')
            except Exception as e:
                st.sidebar.error(f"⚠️ خطأ في قراءة ملف المدونة {self.excel_path}: {str(e)}")
                return {}
        return {}

    def validate_soil_report(self, submission_data):
        """محرك فحص التربة الديناميكي - توليد التقارير والرسائل السداسية بالعربي من ملف التربة"""
        report = {"status": "PASSED", "failures": [], "summary": ""}
        rules = self._load_rules()
        
        if not rules:
            return {"status": "PASSED", "failures": [], "summary": "⚠️ ملف الإكسل الخاص بالتربة data/soil_testing.xlsx غير موجود."}

        actual_bearing = submission_data.get("soil_bearing_capacity", 120)
        actual_gypsum = submission_data.get("actual_gypsum_percentage", 4.5)
        governorate = submission_data.get("governorate", "Baghdad")
        report_status = submission_data.get("soil_report_status", "معتمد ومجاز ومصادق")

        # 1. مطابقة بند اعتمادية وختم تقرير التربة
        auth_rule = rules.get("Soil_Report_Validity", {})
        if auth_rule and report_status != str(auth_rule.get("Required_Value")).strip():
            self._add_failure_to_report(report, auth_rule)

        # 2. مطابقة حد قدرة تحمل التربة المقاسة (kPa)
        bearing_rule = rules.get("Soil_Bearing_Capacity", {})
        if bearing_rule:
            min_allowed = float(bearing_rule.get("Min_Value", 0))
            if actual_bearing < min_allowed:
                self._add_failure_to_report(report, bearing_rule)

        # 3. مطابقة نسبة الجبس والتربة الانهيارية (قيد المحافظات)
        gypsum_rule = rules.get("Soil_Gypsum_Content", {})
        if gypsum_rule:
            max_allowed = float(gypsum_rule.get("Max_Value", 100))
            if governorate in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"] and actual_gypsum > max_allowed:
                self._add_failure_to_report(report, gypsum_rule)

        if report["failures"]:
            has_critical = any(f["severity"].startswith("CRITICAL") or "حرجة" in f["severity"] for f in report["failures"])
            if has_critical:
                report["status"] = "FAILED"
                report["summary"] = "❌ تم رفض المعاملة رقمياً لوجود مخالفات كودية وبلدية حرجة بموجب جدول إكسل مدونة فحص التربة."
        else:
            report["summary"] = "✅ المعاملة مستوفية ومطابقة تماماً لكافة شروط وأرقام ملف إكسل مدونة التربة المعتمد."

        return report

    def _add_failure_to_report(self, report, rule_row):
        report["failures"].append({
            "severity": f"{rule_row.get('Msg_1_Severity', 'CRITICAL')}",
            "title": f"{rule_row.get('Msg_2_Title', 'مخالفة غير معرفة')}",
            "citizen_exp": f"{rule_row.get('Msg_3_Citizen_Explanation', '')}",
            "engineer_exp": f"{rule_row.get('Msg_4_Engineer_Explanation', '')}",
            "resolution": f"{rule_row.get('Msg_5_Technical_Resolution', '')}",
            "legal_penalty": f"{rule_row.get('Msg_6_Legal_Penalty', '')}"
        })

    def generate_pdf_report(self, payload, result, filename="generated_report.pdf"):
        """توليد ملف PDF احترافي منسق رقمياً لكافة شروط المطابقة والمخالفات السداسية بالعربي"""
        os.makedirs("generated", exist_ok=True)
        filepath = os.path.join("generated", filename)
        
        doc = SimpleDocTemplate(filepath, pagesize=letter, title="Iraqi Green Construction Compliance Report")
        styles = getSampleStyleSheet()
        
        # إعداد خطوط افتراضية وأنيقة للتقرير الرقمي
        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor('#1E3A8A'), alignment=1, spaceAfter=15)
        meta_style = ParagraphStyle('MetaStyle', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#4B5563'), leading=14)
        status_style_pass = ParagraphStyle('PassStyle', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#10B981'), alignment=1, spaceBefore=10, spaceAfter=10)
        status_style_fail = ParagraphStyle('FailStyle', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#DC2626'), alignment=1, spaceBefore=10, spaceAfter=10)
        body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#1F2937'), leading=14)
        disclaimer_style = ParagraphStyle('DisclaimerStyle', parent=styles['Normal'], fontSize=8, textColor=colors.HexColor('#9CA3AF'), alignment=1, spaceBefore=30)

        story = []
        
        # tرويسة الوثيقة الرسمية للمنصة
        story.append(Paragraph("Iraqi Green Construction Data Platform", title_style))
        story.append(Paragraph("<b>تقرير المطابقة والتدقيق الإلكتروني الموحد للمخططات الإنشائية والبلدية</b>", title_style))
        story.append(Spacer(1, 10))
        
        # جدول محددات المرحلة (أ) الخاصة بالبلدية والعقار أفقياً وعمودياً
        meta_data = [
            [Paragraph(f"<b>المحافظة / النطاق:</b> {payload.get('governorate', '')}", meta_style), Paragraph(f"<b>رقم القطعة:</b> {payload.get('lot_num', '1024/5')}", meta_style)],
            [Paragraph(f"<b>المساحة الكلية:</b> {payload.get('total_land_area_m2', 0):.1f} m²", meta_style), Paragraph(f"<b>رقم المقاطعة:</b> {payload.get('sector_num', '42 مكة')}", meta_style)],
            [Paragraph(f"<b>عدد الطوابق:</b> {payload.get('building_floors', 0)}", meta_style), Paragraph(f"<b>حالة السرداب:</b> {'يحتوي سرداب' if payload.get('is_heavy_structure') else 'بدون سرداب'}", meta_style)],
        ]
        t = Table(meta_data, colWidths=[250, 250])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
            ('PADDING', (0,0), (-1,-1), 8),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ]))
        story.append(t)
        story.append(Spacer(1, 20))
        
        # طباعة النتيجة العامة للمطابقة الكودية
        if result["status"] == "PASSED":
            story.append(Paragraph(f"<b>النتيجة النهائية: {result['summary']}</b>", status_style_pass))
        else:
            story.append(Paragraph(f"<b>النتيجة النهائية: {result['summary']}</b>", status_style_fail))
            story.append(Spacer(1, 10))
            
            # تفكيك وطبع الرسائل السداسية باللغة العربية داخل ملف الـ PDF
            for idx, failure in enumerate(result["failures"], 1):
                story.append(Paragraph(f"<b>⚠️ المخالفة رقم {idx}: {failure['title']}</b>", body_style))
                story.append(Paragraph(f"<b>• مستوى الحرج والخطورة:</b> {failure['severity']}", body_style))
                story.append(Paragraph(f"<b>• شرح المخالفة للمواطن:</b> {failure['citizen_exp']}", body_style))
                story.append(Paragraph(f"<b>• التوجيه الإنشائي للمهندس:</b> {failure['engineer_exp']}", body_style))
                story.append(Paragraph(f"<b>• مسار الإصلاح والحل الفني:</b> {failure['resolution']}", body_style))
                story.append(Paragraph(f"<b>• الأثر والعقوبة البلدية:</b> {failure['legal_penalty']}", body_style))
                story.append(Spacer(1, 15))
        
        # إضافة هامش التبرؤ والتدقيق الملزم والافتراضي بذيل الصفحة
        story.append(Paragraph("This is for informational purposes only. For medical advice or diagnosis, consult a professional. AI responses may include mistakes.", disclaimer_style))
        
        doc.build(story)
        return filepath
