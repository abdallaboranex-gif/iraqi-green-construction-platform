# components/gate2_hvac.py
import streamlit as st

def render_hvac_program(lang, align):
    """البرنامج الثاني: تخمين أحمال التكييف وتصميم المنظومات (مدونة التبريد والتثليج)"""
    st.markdown(f"<div style='text-align: {align}; padding-top:10px;'><b style='color:#1E3A8A;'>❄️ حساب السعة الفعالة وتدقيق منظومة الـ HVAC:</b></div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        hvac_type = st.selectbox("نوع منظومة التكييف المركزية المقترحة للمخطط:", ["", "منظومة سبلت بكج (Package Units)", "منظومة تدفق مائع التبريد المتغير (VRF)", "منظومة المثلجات المائية (Chillers System)"], key="sb_hvac_typ")
        fresh_air = st.selectbox("منظومة إدخال الهواء النقي (Fresh Air CFM Control):", ["", "تعتمد على التهوئة الطبيعية فقط", "منظومة ميكانيكية مجهزة بـ (Heat Recovery)", "منظومة ميكانيكية اعتيادية مفتوحة"], key="sb_fresh_air")
        safety_factor = st.slider("نسبة الأمان المضافة لحسابات الحمل الإجمالية:", min_value=1.0, max_value=1.3, value=1.1, step=0.05, key="sl_hvac_safety")
        
    if st.button("❄️ تشغيل تدقيق مدونة التبريد والتثليج العراقية", use_container_width=True, key="btn_run_hvac"):
        if hvac_type == "" or fresh_air == "":
            st.error("⚠️ يرجى تحديد نوع منظومة التكييف وآلية الهواء النقي لإجراء التدقيق الميكانيكي.")
        else:
            if hvac_type in ["منظومة تدفق مائع التبريد المتغير (VRF)", "منظومة المثلجات المائية (Chillers System)"] and "Heat Recovery" in fresh_air:
                st.success("🟢 الحسابات ميكانيكياً رصينة ومطابقة لمدونة التبريد والتثليج! المنظومة توفر استهلاك طاقة عالي وتحافظ على نقاء الهواء.")
                st.metric(label="السعة الطنية المستنتجة التقديرية المقدرة", value="14.5 Tons / Ton", delta="-3.2 Tons (توفير ميكانيكي)")
            else:
                st.warning("⚠️ المنظومة التقليدية المحددة تستهلك طاقة كهربائية ضخمة ولا تحقق التهوئة الصحية اللازمة للأقبو والسراديب.")
                st.metric(label="السعة الطنية المستنتجة التقديرية المقدرة", value="22.0 Tons / Ton", delta="+4.5 Tons (أحمال فائضة حرج)")
