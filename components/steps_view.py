# components/steps_view.py
import streamlit as st

def render_steps_and_calculators(L, lang):
    """رسم وإدارة شجرة الخطوات الـ 5 والمطابقة الكودية الاعتمادية على الإكسل"""
    
    # تحديد الاتجاه البصري والمحاذاة حسب لغة النظام النشطة بضغطة الزر
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    
    # تغليف المكون بالكامل بـ HTML لتأمين التنسيق والاتجاه الصحيح في ستريملت
    st.markdown(f"""
    <div dir="{direction}" style="margin-bottom: 20px; text-align: {align};">
        <span style="background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; vertical-align: middle;">{L['phase']}</span> 
        <span style="font-weight: bold; font-size: 1.1rem; margin-left: 8px; margin-right: 8px; color: #1F2937;">{L['eng_comp']}</span> 
        <span style="font-size: 0.85rem; color: #6B7280;">{L['seq_order']}</span>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Step 1: تحليل الموقع والمحددات البلدية (مكتملة ومترجمة) ---
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

    # --- Step 2: فحص التربة والأسس الجيوتقنية (النشطة والمترجمة بالكامل) ---
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
    
    # فتح نظام المحاذاة والاتجاه لحقول ستريملت الفعلية لمنع الخربطة البصرية بالعربي
    st.markdown(f'<div dir="{direction}" style="text-align: {align};">', unsafe_allow_html=True)
    
    # 1. صندوق الرفع المترجم ديناميكياً
    uploaded_file = st.file_uploader(L['file_uploader_lbl'], type=["pdf"])
    
    # 2. الحقول الرقمية المترجمة والمربوطة بالكامل بالقاموس
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        bearing_cap = st.number_input(L['input_bearing'], min_value=10, max_value=500, value=120)
        gypsum = st.number_input(L['input_gypsum'], min_value=0.0, max_value=100.0, value=4.50)
    with sub_col2:
        building_height = st.number_input(L['input_height'], min_value=3, max_value=50, value=10)
        auth_opts = [L['auth_yes'], L['auth_no']]
        report_status_sel = st.selectbox(L['input_auth'], auth_opts)
        report_status = "معتمد ومجاز ومصادق" if report_status_sel == L['auth_yes'] else "غير مصادق"
        
    # 3. زر تشغيل الفحص المترجم بالكامل
    if st.button(L['run_audit'], type="primary", use_container_width=True):
        try:
            from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
            excel_engine = IraqiDynamicComplianceEngine(excel_filename="soil_testing.xlsx")
            
            payload = {
                "governorate": "Salah_Al_Din", 
                "total_land_area_m2": 300, 
                "building_height_meters": building_height, 
                "soil_bearing_capacity": bearing_cap,
                "soil_report_status": report_status, 
                "actual_gypsum_percentage": gypsum
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
                
                # طباعة التقرير السداسي العربي المنظم
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
            
    st.markdown("</div>", unsafe_allow_html=True) # إغلاق حاوية الحماية البصرية بالـ HTML
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='text-align: center; color: #D1D5DB; margin: -10px 0; font-size: 1.2rem;'>│</div>", unsafe_allow_html=True)

    # --- الخطوات المغلقة المتسلسلة المترجمة (Step 3, 4, 5) ---
    steps_data = [("3", L['step3_title']), ("4", L['step4_title']), ("5", L['step5_title'])]
    for step_num, step_title in steps_data:
        with st.container(border=True):
            c1, c2, c3 = st.columns([0.15, 1.0, 0.4])
            with c1: st.markdown("<div>🔒</div>", unsafe_allow_html=True)
            with c2: st.markdown(f"<div style='font-weight: bold; font-size: 0.95rem; color: #9CA3AF; text-align: {align};'>{step_title}</div>", unsafe_allow_html=True)
            with c3: st.markdown(f"<div style='text-align: right; color: #9CA3AF; font-weight: bold; font-size: 0.85rem;'>{L['locked']}</div>", unsafe_allow_html=True)

    # بنر الاشتراك المترجم والمنظم
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div dir="{direction}" style="background-color: #0F172A; color: white; padding: 20px; border-radius: 12px; text-align: {align}; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 1.05rem; margin-bottom: 4px; color: #F59E0B;">{L['premium_title']}</div>
        <div style="font-size: 0.8rem; color: #94A3B8;">{L['premium_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
