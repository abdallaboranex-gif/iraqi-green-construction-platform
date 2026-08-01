# components/gate2_sustainability.py
import streamlit as st

# استدعاء العمليات الأربعة الذكية المعزولة
from components.gate2_insulation import render_insulation_section
from components.gate2_solar_optimizer import render_solar_optimizer_section
from components.gate2_hvac import render_hvac_section
from components.gate2_recommendations import render_energy_recommendations

def render_sustainability_gate(L, lang, direction, align):
    """الموزع الرقمي السيادي المستقل لبوابة إدارة الطاقة والاستدامة"""
    
    # 🟢 تدمير شروط الحجب تماماً وتفجير كارت الترويسة الثابت للبوابة الثانية
    st.markdown(f"""
    <div class='compliance-card' style='text-align: {align};'>
        <h4 style='color: #10B981; margin-top:0;'>🌱 {L['gate_2_title']}</h4>
        <p style='color: #6B7280; font-size: 0.88rem;'>المنظومة الإلكترونية المستقلة للتحقق والتدقيق الذكي لمدونات الطاقة والتكييف والتثليج العراقيّة.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # تأمين وجود قيم افتراضية للمحافظة والأبعاد في الذاكرة لتفادي الـ KeyError نهائياً
    if st.session_state.get("selected_gov", "") == "":
        st.session_state["selected_gov"] = "Baghdad"
    if st.session_state.get("land_width", 0.0) == 0.0:
        st.session_state["land_width"] = 10.0
    if st.session_state.get("land_length", 0.0) == 0.0:
        st.session_state["land_length"] = 25.0

    # 🚀 انفجار وفرش حقول البرامج الأربعة المتتالية حراً ومباشرة تحت بعضها بدون أي قيود
    u_value = render_insulation_section(align)
    
    st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #E2E8F0;'>", unsafe_allow_html=True)
    
    facade_dir, opt_angle, req_kw, panels_cnt = render_solar_optimizer_section(align)
    
    st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #E2E8F0;'>", unsafe_allow_html=True)
    
    hvac_type, fresh_control, req_cfm = render_hvac_section(align)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # تشغيل واستدعاء محرك التوصيات وحسابات الألواح والحلول الذكية بأقل كلفة طاقة
    render_energy_recommendations(align, direction, lang)
