# components/gate2_insulation.py
import streamlit as st

def render_insulation_section(align):
    """حساب المقاومة ومعامل الانتقال الحراري الإجمالي للغلاف الإنشائي"""
    st.markdown(f"<div style='text-align: {align}; padding-top:5px;'><b style='color:#1E3A8A;'>🧱 مدخلات الغلاف الإنشائي والمواد المستخدمة:</b></div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        wall_material = st.selectbox("مادة البناء الأساسية للجدران الخارجية:", ["", "طابوق أحمر اعتيادي مصمت", "ثرمستون عازل خفيف (AAC)", "جدران خرسانية مسبقة الصنع"], key="g2_wall_mat")
        wall_thick = st.number_input("سمك الجدار الكلي (سم):", min_value=10.0, max_value=100.0, value=24.0, step=1.0, key="g2_wall_thick")
        glass_type = st.selectbox("نوع مقاطع وزجاج النوافذ والفتحات المعمارية:", ["", "زجاج مفرد إطار ألمنيوم اعتيادي", "زجاج مزدوج عازل (Double Glazing)", "Double Glazing Low-E"], key="g2_glass_typ")
        roof_insulation = st.checkbox("هل تم حقن السقف بطبقة عزل حراري (فوم/بوليسترين)؟", key="g2_roof_ins")

    # حساب معامل الـ U-Value الرياضي المبدئي
    base_r = 0.50 if "ثرمستون" in wall_material else (0.30 if "خرسانة" in wall_material else 0.20)
    ins_r = 1.5 if roof_insulation else 0.0
    total_r = base_r + (wall_thick / 100.0) + ins_r
    u_value = 1.0 / total_r if total_r > 0 else 2.0
    
    st.session_state["g2_insulation_data"] = {
        "wall_material": wall_material, "glass_type": glass_type, 
        "u_value": u_value, "roof_insulation": roof_insulation
    }
    return u_value
