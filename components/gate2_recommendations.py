# components/gate2_recommendations.py
import streamlit as st

def render_energy_recommendations(align, direction, lang):
    """قراءة واقع العقار من الجلسة الحية وتفجير التوصيات الذكية وهندسة القيمة وحساب الألواح"""
    
    # 📥 جلب داتا الملفات الثلاثة السابقة بأمان من الذاكرة الحية
    ins_data = st.session_state.get("g2_insulation_data", {})
    solar_data = st.session_state.get("g2_solar_data", {})
    hvac_data = st.session_state.get("g2_hvac_data", {})
    
    # سحب محددات الفلترة الجغرافية من الخطوة الأولى لمنع تكرار الإدخال
    gov = st.session_state.get("selected_gov", "")
    corner_status = st.session_state.get("selected_corner", "")
    
    u_value = ins_data.get("u_value", 2.0)
    facade = solar_data.get("facade_direction", "")
    panels = solar_data.get("panels_count", 0)
    kw_req = solar_data.get("required_kw", 0.0)
    angle = solar_data.get("optimal_angle", 32.0)
    
    # 🚨 تفعيل زر تفجير التوصيات والحلول الاستشارية المخصصة لواقع هذا العقار
    if st.button("🧠 تشغيل مستشار الاستدامة وتوليد الحلول والتوصيات الذكية للعقار", type="primary", use_container_width=True, key="btn_run_gate2_ai"):
        st.markdown(f"<div style='text-align: {align}; margin-top:15px;'><b style='color:#10B981;'>📈 التقرير الاستشاري السيادي وتوصيات هندسة القيمة الكفاءة الطاقة:</b></div>", unsafe_allow_html=True)
        
        # 🏢 1. مخرجات وتوصيات مدونة العزل وغلاف المبنى المعماري
        st.markdown(f"<div class='compliance-card'>", unsafe_allow_html=True)
        st.markdown(f"#### 🧱 [مدونة العزل]: معامل الانتقال الحراري الحالي: U = {u_value:.3f} W/m²K")
        if u_value <= 0.45:
            st.success("🟢 غلاف المبنى المعماري مطابق للمواصفة العراقية! معامل الانتقال الحراري ممتاز ومقاوم للحرارة.")
        else:
            st.warning("⚠️ غلاف المبنى الحالي غير مطابق (يتجاوز الحد الأقصى 0.45).")
            st.markdown(f"💡 <b>توصية هندسة القيمة البديلة بأقل كلفة:</b> بدلاً من عزل البيت بالكامل، يكفي حقن الجدران الخارجية بطبقة 5 سم من البوليسترين البثقي (XPS) وعزل السقف كونه المصدر الأول لامتصاص 40% من حرارة شمس الظهيرة العمودية في العراق.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # ❄️ 2. مخرجات وتوصيات التكييف والتهوئة الميكانيكية للسراديب
        st.markdown(f"<div class='compliance-card'>", unsafe_allow_html=True)
        st.markdown(f"#### ❄️ [مدونة التبريد]: تخمين منظومات الـ HVAC وحماية السراديب")
        if "Heat Recovery" in hvac_data.get("fresh_air_control", ""):
            st.success(f"{hvac_data.get('efficiency_txt', '')} • السعة الطنية ممتازة وتم خفض الاستهلاك الفعلي.")
        else:
            st.warning("⚠️ المنظومة المحددة تسبب هدراً طاقياً هائلاً وضغطاً على شبكة الكهرباء الوطنية صيفاً.")
            st.markdown(f"💡 <b>توصية ميكانيكية ذكية:</b> يتوجب تركيب كاسرات شمس أفقية للواجهات الجنوبية لصد شمس الظهيرة العمودية، وكاسرات شمس عمودية (Vertical Louvers) للواجهات الغربية والشرقية لصد أشعة الشمس الحرجة والمائلة عصراً وصباحاً. هذا يقلص السعة الطنية المطلوبة من 25 طناً إلى 16 طناً فقط، مما يوفر كلف الشراء وفاتورة الطاقة الشهريّة.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # ☀️ 3. مخرجات وتوجيه الألواح الشمسية وإنتاجيتها المستدامة
        st.markdown(f"<div class='compliance-card'>", unsafe_allow_html=True)
        st.markdown(f"#### ☀️ [المنظومة الشمسية والتحليل الإشعاعي]: السعة المستهدفة: {kw_req:.2f} kWp")
        st.info(f"📊 <b>العدد الدقيق للألواح الشمسية المطلوبة:</b> {panels} لوح طاقة قياسي (سعة 550 واط لكل لوح) لتغطية نسبة الأحمال المستهدفة.")
        st.markdown(f"🎯 <b>توجيه الألواح الجغرافي المثالي في العراق:</b> يتوجب توجيه الخلايا الشمسية نحو <b>الجنوب الجغرافي الصافي (True South) بزاية ميل زاوية ثابتة تتراوح بين {angle}° إلى 35° صيفاً وشتاءً</b>؛ لتحقيق أعلى إنتاجية مستدامة وكفاءة امتصاص للأشعة وحماية الخلايا الضوئية طوال العام.")
        st.markdown("</div>", unsafe_allow_html=True)
