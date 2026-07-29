import streamlit as st
from shared_engines.energy_engine import calculate_cooling_and_roi

st.title("⚡ 2. Energy & Sustainability Management")
st.info("حاسبة كفاءة غلاف المبنى والجدوى المالية لتقليل فواتير المولدات الأهلية صيفاً.")

with st.container(border=True):
    area = st.number_input("مساحة الغلاف الإنشائي المعرض للشمس (متر مربع):", min_value=50, max_value=5000, value=200, step=50)
    material = st.selectbox("نوع مادة الجدران والبناء المستخدمة في المخطط:", ["طابوق عادي بدون عزل", "ثرمستون (صديق للبيئة)", "عزل حراري متكامل (بولسترين/صوف صخري)"])
    amps = st.number_input("حجم سحب الأمبيرات الحالي المخصص للتبريد صيفاً:", min_value=5, max_value=200, value=30, step=5)
    
    if st.button("🧮 حساب الوفر المالي والعائد", type="primary"):
        roi = calculate_cooling_and_roi(area, material, amps)
        st.write(f"📉 معامل الكسب الحراري للجدران `U-Value`: **{roi['u_value']} W/m²K**")
        st.success(f"💰 الوفر السنوي التقديري: {roi['annual_savings_iqd']:,} دينار عراقي سنوياً!")
        st.info(f"⏳ فترة استرداد رأس مال تركيب العزل: {roi['payback_years']} سنة.")
