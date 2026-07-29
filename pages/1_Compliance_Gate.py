import streamlit as st
from shared_engines.compliance_engine import verify_structural_and_soil

st.title("🏢 1. Engineering Compliance Gate")
st.info("بوابة رفع ومطابقة مخططات إجازة البناء الإلكترونية مع مدونات الكود العراقي.")

with st.container(border=True):
    st.subheader("📥 رفع البيانات والتقارير الهندسية للمشروع")
    bearing_cap = st.number_input("أدخل قيمة قدرة تحمل التربة المستخرجة من المختبر (kPa):", min_value=10, max_value=500, value=120)
    
    if st.button("🔐 تشغيل التدقيق الكودي الفوري", type="primary"):
        res = verify_structural_and_soil(bearing_cap)
        if res["status"]:
            st.success(f"🎉 {res['message']}")
            st.session_state["step2_completed"] = True
            st.session_state["compliance_rate"] = 55
        else:
            st.error(f"❌ {res['message']}")
            st.session_state["step2_completed"] = False
            st.session_state["compliance_rate"] = 42
