# components/gate2_sustainability.py
import streamlit as st

# استدعاء البرامج التخصصية المفصولة والمحمية من ملفاتها الخاصة
from components.gate2_insulation import render_insulation_program
from components.gate2_hvac import render_hvac_program

def render_sustainability_gate(L, lang, direction, align):
    """الموزع والمستدعي الرقمي لبرامج بوابة الاستدامة وكفاءة الطاقة الموحدة"""
    
    st.markdown(f"""
    <div class='compliance-card' style='text-align: {align};'>
        <h4 style='color: #10B981; margin-top:0;'>🌱 {L['gate_2_title']}</h4>
        <p style='color: #6B7280; font-size: 0.88rem;'>المنظومة الإلكترونية السيادية للتحقق والتدقيق الذكي لمدونات الطاقة والتكييف والتثليج العراقيّة.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 📑 تفعيل الخيارين الهندسيين الموزعين في أعلى البوابة بنظام التبويبات (Tabs)
    prog_1 = "🧱 1. حاسبة العزل الحراري وغلاف المبنى (مدونة العزل)" if lang == "AR" else "🧱 1. Thermal Insulation & Envelope Calculator"
    prog_2 = "❄️ 2. تخمين أحمال التكييف وتصميم المنظومات (مدونة التبريد)" if lang == "AR" else "❄️ 2. HVAC Cooling Load Estimator"
    
    tab_insulation, tab_hvac = st.tabs([prog_1, prog_2])
    
    # ==================== 🧱 تشغيل واستدعاء برنامج العزل الحراري المعزول ====================
    with tab_insulation:
        render_insulation_program(lang, align)

    # ==================== ❄️ تشغيل واستدعاء برنامج أحمال التكييف المعزول ====================
    with tab_hvac:
        render_hvac_program(lang, align)
