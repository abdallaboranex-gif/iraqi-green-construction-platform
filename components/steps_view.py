# components/steps_view.py
import streamlit as st

def render_steps_and_calculators(L, lang):
    """رسم وإدارة شجرة الخطوات وبوابة الفلترة البلدية والموقعية المتقدمة لمدونة التربة"""
    
    # 1. تحديد الاتجاه البصري والمحاذاة الفورية حسب لغة النظام لضمان عدم الخربطة البصرية
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    
    # حقن الـ CSS الموضعي لتنعيم وتنسيق الصناديق وحقول الإدخال لتطابق الصورة المرجعية
    st.markdown("""
        <style>
            /* جعل حاويات التقرير تشبه الكروت المستقلة بخلفية بيضاء وظلال متناسقة */
            .compliance-card {
                background-color: white !important;
                padding: 16px !important;
                border-radius: 14px !important;
                border: 1px solid #E2E8F0 !important;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03) !important;
                margin-bottom: 12px !important;
            }
            .step-number {
                background-color: #E8F5E9;
                color: #2E7D32;
                border-radius: 50%;
                width: 28px;
                height: 28px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
                font-family: sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div dir="{direction}" style="margin-bottom: 15px; text-align: {align};">
        <span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; vertical-align: middle;">{L['phase']}</span> 
        <span style="font-weight: bold; font-size: 1.05rem; margin-left: 6px; margin-right: 6px; color: #1F2937;">{L['eng_comp']}</span> 
        <span style="font-size: 0.82rem; color: #6B7280;">{L['seq_order']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Step 1: تحليل الموقع والمحددات البلدية والأرضية (مكتملة ومترجمة) ---
    with st.container(border=True):
        c1, c2, c3 = st.columns([0.15, 1.0, 0.55])
        with c1:
            st.markdown("<div class='step-number'>1</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div style='font-weight: bold; font-size: 0.92rem; color: #1F2937; text-align: {align};'>{L['step1_title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 0.72rem; color: #9CA3AF; text-align: {align};'>{L['step1_desc']}</div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div style='text-align: {align}; color: #10B981; font-weight: bold; font-size: 0.82rem; margin-bottom: 3px;'>{L['completed']}</div>", unsafe_allow_html=True)
            st.button(L['dl_btn'], key="dl_s1", use_container_width=True)

    st.markdown(f"<div style='text-align: center; color: #D1D5DB; margin: -12px 0; font-size: 1.1rem;'>│</div>", unsafe_allow_html=True)

    # --- Step 2: تفعيل بداية ترويسة الخطوة الثانية النشطة لتدقيق التربة ---
    is_pending = st.session_state["step2_status"] == "In Progress"
    border_clr = "#F59E0B" if is_pending else "#10B981"
    badge_text = L['in_progress'] if is_pending else L['completed']
    badge_clr = "#F59E0B" if is_pending else "#10B981"
    
    st.markdown(f"""
    <div dir="{direction}" style="border: 1px solid #E5E7EB; padding: 14px; border-radius: 14px; background-color: white; margin-bottom: 8px; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-right: 4px solid {border_clr if lang == 'EN' else 'transparent'}; border-left: 4px solid {border_clr if lang == 'AR' else 'transparent'}; padding-right: 8px; padding-left: 8px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="background-color: #FFF3E0; color: #E65100; border-radius: 50%; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-family: sans-serif;">2</div>
                <div>
                    <div style="font-weight: bold; font-size: 0.92rem; color: #1F2937;">{L['step2_title']}</div>
                    <div style="font-size: 0.72rem; color: #6B7280;">{L['step2_desc']}</div>
                </div>
            </div>
            <div style="color: {badge_clr}; font-weight: bold; font-size: 0.82rem;">{badge_text}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div dir="{direction}" style="text-align: {align};">', unsafe_allow_html=True)
    # ==================== 📍 أولاً: بوابة المحددات البلدية والموقع الافتتاحية ====================
    stage_title = '📍 المرحلة (أ): بوابة المحددات البلدية والموقع الافتتاحية' if lang == 'AR' else 'Stage (A): Municipal & Location Zoning Gate'
    st.markdown(f"<h6 style='color: #1E3A8A; font-weight:bold; margin-bottom:10px;'>{stage_title}</h6>", unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        gov_lbl = "المحافظة ونطاق المشروع الجغرافي:" if lang == "AR" else "Governorate / Project Scope:"
        gov_opts = {
            "اختر المحافظة...": "",
            "بغداد": "Baghdad", "صلاح الدين": "Salah_Al_Din", "الأنبار": "Anbar", 
            "النجف الأشرف": "Najaf", "نينوى": "Nineveh", "البصرة": "Basra", 
            "المثنى": "Muthanna", "بابل": "Babil", "كربلاء المقدسة": "Karbala", 
            "ديالى": "Diyala", "كركوك": "Kirkuk", "ميسان": "Maysan", 
            "ذي قار": "Dhi_Qar", "القادسية": "Al_Qadisiyah", "واسِط": "Wasit", 
            "أربيل": "Erbil", "السليمانية": "Sulaymaniyah", "دهوك": "Duhok"
        } if lang == "AR" else {
            "Select Governorate...": "",
            "Baghdad": "Baghdad", "Salah Al-Din": "Salah_Al_Din", "Anbar": "Anbar", 
            "Najaf": "Najaf", "Nineveh": "Nineveh", "Basra": "Basra", 
            "Muthanna": "Muthanna", "Babil": "Babil", "Karbala": "Karbala", 
            "Diyala": "Diyala", "Kirkuk": "Kirkuk", "Maysan": "Maysan", 
            "Dhi Qar": "Dhi_Qar", "Al-Qadisiyah": "Al_Qadisiyah", "Wasit": "Wasit", 
            "Erbil": "Erbil", "Sulaymaniyah": "Sulaymaniyah", "Duhok": "Duhok"
        }
        selected_gov_txt = st.selectbox(gov_lbl, list(gov_opts.keys()))
        selected_gov = gov_opts[selected_gov_txt]
        
        req_type_lbl = "نوع الطلب / المعاملة:" if lang == "AR" else "Request / Permit Type:"
        req_opts = ["", "بناء جديد", "إعادة بناء", "إضافة طابق", "ترميم", "مشاريع كبرى"] if lang == "AR" else ["", "New Construction", "Reconstruction", "Floor Addition", "Renovation", "Major Projects"]
        selected_req = st.selectbox(req_type_lbl, req_opts)

        lot_num_lbl = "رقم قطعة العقار (سند طابو):" if lang == "AR" else "Plot / Parcel Number:"
        st.text_input(lot_num_lbl, value="", placeholder="مثال: 1024/5" if lang == "AR" else "e.g., 1024/5", key="lot_num")

    with col_f2:
        usage_lbl = "نوع استعمال العقار الأساسي:" if lang == "AR" else "Primary Land Usage:"
        usage_opts = ["", "سكني", "تجاري", "خدمي", "صناعي", "مجمعات"] if lang == "AR" else ["", "Residential", "Commercial", "Service", "Industrial", "Complexes"]
        selected_usage = st.selectbox(usage_lbl, usage_opts)

        width_lbl = "عرض الأرض / الواجهة (متر):" if lang == "AR" else "Land Width / Frontage (meters):"
        land_width = st.number_input(width_lbl, min_value=0.0, max_value=500.0, value=0.0, step=0.5)

        sector_num_lbl = "رقم المقاطعة والبلدية للعقار:" if lang == "AR" else "District / Sector Number:"
        st.text_input(sector_num_lbl, value="", placeholder="مثال: 42 مكة" if lang == "AR" else "e.g., 42 Mecca", key="sector_num")

    with col_f3:
        street_lbl = "عرض الشارع المقابل للعقار (m):" if lang == "AR" else "Opposite Street Width (m):"
        street_width = st.number_input(street_lbl, min_value=0.0, max_value=100.0, value=0.0, step=0.5)

        length_lbl = "طول الأرض / النزال (متر):" if lang == "AR" else "Land Length / Depth (meters):"
        land_length = st.number_input(length_lbl, min_value=0.0, max_value=500.0, value=0.0, step=0.5)

        corner_lbl = "موضع قطعة الأرض وتصنيفها:" if lang == "AR" else "Plot Orientation Class:"
        corner_opts = ["", "عادي / وسطي", "ركن / زاوية"] if lang == "AR" else ["", "Standard / Middle", "Corner Plot"]
        selected_corner = st.selectbox(corner_lbl, corner_opts)

    col_sub_f1, col_sub_f2 = st.columns(2)
    with col_sub_f1:
        basement_lbl = "هل يتضمن المخطط طابق سرداب (Basement)؟" if lang == "AR" else "Does it include a Basement floor?"
        basement_opts = ["", "موجود", "غير موجود"] if lang == "AR" else ["", "Present", "Not Present"]
        has_basement_sel = st.selectbox(basement_lbl, basement_opts)
        has_basement = True if has_basement_sel in ["موجود", "Present"] else False

    with col_sub_f2:
        floors_lbl = "عدد طوابق المبنى المقترحة فوق مستوى الأرض:" if lang == "AR" else "Proposed Floors Above Ground:"
        building_floors = st.number_input(floors_lbl, min_value=0, max_value=60, value=0)

    user_area = land_width * land_length

    if building_floors > 0:
        if building_floors >= 4 or has_basement:
            structural_class_txt = "🏢 منشأ ثقيل / أحمال حرجة عالية" if lang == "AR" else "🏢 Heavy Structure / High Load Class"
            structural_class_clr = "#DC2626"
            is_heavy_structure = True
        else:
            structural_class_txt = "🏡 منشأ خفيف / أحمال اعتيادية منخفضة" if lang == "AR" else "🏡 Light Structure / Normal Load Class"
            structural_class_clr = "#10B981"
            is_heavy_structure = False
            
        st.markdown(f"""
        <div style="background-color: #F8FAFC; padding: 12px; border-radius: 8px; border-right: 4px solid {structural_class_clr}; border-left: 4px solid {structural_class_clr if lang == 'AR' else 'transparent'}; margin-top: 10px; margin-bottom: 12px;">
            <span style="font-size: 0.8rem; color: #4B5563;">{'🧠 استنتاج عقل النظام التلقائي لثقل ومساحة العقار:' if lang == 'AR' else '🧠 System Automatic Structural Load & Area Inference:'}</span><br>
            <b style="color: {structural_class_clr}; font-size: 0.95rem;">{structural_class_txt} | {'المساحة المستنتجة:' if lang == 'AR' else 'Calculated Area:'} {user_area:.1f} m²</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    # ==================== 🔬 ثانياً: الفحوصات الجيوتقنية المطلوبة والمعطيات ====================
    stage_b_title = '🔬 المرحلة (ب): الفحوصات المطلوبة ونتائج تقرير المختبر' if lang == 'AR' else 'Stage (B): Required Tests & Laboratory Results'
    st.markdown(f"<h6 style='color: #3B82F6; font-weight:bold; margin-bottom:10px;'>{stage_b_title}</h6>", unsafe_allow_html=True)
    
    # 🧠 طباعة قائمة الفحوصات المطلوبة استباقياً بناءً على فلترة المرحلة (أ) داخل كارت رمادي مستقل
    if building_floors > 0 and selected_gov != "":
        st.markdown(f"<div class='compliance-card' style='background-color: #FAFAFA; border: 1px dashed #CBD5E1;'>", unsafe_allow_html=True)
        st.markdown(f"<b>📋 {'الفحوصات والاشتراطات الإلزامية المقرة لهذا المشروع كودياً:' if lang == 'AR' else 'Mandatory Code Requirements For This Project:'}</b>", unsafe_allow_html=True)
        
        if is_heavy_structure:
            bh_text = "• مطلوب 3 حفر اختبارية (Boreholes) كحد أدنى بعمق لا يقل عن 15 متراً لتأمين حسابات السرداب والأحمال." if lang == "AR" else "• Min 3 Boreholes required with depth >= 15m for basement/heavy loads."
        else:
            if user_area <= 400:
                bh_text = "• مطلوب حفرتان اختباريتان فقط (Boreholes) بعمق لا يقل عن 6 أمتار بموجب مساحة الأرض (الجدول 2-1)." if lang == "AR" else "• 2 Boreholes required with depth >= 6m based on land area."
            else:
                bh_text = "• مطلوب 3 حفر اختبارية كحد أدنى بعمق لا يقل عن 6 أمتار لتجاوز مساحة الأرض 400 م²." if lang == "AR" else "• Min 3 Boreholes required with depth >= 6m due to area > 400m²."
        st.markdown(f"<div style='color:#1E40AF; font-size:0.82rem; margin-top:4px;'>{bh_text}</div>", unsafe_allow_html=True)
        
        if has_basement:
            h2o_text = "• ⚠️ شرط حرج: يتوجب تدقيق منسوب المياه الجوفية الحركي الميداني وإجراء فحص التحليل الكيميائي لعدوانية المياه." if lang == "AR" else "• ⚠️ Critical: Groundwater level measurement & chemical aggressiveness tests are mandatory."
            st.markdown(f"<div style='color:#DC2626; font-size:0.82rem; margin-top:2px;'>{h2o_text}</div>", unsafe_allow_html=True)
            
        if selected_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
            gyp_txt = f"• قيد جيوكيميائي: يقع الموقع ضمن نطاق التربة الجبسية، مطلوب فحص الجبس الكلي والانهيارية تحت النقع." if lang == "AR" else "• Gypseous Soil zone: Gypsum content & collapsible soil tests are mandatory."
            st.markdown(f"<div style='color:#B45309; font-size:0.82rem; margin-top:2px;'>{gyp_txt}</div>", unsafe_allow_html=True)
            
        if selected_gov in ["Najaf", "Muthanna"]:
            void_txt = "• قيد جيولوجي خاص: مطلوب إرفاق فحص المسح الراداري الأرضي (GPR Void Scan) لضمان خلو الموقع من التكهفات الكلسية." if lang == "AR" else "• Geological Zone: GPR Void Scan is mandatory to rule out limestone cavities."
            st.markdown(f"<div style='color:#701A75; font-size:0.82rem; margin-top:2px;'>{void_txt}</div>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)

    # حقل رفع تقرير المختبر الجيوتقني
    uploaded_file = st.file_uploader(L['file_uploader_lbl'], type=["pdf"])
    
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        bearing_cap = st.number_input(L['input_bearing'], min_value=10, max_value=500, value=120)
        if selected_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
            gypsum = st.number_input(L['input_gypsum'], min_value=0.0, max_value=100.0, value=4.50)
        else:
            gypsum = 1.0
            
    with sub_col2:
        actual_bh_depth_lbl = "أقصى عمق واصلة له الحفرة الاختبارية ميدانياً (متر):" if lang == "AR" else "Maximum Actual Borehole Depth Executed (meters):"
        actual_bh_depth = st.number_input(actual_bh_depth_lbl, min_value=0.0, max_value=120.0, value=6.0, step=0.5)

        auth_opts = [L['auth_yes'], L['auth_no']]
        report_status_sel = st.selectbox(L['input_auth'], auth_opts)
        report_status = "معتمد ومجاز ومصادق" if report_status_sel == L['auth_yes'] else "غير مصادق"
        
    # تشغيل الفحص والتحقق الرقمي السداسي المربوط بملف الإكسل
    if st.button(L['run_audit'], type="primary", use_container_width=True):
        if not selected_gov or not selected_req or not selected_usage or land_width == 0 or land_length == 0 or selected_corner == "":
            st.error("⚠️ يرجى ملء كافة محددات المرحلة (أ) الافتتاحية والموقع وتحديد الأبعاد وموضع قطعة الأرض أولاً.")
        else:
            try:
                from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
                excel_engine = IraqiDynamicComplianceEngine(excel_filename="soil_testing.xlsx")
                
                payload = {
                    "governorate": selected_gov, "total_land_area_m2": user_area,
                    "soil_bearing_capacity": bearing_cap, "soil_report_status": report_status, 
                    "actual_gypsum_percentage": gypsum, "is_heavy_structure": is_heavy_structure,
                    "actual_borehole_depth_meters": actual_bh_depth,
                    "lot_num": st.session_state.get("lot_num", ""),
                    "sector_num": st.session_state.get("sector_num", ""),
                    "building_floors": building_floors
                }
                
                soil_result = excel_engine.validate_soil_report(payload)
                st.markdown(L['soil_report_header'])
                
                if soil_result["status"] == "PASSED":
                    st.success(soil_result["summary"])
                    st.session_state["compliance_rate"] = 68
                    st.session_state["step2_status"] = "Completed"
                    
                    pdf_path = excel_engine.generate_pdf_report(payload, soil_result, "Soil_Compliance_Success.pdf")
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="📥 تحميل شهادة المطابقة الرسمية (PDF)", data=f, file_name="Soil_Compliance_Success.pdf", mime="application/pdf", use_container_width=True)
                else:
                    st.error(soil_result["summary"])
                    
                    pdf_path = excel_engine.generate_pdf_report(payload, soil_result, "Soil_Compliance_Failures.pdf")
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="📥 تحميل تقرير المخالفات والرفض الرسمي (PDF)", data=f, file_name="Soil_Compliance_Failures.pdf", mime="application/pdf", use_container_width=True)
                    
                    for idx, failure in enumerate(soil_result["failures"], 1):
                        st.markdown(f"<div class='compliance-card'>", unsafe_allow_html=True)
                        st.markdown(f"### ⚠️ المخالفة رقم {idx}:")
                        st.markdown(f"<div style='background-color:#FEF2F2; padding:8px; border-right:4px solid #DC2626; margin-bottom:5px; font-weight:bold;'>{failure['severity']}</div>", unsafe_allow_html=True)
                        st.markdown(f"**{failure['title']}**")
                        st.info(failure['citizen_exp'])
                        st.warning(failure['engineer_exp'])
                        st.success(failure['resolution'])
                        st.markdown(f"<div style='color:#991B1B; background-color:#FEE2E2; padding:8px; border-radius:4px;'><b>🚨 الأثر والعقوبة البلدية:</b> {failure['legal_penalty']}</div>", unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                        st.divider()
                        
            except Exception as e:
                st.error(f"حدث خطأ في معالجة البيانات: {str(e)}")
            
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='text-align: center; color: #D1D5DB; margin: -12px 0; font-size: 1.1rem;'>│</div>", unsafe_allow_html=True)

    # --- الخطوات المغلقة المتسلسلة (Step 3, 4, 5) الانتظارية المقفلة بنظام الكروت الأنيقة ---
    steps_data = [("3", L['step3_title']), ("4", L['step4_title']), ("5", L['step5_title'])]
    for step_num, step_title in steps_data:
        with st.container(border=True):
            c1, c2, c3 = st.columns([0.15, 1.0, 0.4])
            with c1: st.markdown("<div>🔒</div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div style='font-weight: bold; font-size: 0.92rem; color: #9CA3AF; text-align: {align};'>{step_title}</div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div style='text-align: right; color: #9CA3AF; font-weight: bold; font-size: 0.82rem;'>{L['locked']}</div>", unsafe_allow_html=True)

    # بنر الباقة المهنية المدفوعة
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div dir="{direction}" style="background-color: #0F172A; color: white; padding: 18px; border-radius: 14px; text-align: {align}; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 1rem; margin-bottom: 4px; color: #F59E0B;">{L['premium_title']}</div>
        <div style="font-size: 0.78rem; color: #94A3B8;">{L['premium_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
