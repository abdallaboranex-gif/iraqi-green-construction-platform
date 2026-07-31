# components/step2_soil.py
import streamlit as st

def render_step2(L, lang, direction, align, is_step1_ready, user_area, building_floors, selected_gov, has_basement):
    """رسم وإدارة الخطوة الثانية: فحوصات التربة والمختبر الجيوتقني والمياه الجوفية"""
    
    if not is_step1_ready:
        st.markdown(f"""
        <div dir="{direction}" style="border: 1px dashed #CBD5E1; padding: 15px; border-radius: 14px; background-color: #FAFAFA; margin-bottom: 12px; text-align: {align};">
            <div style="display: flex; justify-content: space-between; align-items: center; padding-right: 8px; padding-left: 8px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="color: #9CA3AF;">🔒</div>
                    <div>
                        <div style="font-weight: bold; font-size: 0.92rem; color: #9CA3AF;">{L['step2_title']}</div>
                        <div style="font-size: 0.72rem; color: #9CA3AF;">{'يرجى إكمال وإدخال كافة بيانات الفلترة في الخطوة الأولى لفتح هذا قطاع الفحص' if lang == 'AR' else 'Please complete step 1 zoning fields to unlock this geotechnical section.'}</div>
                    </div>
                </div>
                <div style="color: #9CA3AF; font-weight: bold; font-size: 0.82rem;">{L['locked']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    is_heavy_structure = building_floors >= 4 or has_basement
    is_pending = st.session_state["step2_status"] == "In Progress"
    border_clr = "#F59E0B" if is_pending else "#10B981"
    badge_text = L['in_progress'] if is_pending else L['completed']
    badge_clr = "#F59E0B" if is_pending else "#10B981"
    
    st.markdown(f"""
    <div dir="{direction}" style="border: 1px solid #E5E7EB; padding: 15px; border-radius: 14px; background-color: white; margin-bottom: 12px; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; border-right: 4px solid {border_clr if lang == 'EN' else 'transparent'}; border-left: 4px solid {border_clr if lang == 'AR' else 'transparent'}; padding-right: 8px; padding-left: 8px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div class='step-number-pending'>2</div>
                <div>
                    <div style="font-weight: bold; font-size: 0.92rem; color: #1F2937;">{L['step2_title']}</div>
                    <div style="font-size: 0.72rem; color: #6B7280;">{L['step2_desc']}</div>
                </div>
            </div>
            <div style="color: {badge_clr}; font-weight: bold; font-size: 0.82rem;">{badge_text}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div dir="{direction}" style="text-align: {align}; padding: 5px 10px;">', unsafe_allow_html=True)
    
    # 🧠 طباعة قائمة الفحوصات المستنتجة كودياً
    st.markdown(f"<div class='compliance-card' style='background-color: #FAFAFA; border: 1px dashed #CBD5E1; padding:12px; margin-bottom:12px;'>", unsafe_allow_html=True)
    st.markdown(f"<b>📋 {'الفحوصات والاشتراطات الإلزامية المقرة لهذا المشروع كودياً:' if lang == 'AR' else 'Mandatory Code Requirements:'}</b>", unsafe_allow_html=True)
    
    if is_heavy_structure:
        bh_text = "• مطلوب 3 حفر اختبارية (Boreholes) كحد أدنى بعمق لا يقل عن 15 متراً لتأمين حسابات السرداب والأحمال الثقيلة." if lang == "AR" else "• Min 3 Boreholes required with depth >= 15m for basement/heavy loads."
    else:
        bh_text = ("• مطلوب حفرتان اختباريتان فقط (Boreholes) بعمق لا يقل عن 6 أمتار بموجب مساحة الأرض المستنتجة (الجدول 2-1)." if user_area <= 400 else "• مطلوب 3 حفر اختبارية كحد أدنى بعمق لا يقل عن 6 أمتار لتجاوز مساحة الأرض 400 م².") if lang == "AR" else "• Boreholes count and depth dynamically checked based on area."
    st.markdown(f"<div style='color:#1E40AF; font-size:0.82rem; margin-top:4px;'>{bh_text}</div>", unsafe_allow_html=True)
    
    if has_basement:
        h2o_text = "• ⚠️ شرط حرج: يتوجب تدقيق منسوب المياه الجوفية الحركي الميداني وإجراء فحص التحليل الكيميائي لعدوانية المياه الجوفية." if lang == "AR" else "• ⚠️ Critical: Groundwater and chemical tests are mandatory."
        st.markdown(f"<div style='color:#DC2626; font-size:0.82rem; margin-top:2px;'>{h2o_text}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(L['file_uploader_lbl'], type=["pdf"])
    sub_col1, sub_col2, sub_col3 = st.columns(3)
    with sub_col1:
        bearing_cap = st.number_input(L['input_bearing'], min_value=0, max_value=500, value=0)
        gypsum = st.number_input(L['input_gypsum'], min_value=0.0, max_value=100.0, value=0.0, step=0.1) if selected_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"] else 0.0
    with sub_col2:
        actual_bh_depth = st.number_input("أقصى عمق للحفرة ميدانياً (متر):", min_value=0.0, max_value=120.0, value=0.0, step=0.5)
        report_status_sel = st.selectbox(L['input_auth'], ["", L['auth_yes'], L['auth_no']])
        report_status = "معتمد ومجاز ومصادق" if report_status_sel == L['auth_yes'] else ("غير مصادق" if report_status_sel == L['auth_no'] else "")
    with sub_col3:
        if has_basement:
            water_table = st.number_input("منسوب المياه الجوفية المقاس (متر):", min_value=0.0, max_value=50.0, value=0.0, step=0.1)
            w_opts = ["", "مطابق وضمن الحدود الآمنة", "عدواني جداً"] if lang == "AR" else ["", "Compliant", "Highly Aggressive"]
            water_chem_status = st.selectbox("فحص عدوانية المياه الجوفية:", w_opts)
        else:
            water_table, water_chem_status = 20.0, "مطابق وضمن الحدود الآمنة"
            
    # [ملاحظة: زر التشغيل والتحقق بالإكسل سينتقل للجزء الأخير التابع لـ ملف step2 لتأمين قصر الكود]
    st.session_state["temp_soil_inputs"] = {
        "bearing": bearing_cap, "gypsum": gypsum, "depth": actual_bh_depth, "status": report_status,
        "water_table": water_table, "water_chem": water_chem_status, "is_heavy": is_heavy_structure
    }
    st.markdown("</div></div>", unsafe_allow_html=True)
