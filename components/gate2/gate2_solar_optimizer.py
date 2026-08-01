# components/gate2_solar_optimizer.py
import streamlit as st

def render_solar_optimizer_section(align):
    """تحليل زاوية سقوط الشمس الإشعاعية وحساب إنتاجية ألواح الطاقة الشمسية المثالية للعراق"""
    st.markdown(f"<div style='text-align: {align}; padding-top:5px;'><b style='color:#1E3A8A;'>☀️ مدخلات زاوية واجهة العقار ومتطلبات الطاقة المستدامة:</b></div>", unsafe_allow_html=True)
    
    # سحب جغرافية العقار حياً من الخطوة 1 لمنع التكرار البصري
    gov = st.session_state.get("selected_gov", "Baghdad")
    corner_status = st.session_state.get("has_basement_sel", "")
    
    with st.container(border=True):
        facade_direction = st.selectbox("اتجاه واجهة البناء الرئيسية الحالية (Orientation):", ["", "شمال (North)", "جنوب (South)", "شرق (East)", "غرب (West)"], key="g2_facade_dir")
        target_solar_coverage = st.slider("نسبة تغطية أحمال المبنى الإجمالية عبر الطاقة الشمسية (%):", min_value=0, max_value=100, value=30, key="g2_solar_target")
        has_net_metering = st.checkbox("هل ترغب بربط المنظومة بنظام التغذية العكسية الوطني (Net Metering)؟", key="g2_net_meter")

    # 🧠 معادلات محاكاة زاوية ميل الشمس الكودية في خطوط العرض العراقية (Latitude ~33°N)
    optimal_angle = 32.0 if gov in ["Baghdad", "Salah_Al_Din", "Anbar", "Najaf"] else 36.0
    
    # حساب تقريبي أولي مبني على مساحة الأرض المخزنة بالذاكرة الحية
    land_w = st.session_state.get("land_width", 0.0)
    land_l = st.session_state.get("land_length", 0.0)
    est_area = land_w * land_l
    
    # تخمين السعة والعدد الفعلي للألواح المطلوبة
    required_kw = (est_area * (target_solar_coverage / 100.0) * 0.1) if est_area > 0 else 5.0
    panels_count = int((required_kw * 1000) / 550) + 1  # افتراض لوح طاقة قياسي سعة 550 واط
    
    st.session_state["g2_solar_data"] = {
        "facade_direction": facade_direction, "optimal_angle": optimal_angle,
        "required_kw": required_kw, "panels_count": panels_count, "target_coverage": target_solar_coverage
    }
    return facade_direction, optimal_angle, required_kw, panels_count
