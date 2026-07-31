# components/gate2_sustainability.py
import streamlit as st

# استدعاء العمليات الأربعة المعزولة
from components.gate2_insulation import render_insulation_section
from components.gate2_solar_optimizer import render_solar_optimizer_section
from components.gate2_hvac import render_hvac_section
from components.gate2_recommendations import render_energy_recommendations

def render_sustainability_gate(L, lang, direction, align):
    """الموزع الرقمي المرن لبوابة الاستدامة - يدعم الإدخال المستقل أو الأتمتة التلقائية"""
    
    st.markdown(f"""
    <div class='compliance-card' style='text-align: {align};'>
        <h4 style='color: #10B981; margin-top:0;'>🌱 {L['gate_2_title']}</h4>
        <p style='color: #6B7280; font-size: 0.88rem;'>المنظومة الإلكترونية المستقلة للتحقق والتدقيق الذكي لمدونات الطاقة والتكييف والتثليج لجمهورية العراق.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 🧠 فحص ذكي: هل توجد معطيات قادمة من البوابة الأولى؟
    has_b1_gov = st.session_state.get("selected_gov", "") != ""
    has_b1_dim = st.session_state.get("land_width", 0.0) > 0.0 and st.session_state.get("land_length", 0.0) > 0.0

    # 📥 في حال كانت البوابة الأولى فارغة، يتم فتح قطاع مدخلات سريع وخاص بالاستدامة في الأعلى فوراً
    if not (has_b1_gov and has_b1_dim):
        st.markdown(f"<div style='text-align: {align};'><b style='color:#D97706;'>📍 لم يتم ملء البوابة الأولى - تفعيل استمارة المدخلات الجغرافية المستقلة:</b></div>", unsafe_allow_html=True)
        with st.container(border=True):
            col_s1, col_s2, col_s3 = st.columns(3)
            with col_s1:
                gov_opts = {"اختر المحافظة...": "", "بغداد": "Baghdad", "صلاح الدين": "Salah_Al_Din", "الأنبار": "Anbar", "النجف الأشرف": "Najaf", "نينوى": "Nineveh", "البصرة": "Basra", "المثنى": "Muthanna"}
                # حفظ القيمة المستقلة مباشرة في نفس متغير الذاكرة الأصلي ليعمل المحرك بسلاسة
                sel_gov = st.selectbox("المحافظة ونطاق الطقس الحالي للمشروع:", list(gov_opts.keys()), key="g2_solo_gov")
                if sel_gov != "": st.session_state["selected_gov"] = gov_opts[sel_gov]
            with col_s2:
                st.session_state["land_width"] = st.number_input("عرض واجهة الأرض الحالية (m):", min_value=0.0, step=0.5, key="g2_solo_width")
            with col_s3:
                st.session_state["land_length"] = st.number_input("طول نزال الأرض الحالي (m):", min_value=0.0, step=0.5, key="g2_solo_length")
        st.markdown("<br>", unsafe_allow_html=True)

    # 🟢 فرش حقول البرامج الأربعة المتتالية تحت بعضها؛ لتفتح فوراً وبكفاءة مطلقة سواء سحبت البيانات أو أدخلت هنا
    u_value = render_insulation_section(align)
    st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #E2E8F0;'>", unsafe_allow_html=True)
    
    facade_dir, opt_angle, req_kw, panels_cnt = render_solar_optimizer_section(align)
    st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px dashed #E2E8F0;'>", unsafe_allow_html=True)
    
    hvac_type, fresh_control, req_cfm = render_hvac_section(align)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # تشغيل واستدعاء محرك التوصيات وحسابات الألواح والحلول الذكية بناءً على واقع المعطيات المتوفرة
    render_energy_recommendations(align, direction, lang)
