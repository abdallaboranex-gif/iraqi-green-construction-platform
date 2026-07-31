# components/steps_view.py
import streamlit as st
from components.step1_zoning import render_step1
from components.step2_soil import render_step2
from components.step2_soil_executor import run_soil_compliance_audit

def render_steps_and_calculators(L, lang):
    """الموزع والمستدعي الرقمي لملفات الخطوات المنفصلة والمستدامة للمنصة السيادية"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    
    # 1. استدعاء ورسم الخطوة الأولى المعزولة بالكامل
    is_step1_ready, user_area, building_floors, selected_gov, has_basement = render_step1(L, lang, direction, align)
    
    # 2. استدعاء ورسم الخطوة الثانية ومقاييس فحص المختبر المعزولة
    render_step2(L, lang, direction, align, is_step1_ready, user_area, building_floors, selected_gov, has_basement)
    
    # 3. تشغيل زر الفحص والتحقق والـ PDF حركياً فور فتح الخطوة الثانية
    if is_step1_ready:
        run_soil_compliance_audit(L, lang, user_area, building_floors, selected_gov, st.session_state.get("lot_num", ""), st.session_state.get("sector_num", ""))
        
    # 4. رسم الخطوات الانتظارية الثلاث المتبقية المقفلة (Step 3, 4, 5)
    st.markdown(f"<div style='text-align: center; color: #D1D5DB; margin: -12px 0; font-size: 1.1rem;'>│</div>", unsafe_allow_html=True)
    for step_num, step_title in [("3", L['step3_title']), ("4", L['step4_title']), ("5", L['step5_title'])]:
        with st.container(border=True):
            c1, c2, c3 = st.columns([0.15, 1.0, 0.4])
            with c1: st.markdown("<div>🔒</div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div style='font-weight: bold; font-size: 0.92rem; color: #9CA3AF; text-align: {align};'>{step_title}</div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div style='text-align: right; color: #9CA3AF; font-weight: bold; font-size: 0.82rem;'>{L['locked']}</div>", unsafe_allow_html=True)

    # بنر الحزمة المهنية المدفوعة بأسفل القطاع الإنشائي
    st.markdown(f"<br><div dir='{direction}' style='background-color: #0F172A; color: white; padding: 18px; border-radius: 14px; text-align: {align}; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'><div style='font-weight: bold; font-size: 1rem; margin-bottom: 4px; color: #F59E0B;'>{L['premium_title']}</div><div style='font-size: 0.78rem; color: #94A3B8;'>{L['premium_desc']}</div></div>", unsafe_allow_html=True)
