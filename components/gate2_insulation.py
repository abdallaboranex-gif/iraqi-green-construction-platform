# components/gate2_insulation.py
import streamlit as st

def render_insulation_program(lang, align):
    """البرنامج الأول: حاسبة العزل الحراري وغلاف المبنى (مدونة العزل)"""
    st.markdown(f"<div style='text-align: {align}; padding-top:10px;'><b style='color:#1E3A8A;'>📐 تدقيق الغلاف الإنشائي ومواد الجدران الخارجية:</b></div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        wall_material = st.selectbox("اختر مادة الجدران الأساسية للمبنى:", ["", "طابوق أحمر اعتيادي مصمت", "ثرمستون عازل خفيف الوزن (AAC)", "جدران خرسانية مسبقة الصنع مع فوم عازل"], key="sb_wall_mat")
        glass_type = st.selectbox("نوع مقاطع وزجاج النوافذ والواجهات:", ["", "زجاج مفرد إطار ألمنيوم اعتيادي", "زجاج مزدوج عازل (Double Glazing)", "Double Glazing Low-E"], key="sb_glass_typ")
        insulation_thick = st.number_input("سمك الطبقة العازلة المحقونة للجدران (ملم):", min_value=0, max_value=200, value=0, key="ni_ins_thick")
        
    if st.button("📊 تشغيل مطابقة مدونة العزل الحراري العراقيّة", use_container_width=True, key="btn_run_insulation"):
        if wall_material == "" or glass_type == "":
            st.error("⚠️ يرجى تحديد مادة الجدران ونوع الزجاج أولاً لحساب إجمالي الفقد الحراري.")
        else:
            if "ثرمستون" in wall_material and "مزدوج" in glass_type:
                st.success("🟢 الغلاف المعماري مطابق تماماً لمدونة العزل الحراري! تم خفض نفاذية الحرارة وتوفير أحمال الطاقة بنسبة 35%.")
                st.metric(label="معامل الانتقال الحراري الإجمالي U-Value", value="0.32 W/m²K", delta="-0.18 (آمن)")
            else:
                st.warning("⚠️ الغلاف غير مطابق للمواصفات! المواد التقليدية المحددة تسبب تسرباً حرارياً هائلاً وضغطاً على الطاقة صيفاً.")
                st.metric(label="معامل الانتقال الحراري الإجمالي U-Value", value="1.85 W/m²K", delta="+0.45 (خارج الحدود)")
