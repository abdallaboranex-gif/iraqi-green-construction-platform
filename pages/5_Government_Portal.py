import streamlit as st

st.title("🏛️ 5. Government Link & Reports Portal")
st.info("منصة المصادقة الرسمية لربط البلديات وأمانة بغداد لإصدار تقارير المطابقة السيادية.")

with st.container(border=True):
    st.subheader("📜 تدقيق المعاملة وإصدار التقرير النهائي")
    project_id = st.text_input("أدخل رقم المعاملة الموحد:", value="IQ-2026-99")
    is_step2_done = st.session_state.get("step2_completed", False)
    
    if st.button("🖨️ توليد تقرير المطابقة الرسمي", type="primary"):
        if is_step2_done:
            st.success(f"✅ تقرير المعاملة {project_id}: [مطابق للمواصفات] - الكودات الهندسية العراقية مستوفاة بالكامل. جاهز لإصدار الإجازة.")
        else:
            st.warning(f"⚠️ تقرير المعاملة {project_id}: [غير مطابق حالياً] - بانتظار إكمال فحص التربة والأسس الإنشائية.")
