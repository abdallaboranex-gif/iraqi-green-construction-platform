import streamlit as st
import os
import sys

# التأكد من إمكانية استدعاء المحركات المشتركة من المجلد الفرعي
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shared_engines.compliance_engine import IraqiSoilValidationEngine

# إعدادات الصفحة الفنية
st.set_page_config(page_title="مدونة فحص التربة العراقية", page_icon="🔬", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🇮🇶 النظام الرقمي لمطابقة مدونة فحص التربة العراقية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #4B5563;'>التدقيق والتحقق التلقائي من التقارير الجيوتقنية لضمان السلامة الإنشائية ومطابقة القوانين البلدية</p>", unsafe_allow_html=True)
st.divider()

# بناء قطاعات واجهة المدخلات الذكية
col_ctx, col_lab = st.columns([1, 1], gap="large")

with col_ctx:
    st.markdown("<h3 style='color: #10B981;'>📋 أولاً: معطيات المعاملة والمخطط المعماري</h3>", unsafe_allow_html=True)
    
    project_type = st.selectbox("نوع الطلب / المعاملة", ["بناء جديد", "إضافة طابق", "مشاريع استثمارية كبرى", "ترميم بسيط", "ديكور"])
    
    if project_type in ["ترميم بسيط", "ديكور"]:
        adds_load = st.checkbox("هل يشمل الترميم إضافة أحمال إنشائية أو جدران حاملة جديدة؟")
    else:
        adds_load = True
        
    governorate = st.selectbox("النطاق الجغرافي / المحافظة", ["Baghdad", "Salah_Al_Din", "Anbar", "Basra", "Najaf", "Nineveh", "Muthanna", "Babil"])
    
    total_area = st.number_input("مساحة الأرض الكلية بموجب السند (m²)", min_value=50, max_value=100000, value=250)
    
    total_floors = st.number_input("عدد طوابق المبنى المقترحة (فوق مستوى الأرض)", min_value=1, max_value=50, value=2)
    
    has_basement = st.checkbox("هل يحتوي المخطط المعماري على طابق سرداب (Basement) أو أساس عميق؟")
    if has_basement:
        basement_depth = st.number_input("عمق قاع حفر السرداب المصمم (متر)", min_value=1.5, max_value=15.0, value=3.0, step=0.5)
    else:
        basement_depth = 0.0

with col_lab:
    st.markdown("<h3 style='color: #3B82F6;'>🔬 ثانياً: نتائج وتفاصيل تقرير فحص التربة المختبري</h3>", unsafe_allow_html=True)
    
    report_status = st.selectbox("حالة اعتماد ومصادقة تقرير التربة", ["معتمد ومجاز ومصادق", "غير مصادق / فحص عشوائي"])
    
    report_age = st.number_input("عمر التقرير الجيوتقني منذ تاريخ صدوره (بالأشهر)", min_value=0, max_value=120, value=3)
    
    bh_count = st.number_input("عدد الحفر الاستكشافية الميدانية المنفذة (Boreholes)", min_value=0, max_value=50, value=2)
    
    bh_depth = st.number_input("أقصى عمق واصلة له الحفرة الاختبارية (متر)", min_value=0.0, max_value=100.0, value=6.0, step=0.5)
    
    compaction_degree = st.number_input("قيمة درجة الحدل الميداني الفعلي لتربة الموقع (%)", min_value=50.0, max_value=100.0, value=96.0, step=0.5)
    
    gypsum_content = st.number_input("نسبة محتوى الجبس الكلية المختبرية (%)", min_value=0.0, max_value=100.0, value=4.5, step=0.1)
    
    so3_content = st.number_input("القيمة الرقمية للكبريتات الثلاثية الذائبة SO3 (%)", min_value=0.0, max_value=100.0, value=1.5, step=0.1)

st.divider()

# زر تشغيل الفحص والتحقق الرقمي
if st.button("📊 تشغيل محرك المطابقة الفورية والتدقيق الكودي", use_container_width=True):
    
    # تجميع المدخلات لإرسالها لعقل النظام
    submission_payload = {
        "project_type": project_type,
        "adds_structural_load": adds_load,
        "governorate": governorate,
        "total_land_area_m2": total_area,
        "total_floors": total_floors,
        "has_basement": has_basement,
        "designed_basement_depth_meters": basement_depth,
        "soil_report_status": report_status,
        "report_age_months": report_age,
        "actual_boreholes_count": bh_count,
        "actual_borehole_depth_meters": bh_depth,
        "actual_compaction_degree_percentage": compaction_degree,
        "actual_gypsum_percentage": gypsum_content,
        "actual_so3_percentage": so3_content
    }
    
    # استدعاء المحرك مع الإشارة للموقع الصحيح للملف المرفوع
    engine = IraqiSoilValidationEngine(rules_file_path="soil_rules.json")
    evaluation_result = engine.validate_soil_report(submission_payload)
    
    # عرض النتائج في واجهة مستخدم هندسية خلابة
    st.subheader("📋 تقرير التدقيق الفني والقانوني المباشر")
    
    if evaluation_result["status"] == "PASSED":
        st.success(evaluation_result["summary"])
        if "summary" not in evaluation_result:
            st.info("لم يتم رصد أي ملاحظات إضافية، المعاملة مطابقة ومقبولة بالكامل.")
    else:
        st.error(evaluation_result["summary"])
        
        # عرض المخالفات الحرجة التي تمنع منح الإجازة
        st.markdown("<h4 style='color: #DC2626;'>⚠️ تفاصيل البنود والمخالفات الحرجة المرصودة ومسارات الإصلاح الفنية:</h4>", unsafe_allow_html=True)
        for idx, failure in enumerate(evaluation_result["failures"], 1):
            st.markdown(f"<div style='background-color: #FEF2F2; padding: 12px; border-left: 5px solid #EF4444; border-radius: 4px; margin-bottom: 10px;'><b>المخالفة {idx}:</b> {failure}</div>", unsafe_allow_html=True)
            
    # عرض التنبيهات والتحذيرات غير الحاضرة للإبطال الفوري ولكن تتطلب تعديل مواصفات المخطط الإنشائي
    if evaluation_result.get("warnings"):
        st.markdown("<h4 style='color: #D97706;'>⚠️ تنبيهات واشتراطات خاصة بالمخططات الإنشائية والمواد:</h4>", unsafe_allow_html=True)
        for idx, warning in enumerate(evaluation_result["warnings"], 1):
            st.markdown(f"<div style='background-color: #FFFBEB; padding: 12px; border-left: 5px solid #F59E0B; border-radius: 4px; margin-bottom: 10px;'><b>قيد فني {idx}:</b> {warning}</div>", unsafe_allow_html=True)
