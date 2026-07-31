# components/steps_view.py
import streamlit as st

def render_steps_and_calculators(L, lang):
    """رسم شجرة الخطوات المفلترة هندسياً طبق الأصل وبأعلى دقة وثبات"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    
    # حقن الـ CSS الموضعي لتنعيم وتنسيق الكروت وحواف صناديق الفلترة
    st.markdown("""
        <style>
            .compliance-card {
                background-color: white !important; padding: 16px !important;
                border-radius: 14px !important; border: 1px solid #E2E8F0 !important;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03) !important; margin-bottom: 12px !important;
            }
            .step-number {
                background-color: #E8F5E9; color: #2E7D32; border-radius: 50%;
                width: 28px; height: 28px; display: flex; align-items: center;
                justify-content: center; font-weight: bold; font-family: sans-serif;
            }
            .step-number-pending {
                background-color: #FFF3E0; color: #E65100; border-radius: 50%;
                width: 28px; height: 28px; display: flex; align-items: center;
                justify-content: center; font-weight: bold; font-family: sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)
    # تفعيل وإرساء قيم الذاكرة الحية للمحددات الـ 12 لمنع تصفير الحقول
    if "selected_gov" not in st.session_state: st.session_state["selected_gov"] = ""
    if "selected_req" not in st.session_state: st.session_state["selected_req"] = ""
    if "selected_usage" not in st.session_state: st.session_state["selected_usage"] = ""
    if "selected_corner" not in st.session_state: st.session_state["selected_corner"] = ""
    if "has_basement_sel" not in st.session_state: st.session_state["has_basement_sel"] = ""
    if "land_width" not in st.session_state: st.session_state["land_width"] = 0.0
    if "land_length" not in st.session_state: st.session_state["land_length"] = 0.0
    if "building_floors" not in st.session_state: st.session_state["building_floors"] = 0

    # حساب منطق الجاهزية الحية: هل أدخل المدقق كافة الحقول الأساسية؟
    is_step1_ready = (
        st.session_state["selected_gov"] != "" and 
        st.session_state["selected_req"] != "" and 
        st.session_state["selected_usage"] != "" and 
        st.session_state["selected_corner"] != "" and 
        st.session_state["has_basement_sel"] != "" and 
        st.session_state["land_width"] > 0.0 and 
        st.session_state["land_length"] > 0.0 and 
        st.session_state["building_floors"] > 0
    )

    # تحديد ألوان وحالة الصندوق الأول بناءً على اكتمال تعبئة البيانات
    if is_step1_ready:
        step1_border, step1_badge, step1_badge_clr = "#10B981", L['completed'], "#10B981"
    else:
        step1_border = "#F59E0B"
        step1_badge = "🟡 يرجى إدخال البيانات الموقعية" if lang == "AR" else "🟡 Please Input Zoning Data"
        step1_badge_clr = "#F59E0B"
       # --- 🏢 الخطوة 1: تحليل الموقع والمحددات البلدية الـ 12 للعقار ---
    st.markdown(f"""
    <div dir="{direction}" style="border: 1px solid {step1_border}; padding: 15px; border-radius: 14px; background-color: white; margin-bottom: 12px; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; padding-right: 8px; padding-left: 8px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div class='step-number'>1</div>
                <div>
                    <div style="font-weight: bold; font-size: 0.92rem; color: #1F2937;">{L['step1_title']}</div>
                    <div style="font-size: 0.72rem; color: #6B7280;">{L['step1_desc']}</div>
                </div>
            </div>
            <div style="color: {step1_badge_clr}; font-weight: bold; font-size: 0.82rem;">{step1_badge}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div dir="{direction}" style="text-align: {align}; padding: 5px 10px;">', unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns(3)
        gov_lbl = "المحافظة ونطاق المشروع الجغرافي:" if lang == "AR" else "Governorate / Project Scope:"
        gov_opts = {
            "اختر المحافظة...": "", "بغداد": "Baghdad", "صلاح الدين": "Salah_Al_Din", "الأنبار": "Anbar", 
            "النجف الأشرف": "Najaf", "نينوى": "Nineveh", "البصرة": "Basra", "المثنى": "Muthanna", 
            "بابل": "Babil", "كربلاء المقدسة": "Karbala", "ديالى": "Diyala", "كركوك": "Kirkuk", 
            "ميسان": "Maysan", "ذي قار": "Dhi_Qar", "القادسية": "Al_Qadisiyah", "واسِط": "Wasit", 
            "أربيل": "Erbil", "السليمانية": "Sulaymaniyah", "دهوك": "Duhok"
        }
        gov_list = list(gov_opts.keys())
        
        # تصحيح دالة البحث السريع لحساب الـ Index وحمايتها بـ try لمنع أي ValueError نهائياً
        idx_gov = 0
        try:
            if st.session_state["selected_gov"] != "":
                for k, v in gov_opts.items():
                    if v == st.session_state["selected_gov"]:
                        idx_gov = gov_list.index(k)
                        break
        except:
            idx_gov = 0
                    
        selected_gov_txt = st.selectbox(gov_lbl, gov_list, index=idx_gov)
        st.session_state["selected_gov"] = gov_opts[selected_gov_txt]
        
        req_type_lbl = "نوع الطلب / المعاملة:" if lang == "AR" else "Request / Permit Type:"
        req_opts = ["", "بناء جديد", "إعادة بناء", "إضافة طابق", "ترميم", "مشاريع كبرى"] if lang == "AR" else ["", "New Construction", "Reconstruction", "Floor Addition", "Renovation", "Major Projects"]
        
        idx_req = 0
        try:
            if st.session_state["selected_req"] in req_opts:
                idx_req = req_opts.index(st.session_state["selected_req"])
        except:
            idx_req = 0
            
        st.session_state["selected_req"] = st.selectbox(req_type_lbl, req_opts, index=idx_req)


        lot_num_lbl = "رقم قطعة العقار (سند طابو):" if lang == "AR" else "Plot / Parcel Number:"
        lot_num_val = st.text_input(lot_num_lbl, value="", placeholder="مثال: 1024/5", key="lot_num")

        lot_num_lbl = "رقم قطعة العقار (سند طابو):" if lang == "AR" else "Plot / Parcel Number:"
        lot_num_val = st.text_input(lot_num_lbl, value="", placeholder="مثال: 1024/5", key="lot_num")
    with col_f2:
        usage_lbl = "نوع استعمال العقار الأساسي:" if lang == "AR" else "Primary Land Usage:"
        usage_opts = ["", "سكني", "تجاري", "خدمي", "صناعي", "مجمعات"] if lang == "AR" else ["", "Residential", "Commercial", "Service", "Industrial", "Complexes"]
        idx_use = usage_opts.index(st.session_state["selected_usage"]) if st.session_state["selected_usage"] in usage_opts else 0
        st.session_state["selected_usage"] = st.selectbox(usage_lbl, usage_opts, index=idx_use)

        width_lbl = "عرض الأرض / الواجهة (متر):" if lang == "AR" else "Land Width / Frontage (meters):"
        st.session_state["land_width"] = st.number_input(width_lbl, min_value=0.0, max_value=500.0, value=st.session_state["land_width"], step=0.5)

        sector_num_lbl = "رقم المقاطعة والبلدية للعقار:" if lang == "AR" else "District / Sector Number:"
        sector_num_val = st.text_input(sector_num_lbl, value="", placeholder="مثال: 42 مكة", key="sector_num")

    with col_f3:
        street_lbl = "عرض الشارع المقابل للعقار (m):" if lang == "AR" else "Opposite Street Width (m):"
        street_width = st.number_input(street_lbl, min_value=0.0, max_value=100.0, value=0.0, step=0.5)

        length_lbl = "طول الأرض / النزال (متر):" if lang == "AR" else "Land Length / Depth (meters):"
        st.session_state["land_length"] = st.number_input(length_lbl, min_value=0.0, max_value=500.0, value=st.session_state["land_length"], step=0.5)

        corner_lbl = "موضع قطعة الأرض وتصنيفها:" if lang == "AR" else "Plot Orientation Class:"
        corner_opts = ["", "عادي / وسطي", "ركن / زاوية"] if lang == "AR" else ["", "Standard / Middle", "Corner Plot"]
        idx_crn = corner_opts.index(st.session_state["selected_corner"]) if st.session_state["selected_corner"] in corner_opts else 0
        st.session_state["selected_corner"] = st.selectbox(corner_lbl, corner_opts, index=idx_crn)

    col_sub_f1, col_sub_f2 = st.columns(2)
    with col_sub_f1:
        basement_lbl = "هل يتضمن المخطط طابق سرداب (Basement)؟" if lang == "AR" else "Does it include a Basement floor?"
        basement_opts = ["", "موجود", "غير موجود"] if lang == "AR" else ["", "Present", "Not Present"]
        idx_bsm = basement_opts.index(st.session_state["has_basement_sel"]) if st.session_state["has_basement_sel"] in basement_opts else 0
        st.session_state["has_basement_sel"] = st.selectbox(basement_lbl, basement_opts, index=idx_bsm)
        has_basement = True if st.session_state["has_basement_sel"] in ["موجود", "Present"] else False

    with col_sub_f2:
        floors_lbl = "عدد طوابق المبنى المقترحة فوق مستوى الأرض:" if lang == "AR" else "Proposed Floors Above Ground:"
        st.session_state["building_floors"] = st.number_input(floors_lbl, min_value=0, max_value=60, value=st.session_state["building_floors"])

    user_area = st.session_state["land_width"] * st.session_state["land_length"]
    building_floors = st.session_state["building_floors"]
    selected_gov = st.session_state["selected_gov"]

    if building_floors > 0:
        if building_floors >= 4 or has_basement:
            structural_class_txt = "🏢 منشأ ثقيل / أحمال حرجة عالية" if lang == "AR" else "🏢 Heavy Structure / High Load Class"
            structural_class_clr = "#DC2626"
            is_heavy_structure = True
        else:
            structural_class_txt = "🏡 منشأ خفيف / أحمال اعتيادية منخفضة" if lang == "AR" else "🏡 Light Structure / Normal Load Class"
            structural_class_clr = "#10B981"
            is_heavy_structure = False
            
        area_msg = f"المساحة الكلية المستنتجة: {user_area:.1f} m²"
        st.markdown(f"""
        <div style="background-color: #F8FAFC; padding: 10px; border-radius: 8px; border-right: 4px solid {structural_class_clr}; border-left: 4px solid {structural_class_clr if lang == 'AR' else 'transparent'}; margin-top: 5px; text-align: {align};">
            <b style="color: {structural_class_clr}; font-size: 0.85rem;">{structural_class_txt} | {area_msg}</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; color: #D1D5DB; margin: -12px 0; font-size: 1.1rem;'>│</div>", unsafe_allow_html=True)

    # --- 🔬 الخطوة 2: فحص التربة والأسس الجيوتقنية المعملية (المقيدة بحالة الخطوة 1) ---
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
    else:
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
        
        # طباعة شجرة الفحوصات المستنتجة كودياً
        st.markdown(f"<div class='compliance-card' style='background-color: #FAFAFA; border: 1px dashed #CBD5E1; padding:12px; margin-bottom:12px;'>", unsafe_allow_html=True)
        st.markdown(f"<b>📋 {'الفحوصات والاشتراطات الإلزامية المقرة لهذا المشروع كودياً:' if lang == 'AR' else 'Mandatory Code Requirements For This Project:'}</b>", unsafe_allow_html=True)
        
        if is_heavy_structure:
            bh_text = "• مطلوب 3 حفر اختبارية (Boreholes) كحد أدنى بعمق لا يقل عن 15 متراً لتأمين حسابات السرداب والأحمال الثقيلة." if lang == "AR" else "• Min 3 Boreholes required with depth >= 15m for basement/heavy loads."
        else:
            if user_area <= 400:
                bh_text = "• مطلوب حفرتان اختباريتان فقط (Boreholes) بعمق لا يقل عن 6 أمتار بموجب مساحة الأرض المستنتجة (الجدول 2-1)." if lang == "AR" else "• 2 Boreholes required with depth >= 6m based on land area."
            else:
                bh_text = "• مطلوب 3 حفر اختبارية كحد أدنى بعمق لا يقل عن 6 أمتار لتجاوز مساحة الأرض 400 م²." if lang == "AR" else "• Min 3 Boreholes required with depth >= 6m due to area > 400m²."
        st.markdown(f"<div style='color:#1E40AF; font-size:0.82rem; margin-top:4px;'>{bh_text}</div>", unsafe_allow_html=True)
        
        if has_basement:
            h2o_text = "• ⚠️ شرط حرج: يتوجب تدقيق منسوب المياه الجوفية الحركي الميداني وإجراء فحص التحليل الكيميائي لعدوانية المياه الجوفية." if lang == "AR" else "• ⚠️ Critical: Groundwater level measurement & chemical aggressiveness tests are mandatory."
            st.markdown(f"<div style='color:#DC2626; font-size:0.82rem; margin-top:2px;'>{h2o_text}</div>", unsafe_allow_html=True)
            
        if selected_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
            gyp_txt = f"• قيد جيوكيميائي: يقع الموقع ضمن نطاق التربة الجبسية، مطلوب فحص الجبس الكلي والانهيارية تحت النقع المستمر." if lang == "AR" else "• Gypseous Soil zone: Gypsum content & collapsible soil tests are mandatory."
            st.markdown(f"<div style='color:#B45309; font-size:0.82rem; margin-top:2px;'>{gyp_txt}</div>", unsafe_allow_html=True)
            
        if selected_gov in ["Najaf", "Muthanna"]:
            void_txt = "• قيد جيولوجي خاص: مطلوب إرفاق فحص المسح الراداري الأرضي (GPR Void Scan) لضمان خلو الموقع من التكهفات الكلسية." if lang == "AR" else "• Geological Zone: GPR Void Scan is mandatory to rule out limestone cavities."
            st.markdown(f"<div style='color:#701A75; font-size:0.82rem; margin-top:2px;'>{void_txt}</div>", unsafe_allow_html=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(L['file_uploader_lbl'], type=["pdf"])
        sub_col1, sub_col2, sub_col3 = st.columns(3)
        with sub_col1:
            bearing_cap = st.number_input(L['input_bearing'], min_value=10, max_value=500, value=120)
            gypsum = st.number_input(L['input_gypsum'], min_value=0.0, max_value=100.0, value=4.50) if selected_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"] else 1.0
        with sub_col2:
            actual_bh_depth_lbl = "أقصى عمق للحفرة ميدانياً (متر):" if lang == "AR" else "Max Borehole Depth (m):"
            actual_bh_depth = st.number_input(actual_bh_depth_lbl, min_value=0.0, max_value=120.0, value=6.0, step=0.5)
            report_status_sel = st.selectbox(L['input_auth'], [L['auth_yes'], L['auth_no']])
            report_status = "معتمد ومجاز ومصادق" if report_status_sel == L['auth_yes'] else "غير مصادق"
        with sub_col3:
            if has_basement:
                water_table_lbl = "منسوب المياه الجوفية المقاس (متر):" if lang == "AR" else "Water Table (m):"
                water_table = st.number_input(water_table_lbl, min_value=0.0, max_value=50.0, value=1.5, step=0.1)
                water_chem_lbl = "فحص عدوانية المياه الجوفية:" if lang == "AR" else "Water Aggressiveness:"
                w_opts = ["مطابق وضمن الحدود الآمنة", "عدواني جداً"] if lang == "AR" else ["Compliant", "Highly Aggressive"]
                water_chem_status = st.selectbox(water_chem_lbl, w_opts)
            else:
                water_table, water_chem_status = 20.0, "مطابق وضمن الحدود الآمنة"
            
        if st.button(L['run_audit'], type="primary", use_container_width=True):
            try:
                from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
                excel_engine = IraqiDynamicComplianceEngine(excel_filename="soil_testing.xlsx")
                payload = {
                    "governorate": selected_gov, "total_land_area_m2": user_area, "soil_bearing_capacity": bearing_cap,
                    "soil_report_status": report_status, "actual_gypsum_percentage": gypsum, "is_heavy_structure": is_heavy_structure,
                    "actual_borehole_depth_meters": actual_bh_depth, "lot_num": lot_num_val, "sector_num": sector_num_val,
                    "building_floors": building_floors, "water_table_meters": water_table, "water_chemical_status": water_chem_status
                }
                soil_result = excel_engine.validate_soil_report(payload)
                st.markdown(L['soil_report_header'])
                if soil_result["status"] == "PASSED":
                    st.success(soil_result["summary"])
                    st.session_state["compliance_rate"], st.session_state["step2_status"] = 68, "Completed"
                    st.rerun()
                else:
                    st.error(soil_result["summary"])
                    pdf_path = excel_engine.generate_pdf_report(payload, soil_result, "Soil_Compliance_Failures.pdf")
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="📥 تحميل تقرير المخالفات والرفض الرسمي (PDF)", data=f, file_name="Soil_Compliance_Failures.pdf", mime="application/pdf", use_container_width=True)
                    for idx, failure in enumerate(soil_result["failures"], 1):
                        st.markdown(f"<div class='compliance-card'>### ⚠️ المخالفة {idx}: **{failure['title']}**<br><small>{failure['severity']}</small><br>💬 {failure['citizen_exp']}<br>🔧 {failure['engineer_exp']}<br>✅ {failure['resolution']}<br>🚨 {failure['legal_penalty']}</div>", unsafe_allow_html=True)
            except Exception as e: st.error(f"حدث خطأ في المعالجة: {str(e)}")
        st.markdown("</div></div>", unsafe_allow_html=True)

    st.markdown(f"<div style='text-align: center; color: #D1D5DB; margin: -12px 0; font-size: 1.1rem;'>│</div>", unsafe_allow_html=True)
    for step_num, step_title in [("3", L['step3_title']), ("4", L['step4_title']), ("5", L['step5_title'])]:
        with st.container(border=True):
            c1, c2, c3 = st.columns([0.15, 1.0, 0.4])
            with c1: st.markdown("<div>🔒</div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div style='font-weight: bold; font-size: 0.92rem; color: #9CA3AF; text-align: {align};'>{step_title}</div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div style='text-align: right; color: #9CA3AF; font-weight: bold; font-size: 0.82rem;'>{L['locked']}</div>", unsafe_allow_html=True)

    st.markdown(f"<br><div dir='{direction}' style='background-color: #0F172A; color: white; padding: 18px; border-radius: 14px; text-align: {align}; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'><div style='font-weight: bold; font-size: 1rem; margin-bottom: 4px; color: #F59E0B;'>{L['premium_title']}</div><div style='font-size: 0.78rem; color: #94A3B8;'>{L['premium_desc']}</div></div>", unsafe_allow_html=True)
