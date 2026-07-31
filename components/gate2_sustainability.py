# components/gate2_sustainability.py
import streamlit as st

# استدعاء العمليات الأربعة المستقلة والذكية من ملفاتها المعزولة
from components.gate2_insulation import render_insulation_section
from components.gate2_solar_optimizer import render_solar_optimizer_section
from components.gate2_hvac import render_hvac_section
from components.gate2_recommendations import render_energy_recommendations

def render_sustainability_gate(L, lang, direction, align):
    """الموزع والمستدعي العام لعمليات بوابة إدارة الطاقة والاستدامة الرصينة"""
    
    st.markdown(f"""
    <div class='compliance-card' style='text-align: {align};'>
        <h4 style='color: #10B981; margin-top:0;'>🌱 {L['gate_2_title']}</h4>
        <p style='color: #6B7280; font-size: 0.88rem;'>المنظومة الإلكترونية للتحقق والتدقيق الذكي لمدونات الطاقة والتكييف والتثليج لجمهورية العراق.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 📑 تفعيل قطاعات الإدخال الفنية الثلاثة المتتالية تحت بعضها بدقة متناهية لحماية واقع العقار
    u_value = render_insulation_section(align)
    
    st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #E2E8F0;'>", unsafe_allow_html=True)
    
    facade_dir, opt_angle, req_kw, panels_cnt = render_solar_optimizer_section(align)
    
    st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #E2E8F0;'>", unsafe_allow_html=True)
    
    hvac_type, fresh_control, req_cfm = render_hvac_section(align)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 🧠 تشغيل واستدعاء محرك التوصيات وحسابات الألواح والحلول الذكية بأقل كلفة طاقة
    render_energy_recommendations(align, direction, lang)
