# pages/2_Energy_Management.py
import streamlit as st
from shared_engines.energy_engine import calculate_cooling_and_roi

st.title("⚡ 2. Energy & Sustainability Management")
st.info("بوابة إدارة الطاقة وتدقيق معاملات الكسب الحراري والجدوى المالية صيفاً.")

with st.container(border=True):
    st.subheader("📥 مدخلات تدقيق كفاءة الطاقة وغلاف المنشأ")
    
    area = st.number_input("مساحة الغلاف الإنشائي المعرض للشمس (متر مربع):", min_value=50, max_value=5000, value=200, step=50)
    material = st.selectbox("نوع مادة بناء الجدران الخارجية المقترحة:", ["طابوق عادي بدون عزل", "ثرمستون (صديق للبيئة)", "عزل حراري متكامل (بولسترين/صوف صخري)"])
    amps = st.number_input("حجم سحب الأمبيرات التقديري للتكييف صيفاً (أمبير):", min_value=5, max_value=200, value=30, step=5)
    
    st.markdown("---")
    
    if st.button("🧮 تشغيل محرك حسابات الطاقة والـ ROI", type="primary"):
        # استدعاء المحرك المركزي المطور المرتبط بملف الـ JSON
        roi = calculate_cooling_and_roi(area, material, amps)
        
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.metric(label="📉 معامل الكسب الحراري الكلي للجدران (U-Value)", value=f"{roi['u_value']} W/m²K")
            st.metric(label="☀️ درجة الحرارة التصميمية لوسط العراق", value=f"{roi['design_temp']} °C")
            
        with col_res2:
            st.metric(label="📉 الحاجة الجديدة للأمبيرات بعد العزل", value=f"{roi['new_amps_needed']} Amp", delta=f"-{roi['amperage_saved']} Amp")
            st.metric(label="⏳ فترة استرداد رأس مال العزل التقديرية", value=f"{roi['payback_years']} Years")
            
        st.markdown("---")
        st.html(f"""
        <div style="background-color:#F0FDF4; border:1px solid #BBF7D0; padding:15px; border-radius:8px;">
            <h5 style="color:#065F46; margin:0; font-family:sans-serif;">💰 الوفر المالي السنوي التقديري من فواتير المولدات صيفاً:</h5>
            <p style="font-size:22px; font-weight:bold; color:#15803D; margin:5px 0; font-family:sans-serif;">{roi['annual_savings_iqd']:,} دينار عراقي سنوياً</p>
        </div>
        """)
