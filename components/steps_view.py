# components/steps_view.py
import streamlit as st

def render_steps_and_calculators(L, lang):
    """رسم وإعادة بناء بوابات التدقيق المتسلسلة والمقفلة بأكواد ويب صافية ومضمونة 100%"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"

    # 1. تصميم شريط الخطوات المتتالية والأقفال الاحترافي المطابق للصورة بالملي عبر HTML/CSS
    steps_html = f"""
    <div dir="{direction}" style="display: flex; gap: 10px; justify-content: space-between; margin-bottom: 25px; text-align: {align}; flex-wrap: wrap;">
        <!-- الخطوة 1 المكتملة -->
        <div style="background-color: white; border: 1px solid #E2E8F0; padding: 10px 14px; border-radius: 12px; display: flex; align-items: center; gap: 8px; flex: 1; min-width: 140px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <span style="background-color: #10B981; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; font-family: sans-serif;">✓</span>
            <div style="font-size: 11px; font-weight: bold; color: #1E293B;">{'الخطوة 1: المحددات' if lang=='AR' else 'Step 1: Zoning'}</div>
        </div>
        
        <!-- الخطوة 2 الجارية -->
        <div style="background-color: #FFF7ED; border: 1px solid #FFEDD5; padding: 10px 14px; border-radius: 12px; display: flex; align-items: center; gap: 8px; flex: 1; min-width: 140px; box-shadow: 0 1px 3px rgba(0,0,0,0.02);">
            <span style="background-color: #F97316; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; font-family: sans-serif;">2</span>
            <div style="font-size: 11px; font-weight: bold; color: #9A3412;">{'الخطوة 2: فحص التربة' if lang=='AR' else 'Step 2: Soil Audit'}</div>
        </div>

        <!-- الخطوة 3 المقفلة -->
        <div style="background-color: #F8FAFC; border: 1px dashed #CBD5E1; padding: 10px 14px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; flex: 1; min-width: 140px; opacity: 0.75;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background-color: #94A3B8; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; font-family: sans-serif;">3</span>
                <div style="font-size: 11px; font-weight: bold; color: #64748B;">{'الخطوة 3: الإنشائي' if lang=='AR' else 'Step 3: Structural'}</div>
            </div>
            <span style="font-size: 12px;">🔒</span>
        </div>

        <!-- الخطوة 4 المقفلة -->
        <div style="background-color: #F8FAFC; border: 1px dashed #CBD5E1; padding: 10px 14px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; flex: 1; min-width: 140px; opacity: 0.75;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background-color: #94A3B8; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; font-family: sans-serif;">4</span>
                <div style="font-size: 11px; font-weight: bold; color: #64748B;">{'الخطوة 4: الصحي' if lang=='AR' else 'Step 4: Sanitary'}</div>
            </div>
            <span style="font-size: 12px;">🔒</span>
        </div>

        <!-- الخطوة 5 المقفلة -->
        <div style="background-color: #F8FAFC; border: 1px dashed #CBD5E1; padding: 10px 14px; border-radius: 12px; display: flex; align-items: center; justify-content: space-between; flex: 1; min-width: 140px; opacity: 0.75;">
            <div style="display: flex; align-items: center; gap: 8px;">
                <span style="background-color: #94A3B8; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; font-family: sans-serif;">5</span>
                <div style="font-size: 11px; font-weight: bold; color: #64748B;">{'الخطوة 5: الكهربائي' if lang=='AR' else 'Step 5: Electrical'}</div>
            </div>
            <span style="font-size: 12px;">🔒</span>
        </div>
    </div>
    """
    st.markdown(steps_html, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
    
    # 2. حقول الإدخال والمقاييس لـ (الخطوة 1) كما هي مخزنة داخل حاويتك الأصلية
    with st.container(border=True):
        st.markdown(f"<div style='text-align: {align}; font-weight: bold; color: #1E293B; margin-bottom: 12px;'>📋 معطيات الموقع والمحددات الحالية:</div>", unsafe_allow_html=True)

           # حقول الإدخال الهندسية مقسمة بالتناظر على 3 أعمدة
        col1, col2, col3 = st.columns(3)
        with col1:
            gov_opts = {"": "اختر المحافظة...", "بغداد": "Baghdad", "صلاح الدين": "Salah_Al_Din", "الأنبار": "Anbar", "النجف الأشرف": "Najaf", "نينوى": "Nineveh", "البصرة": "Basra"} if lang == "AR" else {"": "Select Governorate...", "Baghdad": "Baghdad", "Salah_Al_Din": "Salah_Al_Din", "Anbar": "Anbar", "Najaf": "Najaf", "Nineveh": "Nineveh", "Basra": "Basra"}
            f_gov = gov_opts[st.selectbox("المحافظة" if lang == "AR" else "Governorate", list(gov_opts.keys()), key="w_gov")]
            
            req_opts = ["", "بناء جديد", "إعادة تأهيل", "ترميم", "إضافة طابق", "مشاريع كبرى"] if lang == "AR" else ["", "New Construction", "Reconstruction", "Floor Addition", "Renovation", "Major Projects"]
            f_req = st.selectbox("نوع الطلب / المعاملة" if lang == "AR" else "Request Type", req_opts, key="w_req")
            f_plot = st.text_input("رقم قطعة العقار (المرقم)" if lang == "AR" else "Plot Number", key="w_lot", placeholder="1024/5")
            
        with col2:
            usage_opts = ["", "سكني", "تجاري", "خدمي", "صناعي", "مجمعات"] if lang == "AR" else ["", "Residential", "Commercial", "Service", "Industrial", "Complexes"]
            f_usage = st.selectbox("الاستعمال المخطط الأساسي" if lang == "AR" else "Primary Usage", usage_opts, key="w_usage")
            f_width = st.number_input("عرض الواجهة (متر)" if lang == "AR" else "Frontage Width (m)", min_value=0.0, step=0.5, key="w_width")
            f_sec = st.text_input("رقم المقاطعة والبلدية" if lang == "AR" else "District Number", key="w_sec", placeholder="42")
            
        with col3:
            f_street = st.number_input("عرض الشارع المقابل (متر)" if lang == "AR" else "Street Width (m)", min_value=0.0, step=0.5, key="w_street")
            f_length = f_length = st.number_input("طول الأرض / النزال (متر)" if lang == "AR" else "Land Length (m)", min_value=0.0, step=0.5, key="w_length")
            base_opts = ["", "موجود", "غير موجود"] if lang == "AR" else ["", "Present", "Not Present"]
            f_base = st.selectbox("هل يوجد طابق سرداب؟" if lang == "AR" else "Basement?", base_opts, key="w_base")

        f_floors = st.number_input("عدد الطوابق فوق الأرض" if lang == "AR" else "Floors Above Ground", min_value=0, max_value=60, key="w_floors")
        dir_opts = ["", "شمالي", "جنوبي", "شرقي", "غربي", "شمالي شرقي", "شمالي غربي", "جنوبي شرقي", "جنوبي غربي"] if lang == "AR" else ["", "North", "South", "East", "West", "North-East", "North-West", "South-East", "South-West"]
        st.selectbox("اتجاه واجهة المبنى الجغرافية" if lang == "AR" else "Frontage Orientation", dir_opts, key="w_orient")

        
        # حسابات المساحة الكلية وتصنيف الأحمال الإنشائية
        calculated_area = f_width * f_length
        is_heavy = f_floors >= 4 or f_base == "موجود" or f_base == "Present"
        
        if f_floors > 0:
            st_class = "منشأ ثقيل / أحمال مركبة 🏢" if is_heavy else "منشأ خفيف / أحمال اعتيادية 🏡"
            st_clr = "#DC2626" if is_heavy else "#10B981"
            st.markdown(f"""
            <div dir="{direction}" style="background-color: #F8FAFC; padding: 12px; border-radius: 10px; border-right: 4px solid {st_clr}; border-left: 4px solid {st_clr}; margin-top: 15px; text-align: {align};">
                <b style="color: {st_clr}; font-size: 0.92rem;">🔍 استنتاج النظام الهندسي الحالي:</b> المساحة المحسوبة: {calculated_area:.1f} م² | تصنيف المنشأ: {st_class}
            </div>
            """, unsafe_allow_html=True)
            # توليد شجرة التوصيات والمحددات البلدية المؤتمتة بناءً على المعطيات
            with st.expander("📋 عرض تفاصيل محددات فحص ومسح التربة الإلزامية للموقع", expanded=True):
                if is_heavy:
                    st.markdown("🔹 **مطلوب 3 حفر اختبارية** كحد أدنى بعمق لا يقل عن 15 متراً (Boreholes) لحساب استقرارية المنشأ الثقيل.")
                    st.markdown("🔹 **إلزامي فحص مسح التربة الماسي للمستودعات والديناميكي (Triaxial Shear)** للمنشآت الكبرى.")
                else:
                    bh_count = 2 if calculated_area <= 400 else 3
                    st.markdown(f"🔹 **مطلوب {bh_count} حفر اختبارية** بعمق لا يقل عن 6 أمتار بموجب المدونة العراقية الموحدة.")
                
                if f_base in ["موجود", "Present"]:
                    st.markdown("🔹 **فحص المياه الجوفية الكيميائي إلزامي:** للكشف عن نسب الكبريتات والأملاح لحماية الأسس تحت الأرض.")
                if f_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
                    st.markdown("⚠️ **متطلب كودي حرج للمحافظة:** إلزامي فحص الانهيارية والجبس المتفخ (Leaching & Collapse Test) لتربة هذه المناطق.")
                elif f_gov in ["Basra", "Dhi_Qar", "Maysan", "Muthanna"]:
                    st.markdown("🔹 **تحذير التربة الرخوة والملوحة العالية:** إلزامي تحديد صنف السمنت المقاوم للأملاح (صنف 503) للأسس.")
                if f_gov in ["Najaf", "Muthanna"]:
                    st.markdown("🔹 **فحص المسح الراداري للموقع (GPR Void Scan):** للكشف عن الفجوات والكهوف المغلقة تحت السطحية.")

    # ==================== 🟠 الخطوة 2: فحص التربة والأسس الجاري تدقيقها حياً ====================
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    with st.container(border=True):
        # حقن شارة قيد التدقيق البرتقالية المستديرة العائمة لتطابق التصميم المرجو تماماً
        st.markdown(f"""
        <div dir="{direction}" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; text-align: {align};">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="background-color: #F97316; color: white; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold; font-family: sans-serif;">2</span>
                <b style="color: #1E293B; font-size: 1rem;">{L['step2_title']}</b>
            </div>
            <span style="background-color: #FFEDD5; color: #9A3412; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; border: 1px solid #FED7AA;">
                ⏳ {"قيد التدقيق" if lang == "AR" else "In Progress"}
            </span>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(L['file_uploader_lbl'], type=["pdf"], key="w_soil_pdf")
        
        sub_c1, sub_c2 = st.columns(2)
        with sub_c1:
            bearing_cap = st.number_input(L['input_bearing'], min_value=10, max_value=500, value=120, key="w_soil_bearing")
            if f_floors > 0 and f_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
                gypsum = st.number_input(L['input_gypsum'], min_value=0.0, max_value=100.0, value=4.50, key="w_soil_gypsum")
            else:
                gypsum = 1.0
                
        with sub_c2:
            actual_bh_depth = st.number_input("أقصى عمق واصلة له الحفرة الاختبارية ميدانياً (متر):" if lang == "AR" else "Maximum Actual Borehole Depth (m):", min_value=0.0, max_value=120.0, value=6.0, step=0.5, key="w_soil_depth")
            report_status_sel = st.selectbox(L['input_auth'], [L['auth_yes'], L['auth_no']], key="w_soil_auth")
            report_status = "معتمد ومصادق" if report_status_sel == L['auth_yes'] else "غير مصدق"
        # زر التدقيق والامتثال المركزي المطور
        if st.button(L['run_audit'], type="primary", use_container_width=True, key="w_btn_audit"):
            if not f_gov or f_req == "" or f_usage == "" or f_width == 0 or f_length == 0 or f_floors == 0 or f_base == "":
                st.error("⚠️ يرجى ملء كافة محددات ومقاييس الخطوة الأولى الافتتاحية والموقع وتحديد الأبعاد أولاً.")
            else:
                try:
                    from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
                    excel_engine = IraqiDynamicComplianceEngine(excel_filename="data/soil_testing.xlsx")
                    
                    payload = {
                        "governorate": f_gov, "total_land_area_m2": calculated_area,
                        "soil_bearing_capacity": bearing_cap, "report_status": report_status,
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
                            st.markdown(f"❌ **المخالفة رقم ({idx}):** {failure['title']}")
                            st.markdown(f"""
                            <div style="background-color: #FEF2F2; padding: 10px; border-radius: 8px; border-right: 4px solid #DC2626; margin-bottom: 8px; text-align: {align};">
                                <span style="color:#DC2626; font-weight:bold;">مستوى الحرج:</span> {failure['severity']}<br>
                                <span style="color:#4B5563; font-weight:bold;">الشرح الفني للمهندس:</span> {failure['engineer_exp']}<br>
                                <span style="color:#2563EB; font-weight:bold;">🛠️ المسار الإصلاحي:</span> {failure['resolution']}<br>
                                <span style="color:#D97706; font-weight:bold;">⚖️ الأثر والعقوبة البلدية:</span> {failure['legal_penalty']}
                            </div>
                            """, unsafe_allow_html=True)
                            st.divider()
                except Exception as e:
                    st.error(f"حدث خطأ في معالجة البيانات: {str(e)}")

    # ==================== 🔒 الخطوات المتسلسلة والمقفلة بحماية برمجية وبصرية ====================
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    
    locked_steps = [
        ("3", "Step 3: Structural Audit & Load Calculations" if lang == "EN" else "الخطوة 3: التدقيق الإنشائي وحسابات الأحمال الموحدة"),
        ("4", "Step 4: Hydro-Sanitary & Plumbing Design" if lang == "EN" else "الخطوة 4: التصاميم الهيدروليكية والشبكات الصحية البيئية"),
        ("5", "Step 5: Electrical Systems Analysis" if lang == "EN" else "الخطوة 5: المنظومات الكهربائية وكفاءة الطاقة المتجددة")
    ]
    
    for num, title in locked_steps:
        st.markdown(f"""
        <div dir="{direction}" style="background-color: #F8FAFC; padding: 14px; border-radius: 14px; border: 1px dashed #CBD5E1; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; text-align: {align}; opacity: 0.75;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="background-color: #94A3B8; color: white; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold; font-family: sans-serif;">{num}</span>
                <span style="color: #64748B; font-weight: 600; font-size: 0.92rem;">{title}</span>
            </div>
            <span style="font-size: 1.1rem; color: #94A3B8;">🔒</span>
        </div>
        """, unsafe_allow_html=True)

    # ------------------ باقة الترقية المتميزة الموحدة بأفل الشاشة ------------------
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div dir="{direction}" style="background-color: #0F172A; color: white; padding: 22px; border-radius: 16px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); text-align: {align}; position: relative; overflow: hidden; border: 1px solid #1E293B;">
        <div style="position: absolute; top: -10px; right: -10px; background-color: #3B82F6; opacity: 0.1; width: 100px; height: 100px; border-radius: 50%;"></div>
        <div style="font-weight: 700; font-size: 1.15rem; color: #F59E0B; margin-bottom: 6px;">✨ {L['premium_title']}</div>
        <div style="font-size: 0.88rem; color: #E2E8F0; line-height: 20px; max-width: 85%;">
            {L['premium_desc']}
        </div>
        <div style="margin-top: 12px; font-size: 0.75rem; color: #94A3B8;">
            🔒 فتح كافة الحاسبات الـ 14 المؤتمتة للامتثال البيئي العراقي ومحركات التحقق الخلفية حياً.
        </div>
    </div>
    """, unsafe_allow_html=True)
