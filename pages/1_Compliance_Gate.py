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
        
        # 1. استدعاء محرك فحص التربة الجديد
        from shared_engines.compliance_engine import IraqiSoilValidationEngine
        soil_engine = IraqiSoilValidationEngine(rules_file_path="soil_rules.json")
        
        # 2. بناء حزمة البيانات بالاعتماد على متغيرات صفحتك الحالية
        payload = {
            "governorate": zone,
            "total_land_area_m2": 300, 
            "total_floors": int(building_height / 3),
            "soil_bearing_capacity": bearing_cap,
            "soil_report_status": "معتمد ومجاز ومصادق", 
            "report_age_months": 1,
            "actual_boreholes_count": 2, 
            "actual_borehole_depth_meters": 6.0,
            "actual_compaction_degree_percentage": 96.0,
            "actual_gypsum_percentage": 4.5,
            "actual_so3_percentage": 1.5
        }
        
        # 3. تشغيل الفحص ومطابقة الـ JSON
        soil_result = soil_engine.validate_soil_report(payload)
        
        # 4. طباعة التقرير الهندسي لمدونة التربة
        st.markdown("### 🔬 نتيجة تدقيق مدونة التربة والأسس العراقية:")
        if soil_result["status"] == "PASSED":
            st.success(soil_result["summary"])
        else:
            st.error(soil_result["summary"])
            for err in soil_result["failures"]:
                st.warning(err)
        
        # 5. الحفاظ على تحديث مؤشرات لوحة القيادة الخاصة بك
        st.session_state["step2_completed"] = True
        st.session_state["compliance_rate"] = 55
        st.session_state["val6"] = 55
    else:
        st.error(f"❌ {res['message']}")
        st.session_state["step2_completed"] = False
        st.session_state["compliance_rate"] = 42
        st.session_state["val6"] = 42
