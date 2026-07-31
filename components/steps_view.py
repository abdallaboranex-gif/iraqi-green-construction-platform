# components/steps_view.py
import streamlit as st

def render_steps_and_calculators(L, lang):
    """رسم وإدارة بوابات التدقيق والمطابقة الكودية بالتفكيك الهندسي النظيف"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    
    # 1. شريط المرحلة العلوي
    st.markdown(f"""
    <div dir="{direction}" style="margin-bottom: 20px; text-align: {align};">
        <span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: bold;">{L['phase']}</span> 
        <span style="font-weight: bold; font-size: 1.1rem; color: #1F2937; margin: 0 10px;">{L['eng_comp']}</span> 
        <span style="font-size: 0.85rem; color: #6B7280;">{L['seq_order']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. الخطوة 1: بوابة المحددات البلدية الـ 13 المصفّرة
    with st.container(border=True):
        st.markdown(f"#### 🏢 {L['step1_title']}")
        st.markdown(f'<div dir="{direction}" style="text-align: {align};">', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            gov_opts = {"اختر المحافظة...": "", "بغداد": "Baghdad", "صلاح الدين": "Salah_Al_Din", "الأنبار": "Anbar", "النجف الأشرف": "Najaf", "نينوى": "Nineveh", "البصرة": "Basra"} if lang == "AR" else {"Select Governorate...": "", "Baghdad": "Baghdad", "Salah Al-Din": "Salah_Al_Din", "Anbar": "Anbar", "Najaf": "Najaf", "Nineveh": "Nineveh", "Basra": "Basra"}
            f_gov = gov_opts[st.selectbox("المحافظة ونطاق المشروع:" if lang == "AR" else "Governorate:", list(gov_opts.keys()), key="w_gov")]
            
            req_opts = ["", "بناء جديد", "إعادة بناء", "إضافة طابق", "ترميم", "مشاريع كبرى"] if lang == "AR" else ["", "New Construction", "Reconstruction", "Floor Addition", "Renovation", "Major Projects"]
            f_req = st.selectbox("نوع الطلب / المعاملة:" if lang == "AR" else "Request Type:", req_opts, key="w_req")
            st.text_input("رقم قطعة العقار (الطابو):" if lang == "AR" else "Plot Number:", key="w_lot", placeholder="1024/5")

        with col2:
            usage_opts = ["", "سكني", "تجاري", "خدمي", "صناعي", "مجمعات"] if lang == "AR" else ["", "Residential", "Commercial", "Service", "Industrial", "Complexes"]
            f_usage = st.selectbox("استعمال العقار الأساسي:" if lang == "AR" else "Primary Usage:", usage_opts, key="w_usage")
            f_width = st.number_input("عرض الواجهة (متر):" if lang == "AR" else "Frontage Width (m):", min_value=0.0, step=0.5, key="w_width")
            st.text_input("رقم المقاطعة والبلدية:" if lang == "AR" else "District Number:", key="w_sec", placeholder="42 مكة")

        with col3:
            f_street = st.number_input("عرض الشارع المقابل (m):" if lang == "AR" else "Street Width (m):", min_value=0.0, step=0.5, key="w_street")
            f_length = st.number_input("طول الأرض / النزال (متر):" if lang == "AR" else "Land Length (m):", min_value=0.0, step=0.5, key="w_length")
            base_opts = ["", "موجود", "غير موجود"] if lang == "AR" else ["", "Present", "Not Present"]
            f_base = st.selectbox("هل يوجد طابق سرداب؟" if lang == "AR" else "Basement?", base_opts, key="w_base")
            
        f_floors = st.number_input("عدد الطوابق فوق الأرض:" if lang == "AR" else "Floors Above Ground:", min_value=0, max_value=60, key="w_floors")
        
        # حقل الاتجاه الجغرافي (المحدد رقم 13)
        dir_opts = ["", "شمالي", "جنوبي", "شرقي", "غربي", "شمالي شرقي", "شمالي غربي", "جنوبي شرقي", "جنوبي غربي"] if lang == "AR" else ["", "North", "South", "East", "West", "North-East", "North-West", "South-East", "South-West"]
        st.selectbox("اتجاه واجهة المبنى الجغرافية:" if lang == "AR" else "Frontage Orientation:", dir_opts, key="w_orient")
        st.markdown("</div>", unsafe_allow_html=True)
        # 3. محرك الاستنتاج الذكي للمساحة وثقل المنشأ وتوليد شجرة الفحوصات
        calculated_area = f_width * f_length
        is_heavy = f_floors >= 4 or f_base == "موجود"
        
        if f_floors > 0:
            st_class = "🏢 منشأ ثقيل / أحمال حرجية" if is_heavy else "🏡 منشأ خفيف / أحمال اعتيادية"
            st_clr = "#DC2626" if is_heavy else "#10B981"
            
            st.markdown(f"""
            <div style="background-color: #F8FAFC; padding: 12px; border-radius: 8px; border-right: 4px solid {st_clr}; margin: 15px 0;">
                <b style="color: {st_clr}; font-size: 0.95rem;">🧠 استنتاج عقل النظام: {st_class} | المساحة: {calculated_area:.1f} م²</b>
            </div>
            """, unsafe_allow_html=True)
            
            # 📋 توليد شجرة الفحوصات المطلوبة تلقائياً بناءً على محددات الفلترة
            st.markdown("##### 📋 الفحوصات والوثائق الإلزامية المطلوبة كودياً لهذا المشروع:")
            with st.expander("عرض تفاصيل دليل الفحص الجيوتقني الحاكم للموقع", expanded=True):
                if is_heavy:
                    st.markdown("• **حفر الموقع (Boreholes):** مطلوب **3 حفر اختبارية كحد أدنى بعمق لا يقل عن 15 متراً**.")
                    st.markdown("• **فحص القص ثلاثي المحاور (Triaxial Shear):** إلزامي لحساب ضغط التربة الجانبي للسرداب.")
                else:
                    bh_count = 2 if calculated_area <= 400 else 3
                    st.markdown(f"• **حفر الموقع (Boreholes):** مطلوب **{bh_count} حفر اختبارية بعمق لا يقل عن 6 أمتار** بموجب الجدول 2-1.")
                
                if f_base == "موجود":
                    st.markdown("• **💧 فحص المياه الجوفية الميداني:** إلزامي نظراً لوجود سرداب لتحديد منسوب المياه السطحية بدقة.")
                    st.markdown("• **التحليل الكيميائي لعدوانية المياه:** فحص نسب الكبريتات والكلوريدات لحماية جدران السرداب.")
                
                if f_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
                    st.markdown("• **🚨 فحص الجبس الكلي (Leaching & Collapse Test):** مطلب كودي صارم للتحقق من انهيارية التربة.")
                elif f_gov in ["Basra", "Dhi_Qar", "Maysan", "Muthanna", "Baghdad"]:
                    st.markdown("• **فحص محتوى الكبريتات الكلية (SO3):** إلزامي لتحديد صنف السمنت المقاوم للأسس.")
                    
                if f_gov in ["Najaf", "Muthanna"]:
                    st.markdown("• **🔒 فحص المسح الراداري (GPR Void Scan):** مطلب بلدية خاص للكشف عن الفجوات الكلسية التكهفية.")
    # =========================================================================
    # --- 🔬 الخطوة 2: نتائج الفحوصات المختبرية لتقرير التربة (مرتبطة بالإكسل) ---
    # =========================================================================
    st.markdown("<div style='text-align: center; color: #D1D5DB; margin: 10px 0;'>│</div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown(f"#### 🔬 {L['step2_title']}")
        st.markdown(f'<div dir="{direction}" style="text-align: {align};">', unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(L['file_uploader_lbl'], type=["pdf"], key="w_soil_pdf")
        
        sub_c1, sub_c2 = st.columns(2)
        with sub_c1:
            bearing_cap = st.number_input(L['input_bearing'], min_value=10, max_value=500, value=120, key="w_soil_bearing")
            # حقل الجبس المشروط جغرافياً
            if f_floors > 0 and f_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
                gypsum = st.number_input(L['input_gypsum'], min_value=0.0, max_value=100.0, value=4.50, key="w_soil_gypsum")
            else:
                gypsum = 1.0
                
        with sub_c2:
            actual_bh_depth = st.number_input("أقصى عمق واصلة له الحفرة الاختبارية ميدانياً (متر):" if lang == "AR" else "Maximum Actual Borehole Depth (m):", min_value=0.0, max_value=120.0, value=6.0, step=0.5, key="w_soil_depth")
            report_status_sel = st.selectbox(L['input_auth'], [L['auth_yes'], L['auth_no']], key="w_soil_auth")
            report_status = "معتمد ومجاز ومصادق" if report_status_sel == L['auth_yes'] else "غير مصادق"
            
        # زر الفحص الكودي المباشر من ملف الإكسل
        if st.button(L['run_audit'], type="primary", use_container_width=True, key="w_btn_audit"):
            if not f_gov or f_req == "" or f_usage == "" or f_width == 0 or f_length == 0 or f_floors == 0 or f_base == "":
                st.error("⚠️ يرجى ملء كافة محددات ومقاييس الخطوة الأولى الافتتاحية والموقع وتحديد الأبعاد أولاً.")
            else:
                try:
                    from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
                    excel_engine = IraqiDynamicComplianceEngine(excel_filename="soil_testing.xlsx")
                    
                    payload = {
                        "governorate": f_gov, "total_land_area_m2": calculated_area,
                        "soil_bearing_capacity": bearing_cap, "soil_report_status": report_status, 
                        "actual_gypsum_percentage": gypsum, "is_heavy_structure": is_heavy,
                        "actual_borehole_depth_meters": actual_bh_depth
                    }
                    
                    soil_result = excel_engine.validate_soil_report(payload)
                    st.markdown(L['soil_report_header'])
                    
                    if soil_result["status"] == "PASSED":
                        st.success(soil_result["summary"])
                        st.session_state["compliance_rate"] = 68
                        st.session_state["step2_status"] = "Completed"
                        st.rerun()
                    else:
                        st.error(soil_result["summary"])
                        for idx, failure in enumerate(soil_result["failures"], 1):
                            st.markdown(f"### ⚠️ المخالفة رقم {idx}:")
                            st.markdown(f"<div style='background-color:#FEF2F2; padding:8px; border-right:4px solid #DC2626; margin-bottom:5px; font-weight:bold;'>{failure['severity']}</div>", unsafe_allow_html=True)
                            st.markdown(f"**{failure['title']}**")
                            st.info(failure['citizen_exp'])
                            st.warning(failure['engineer_exp'])
                            st.success(failure['resolution'])
                            st.markdown(f"<div style='color:#991B1B; background-color:#FEE2E2; padding:8px; border-radius:4px;'><b>🚨 الأثر والعقوبة البلدية:</b> {failure['legal_penalty']}</div>", unsafe_allow_html=True)
                            st.divider()
                except Exception as e:
                    st.error(f"حدث خطأ في معالجة البيانات: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================================
    # --- 🔒 الخطوات المغلقة المتسلسلة (Step 3, 4, 5) الانتظارية بقفل إلكتروني ---
    # =========================================================================
    steps_data = [("3", L['step3_title']), ("4", L['step4_title']), ("5", L['step5_title'])]
    for step_num, step_title in steps_data:
        st.markdown("<div style='text-align: center; color: #D1D5DB; margin: 5px 0;'>│</div>", unsafe_allow_html=True)
        with st.container(border=True):
            c_s1, c_s2, c_s3 = st.columns([0.1, 1.0, 0.4])
            with c_s1: st.markdown("<div>🔒</div>", unsafe_allow_html=True)
            with c_s2: st.markdown(f"<div style='font-weight: bold; font-size: 0.95rem; color: #9CA3AF; text-align: {align};'>{step_title}</div>", unsafe_allow_html=True)
            with c_s3: st.markdown(f"<div style='text-align: right; color: #9CA3AF; font-weight: bold; font-size: 0.85rem;'>{L['locked']}</div>", unsafe_allow_html=True)

    # بنر الباقة المهنية المدفوعة
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div dir="{direction}" style="background-color: #0F172A; color: white; padding: 20px; border-radius: 12px; text-align: {align}; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 1.05rem; margin-bottom: 4px; color: #F59E0B;">{L['premium_title']}</div>
        <div style="font-size: 0.8rem; color: #94A3B8;">{L['premium_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
