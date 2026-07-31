# components/gate2_hvac.py
import streamlit as st

def render_hvac_section(align):
    """تخمين أحمال التكييف وتدقيق منظومات التهوئة وحجم الـ CFM لسراديب العراق"""
    st.markdown(f"<div style='text-align: {align}; padding-top:5px;'><b style='color:#1E3A8A;'>❄️ مدخلات منظومات التكييف الميكانيكية وتدوير الهواء:</b></div>", unsafe_allow_html=True)
    
    # قراءة المدخلات التاريخية للسرداب للتأقلم التلقائي مع الكود الميكانيكي لـ بايثون
    has_basement = st.session_state.get("has_basement_sel", "") in ["موجود", "Present"]
    
    with st.container(border=True):
        hvac_type = st.selectbox("نوع منظومة التكييف المركزية المقترحة للمخطط:", ["", "منظومة سبلت بكج (Package Units)", "منظومة تدفق مائع التبريد المتغير (VRF)", "منظومة المثلجات المائية (Chillers System)"], key="g2_hvac_typ")
        fresh_air_control = st.selectbox("آلية التحكم ودفع الهواء النقي (Fresh Air Control):", ["", "تهوئة طبيعية عشوائية", "منظومة دفع ميكانيكي مجهزة بـ (Heat Recovery)", "منظومة ميكانيكية اعتيادية مفتوحة"], key="g2_fresh_air")
        safety_factor = st.slider("نسبة الأمان الحرارية المضافة للحسابات (Safety Factor):", min_value=1.0, max_value=1.3, value=1.1, step=0.05, key="g2_hvac_safety")

    # حساب حجم دفع الهواء النقي الافتراضي المطلق بناءً على حالة قبو العقار
    required_cfm = 850 if has_basement else 0
    if "Heat Recovery" in fresh_air_control:
        cfm_efficiency_txt = "🟢 كفاءة التهوئة عالية جداً وموفرة للطاقة"
    else:
        cfm_efficiency_txt = "⚠️ فاقد طاقة مرتفع نتيجة غياب متبادل الحرارة"

    st.session_state["g2_hvac_data"] = {
        "hvac_type": hvac_type, "fresh_air_control": fresh_air_control,
        "safety_factor": safety_factor, "required_cfm": required_cfm,
        "efficiency_txt": cfm_efficiency_txt
    }
    return hvac_type, fresh_air_control, required_cfm
