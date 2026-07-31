# components/steps_view.py
import streamlit as st

def render_steps_and_calculators(L, lang):
    """رسم وإدارة شجرة الخطوات وبوابة الفلترة البلدية الافتتاحية لمدونة التربة"""
    
    # 1. تحديد الاتجاه البصري والمحاذاة الفورية حسب لغة النظام
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    
    # تغليف المكون بـ HTML لتأمين التنسيق والاتجاه الصحيح في ستريملت عند التبديل
    st.markdown(f"""
    <div dir="{direction}" style="margin-bottom: 20px; text-align: {align};">
        <span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; vertical-align: middle;">{L['phase']}</span> 
        <span style="font-weight: bold; font-size: 1.1rem; margin-left: 8px; margin-right: 8px; color: #1F2937;">{L['eng_comp']}</span> 
        <span style="font-size: 0.85rem; color: #6B7280;">{L['seq_order']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Step 1: تحليل الموقع والمحددات البلدية والأرضية (مكتملة ومترجمة) ---
    with st.container(border=True):
        c1, c2, c3 = st.columns([0.15, 1.0, 0.55])
        with c1:
            st.markdown("<div style='background-color: #E8F5E9; color: #2E7D32; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-family: sans-serif;'>1</div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div style='font-weight: bold; font-size: 0.95rem; color: #1F2937; text-align: {align};'>{L['step1_title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 0.75rem; color: #9CA3AF; text-align: {align};'>{L['step1_desc']}</div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div style='text-align: {align}; color: #10B981; font-weight: bold; font-size: 0.85rem; margin-bottom: 5px;'>{L['completed']}</div>", unsafe_allow_html=True)
            st.button(L['dl_btn'], key="dl_s1", use_container_width=True)

    st.markdown(f"<div style='text-align: center; color: #D1D5DB; margin: -10px 0; font-size: 1.2rem;'>│</div>", unsafe_allow_html=True)

    # --- Step 2: تفعيل بداية ترويسة الخطوة الثانية النشطة لتدقيق التربة ---
    is_pending = st.session_state["step2_status"] == "In Progress"
    border_clr = "#F59E0B" if is_pending else "#10B981"
    badge_text = L['in_progress'] if is_pending else L['completed']
    badge_clr = "#F59E0B" if is_pending else "#10B981"
    
    st.markdown(f"""
    <div dir="{direction}" style="border: 1px solid #E5E7EB; padding: 15px; border-radius: 12px; background-color: #FAFAFA; margin-bottom: 10px; text-align: {align};">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; border-right: 4px solid {border_clr if lang == 'EN' else 'transparent'}; border-left: 4px solid {border_clr if lang == 'AR' else 'transparent'}; padding-right: 10px; padding-left: 10px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="background-color: #FFF3E0; color: #E65100; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-family: sans-serif;">2</div>
                <div>
                    <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937;">{L['step2_title']}</div>
                    <div style="font-size: 0.75rem; color: #6B7280;">{L['step2_desc']}</div>
                </div>
            </div>
            <div style="color: {badge_clr}; font-weight: bold; font-size: 0.85rem;">{badge_text}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<div dir="{direction}" style="text-align: {align};">', unsafe_allow_html=True)
    # ==================== 📍 أولاً: بوابة الفلترة والمحددات البلدية لـ العقار ====================
    stage_title = '📍 المرحلة (أ): بوابة المحددات البلدية والموقع الافتتاحية' if lang == 'AR' else 'Stage (A): Municipal & Location Zoning Gate'
    st.markdown(f"<h5 style='color: #1E3A8A;'>{stage_title}</h5>", unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        gov_lbl = "المحافظة ونطاق المشروع الجغرافي:" if lang == "AR" else "Governorate / Project Scope:"
        gov_opts = {
            "بغداد / وسط العراق": "Baghdad", "صلاح الدين / تربة جبسية حرجية": "Salah_Al_Din",
            "الأنبار / تربة جبسية رسوبية": "Anbar", "النجف الأشرف / خطر تكهفات جيرية": "Najaf",
            "نينوى / تكوينات صخرية كلسية": "Nineveh", "البصرة / تربة طينية رخوة عدوانية": "Basra",
            "المثنى / بادية السماوة وتكهفات": "Muthanna"
        } if lang == "AR" else {
            "Baghdad": "Baghdad", "Salah Al-Din": "Salah_Al_Din", "Anbar": "Anbar",
            "Najaf": "Najaf", "Nineveh": "Nineveh", "Basra": "Basra", "Muthanna": "Muthanna"
        }
        selected_gov_txt = st.selectbox(gov_lbl, list(gov_opts.keys()))
        selected_gov = gov_opts[selected_gov_txt]
        
        req_type_lbl = "نوع الطلب / المعاملة:" if lang == "AR" else "Request / Permit Type:"
        req_opts = ["heavy_projects", "investment_projects", "all"] if lang == "EN" else ["مشاريع ثقيلة وأبراج عالية", "مشاريع استثمارية وتطوير عقاري", "بناء وترميم سكني عام"]
        selected_req = st.selectbox(req_type_lbl, req_opts)

        lot_num_lbl = "رقم قطعة العقار (سند طابو):" if lang == "AR" else "Plot / Parcel Number:"
        st.text_input(lot_num_lbl, value="1024/5", key="lot_num")

    with col_f2:
        usage_lbl = "نوع استعمال العقار الأساسي:" if lang == "AR" else "Primary Land Usage:"
        usage_opts = ["light_commercial_residential", "heavy_commercial_public", "all"] if lang == "EN" else ["سكني وتجاري خفيف / مكاتب", "تجاري ثقيل ومستشفيات ومباني عامة", "جميع الاستعمالات العامة"]
        selected_usage = st.selectbox(usage_lbl, usage_opts)

        area_lbl = "مساحة الأرض الكلية بموجب السند (m²):" if lang == "AR" else "Total Land Area (m²):"
        user_area = st.number_input(area_lbl, min_value=50, max_value=100000, value=250)

        sector_num_lbl = "رقم المقاطعة والبلدية للعقار:" if lang == "AR" else "District / Sector Number:"
        st.text_input(sector_num_lbl, value="42 مكة", key="sector_num")

    with col_f3:
        dim_lbl = "أبعاد واجهة وعمق الأرض (متر):" if lang == "AR" else "Land Dimensions (Meters):"
        st.text_input(dim_lbl, value="10 x 25", key="land_dim")

        street_lbl = "عرض الشارع المقابل للعقار (m):" if lang == "AR" else "Opposite Street Width (m):"
        st.number_input(street_lbl, min_value=4, max_value=100, value=10)

        basement_lbl = "هل يتضمن المخطط طابق سرداب (Basement)؟" if lang == "AR" else "Does it include a Basement floor?"
        basement_opts = ["لا - بدون سرداب", "نعم - يحتوي سرداب"] if lang == "AR" else ["No Basement", "Yes - Includes Basement"]
        has_basement_sel = st.selectbox(basement_lbl, basement_opts)
        has_basement = True if "نعم" in has_basement_sel or "Yes" in has_basement_sel else False

    # حقل عدد الطوابق الحاسم والمحوري للاستنتاج الذكي في بايثون
    floors_lbl = "عدد طوابق المبنى المقترحة فوق مستوى الأرض:" if lang == "AR" else "Proposed Floors Above Ground:"
    building_floors = st.number_input(floors_lbl, min_value=1, max_value=60, value=2)

    # 🧠 استنتاج عقل بايثون الذكي لثقل وخطورة المنشأ تلقائياً في الخلفية
    if building_floors >= 4 or has_basement:
        structural_class_txt = "🏢 منشأ ثقيل / أحمال حرجة عالية" if lang == "AR" else "🏢 Heavy Structure / High Load Class"
        structural_class_clr = "#DC2626"
        is_heavy_structure = True
    else:
        structural_class_txt = "🏡 منشأ خفيف / أحمال اعتيادية منخفضة" if lang == "AR" else "🏡 Light Structure / Normal Load Class"
        structural_class_clr = "#10B981"
        is_heavy_structure = False

    st.markdown(f"""
    <div style="background-color: #F8FAFC; padding: 12px; border-radius: 8px; border-right: 4px solid {structural_class_clr}; border-left: 4px solid {structural_class_clr if lang == 'AR' else 'transparent'}; margin-top: 10px; margin-bottom: 20px;">
        <span style="font-size: 0.85rem; color: #4B5563;">{'🧠 استنتاج عقل النظام التلقائي لثقل المنشأ:' if lang == 'AR' else '🧠 System Automatic Structural Load Inference:'}</span><br>
        <b style="color: {structural_class_clr}; font-size: 1.05rem;">{structural_class_txt}</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    # ==================== 🔬 ثانياً: معطيات فحص التربة والمختبر الجيوتقني ====================
    stage_b_title = '🔬 المرحلة (ب): نتائج الفحوصات المختبرية لتقرير التربة' if lang == 'AR' else 'Stage (B): Geotechnical Laboratory Test Results'
    st.markdown(f"<h5 style='color: #3B82F6;'>{stage_b_title}</h5>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(L['file_uploader_lbl'], type=["pdf"])
    
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        bearing_cap = st.number_input(L['input_bearing'], min_value=10, max_value=500, value=120)
        
        # فلترة جغرافية ذكية: حقل الجبس يظهر فقط في المحافظات المصنفة بالتربة الجبسية لراحة المدقق
        if selected_gov in ["Salah_Al_Din", "Anbar", "Najaf", "Nineveh"]:
            gypsum = st.number_input(L['input_gypsum'], min_value=0.0, max_value=100.0, value=4.50)
        else:
            gypsum = 1.0 # قيمة افتراضية آمنة لبقية النطاقات
            
    with sub_col2:
        # حقل عمق الحفر الفعلي لإقرانه تلقائياً بالاستنتاج الذكي (المنشأ الخفيف والثقيل)
        actual_bh_depth_lbl = "أقصى عمق واصلة له الحفرة الاختبارية ميدانياً (متر):" if lang == "AR" else "Maximum Actual Borehole Depth Executed (meters):"
        actual_bh_depth = st.number_input(actual_bh_depth_lbl, min_value=0.0, max_value=120.0, value=6.0, step=0.5)

        auth_opts = [L['auth_yes'], L['auth_no']]
        report_status_sel = st.selectbox(L['input_auth'], auth_opts)
        report_status = "معتمد ومجاز ومصادق" if report_status_sel == L['auth_yes'] else "غير مصادق"
        
    # تشغيل الفحص والتحقق الرقمي السداسي المربوط بملف الإكسل
    if st.button(L['run_audit'], type="primary", use_container_width=True):
        try:
            from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
            excel_engine = IraqiDynamicComplianceEngine(excel_filename="soil_testing.xlsx")
            
            # حزم البيانات والمدخلات الـ 11 والنتائج الاستنتاجية لإرسالها للمحرك المشترك
            payload = {
                "governorate": selected_gov,
                "total_land_area_m2": user_area,
                "soil_bearing_capacity": bearing_cap,
                "soil_report_status": report_status, 
                "actual_gypsum_percentage": gypsum,
                "is_heavy_structure": is_heavy_structure, # تمرير الاستنتاج التلقائي (ثقيل / خفيف)
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
                
                # طباعة وتوزيع البنود إلى التقارير والرسائل السداسية الإلزامية بالعربي
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
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='text-align: center; color: #D1D5DB; margin: -10px 0; font-size: 1.2rem;'>│</div>", unsafe_allow_html=True)

    # --- الخطوات المغلقة المتسلسلة (Step 3, 4, 5) ---
    steps_data = [("3", L['step3_title']), ("4", L['step4_title']), ("5", L['step5_title'])]
    for step_num, step_title in steps_data:
        with st.container(border=True):
            c1, c2, c3 = st.columns([0.15, 1.0, 0.4])
            with c1: st.markdown("<div>🔒</div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div style='font-weight: bold; font-size: 0.95rem; color: #9CA3AF; text-align: {align};'>{step_title}</div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div style='text-align: right; color: #9CA3AF; font-weight: bold; font-size: 0.85rem;'>{L['locked']}</div>", unsafe_allow_html=True)

    # بنر الباقة المهنية المدفوعة
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div dir="{direction}" style="background-color: #0F172A; color: white; padding: 20px; border-radius: 12px; text-align: {align}; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 1.05rem; margin-bottom: 4px; color: #F59E0B;">{L['premium_title']}</div>
        <div style="font-size: 0.8rem; color: #94A3B8;">{L['premium_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
