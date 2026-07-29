# pages/1_Compliance_Gate.py
import streamlit as st
from shared_engines.compliance_engine import verify_comprehensive_compliance

st.title("🏢 1. Engineering Compliance Gate")
st.info("بوابة رفع ومطابقة مخططات إجازة البناء الإلكترونية الموحدة مع الكودات العراقية.")

with st.container(border=True):
    st.subheader("📥 مدخلات الفحص والتدقيق البلدي والإنشائي")
    
    # خيارات اختيار المنطقة والتربة المربوطة بالدستور الرقمي
    zone = st.selectbox("اختر المحافظة ونطاق المشروع الجغرافي:", ["وسط العراق (بغداد وحواسبها)", "جنوب العراق (البصرة والمحافظات الجنوبية)", "شمال العراق (نينوى والمناطق الجبلية)"])
    
    # تحويل الاختيار إلى المفتاح البرمجي المناسب لقراءة الـ JSON
    if "وسط" in zone:
        soil_key = "cohesive_clay_baghdad"
    elif "جنوب" in zone:
        soil_key = "sandy_gravel_basra"
    else:
        soil_key = "rocky_hills_nineveh"
        
    bearing_cap = st.number_input("أدخل قيمة قدرة تحمل التربة المستخرجة من المختبر (kPa):", min_value=10, max_value=500, value=120)
    building_height = st.number_input("أدخل الارتفاع الكلي المخطط للبناء (متر):", min_value=3, max_value=50, value=10)
    
    st.markdown("---")
    
    if st.button("🔐 تشغيل التدقيق الكودي والبلدي الفوري", type="primary"):
        # استدعاء محرك الفحص المطور والمستدام
        res = verify_comprehensive_compliance(zone, soil_key, bearing_cap, building_height)
        
        if res["status"]:
            st.success(f"🎉 {res['message']}")
            # تحديث مؤشرات لوحة القيادة المركزية في الذاكرة المؤقتة
            st.session_state["step2_completed"] = True
            st.session_state["compliance_rate"] = 55
            st.session_state["val6"] = 55
        else:
            st.error(f"❌ {res['message']}")
            st.session_state["step2_completed"] = False
            st.session_state["compliance_rate"] = 42
            st.session_state["val6"] = 42
