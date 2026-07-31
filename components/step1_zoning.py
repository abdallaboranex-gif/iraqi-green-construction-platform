# components/step1_zoning.py
import streamlit as st

def render_step1(L, lang, direction, align):
    """رسم وإدارة الخطوة الأولى: بوابة المحددات البلدية الـ 12 الكبرى للعقار"""
    
    # تهيئة وحفظ قيم الجلسة الحية للمحددات الـ 12 لمنع تصفير الحقول
    if "selected_gov" not in st.session_state: st.session_state["selected_gov"] = ""
    if "selected_req" not in st.session_state: st.session_state["selected_req"] = ""
    if "selected_usage" not in st.session_state: st.session_state["selected_usage"] = ""
    if "selected_corner" not in st.session_state: st.session_state["selected_corner"] = ""
    if "has_basement_sel" not in st.session_state: st.session_state["has_basement_sel"] = ""
    if "land_width" not in st.session_state: st.session_state["land_width"] = 0.0
    if "land_length" not in st.session_state: st.session_state["land_length"] = 0.0
    if "building_floors" not in st.session_state: st.session_state["building_floors"] = 0

    # 🧠 فحص الجاهزية الحية: تم التعديل إلى >= 0 لفتح قفل الخطوة الثانية فوراً
    is_step1_ready = (
        st.session_state["selected_gov"] != "" and st.session_state["selected_req"] != "" and 
        st.session_state["selected_usage"] != "" and st.session_state["selected_corner"] != "" and 
        st.session_state["has_basement_sel"] != "" and st.session_state["land_width"] > 0.0 and 
        st.session_state["land_length"] > 0.0 and st.session_state["building_floors"] >= 0
    )

    step1_border = "#10B981" if is_step1_ready else "#F59E0B"
    step1_badge = L['completed'] if is_step1_ready else ("🟡 يرجى إدخال البيانات الموقعية" if lang == "AR" else "🟡 Please Input Zoning Data")
    step1_badge_clr = "#10B981" if is_step1_ready else "#F59E0B"

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
    with col_f1:
        gov_lbl = "المحافظة ونطاق المشروع الجغرافي:" if lang == "AR" else "Governorate:"
        gov_opts = {"اختر المحافظة...": "", "بغداد": "Baghdad", "صلاح الدين": "Salah_Al_Din", "الأنبار": "Anbar", "النجف الأشرف": "Najaf", "نينوى": "Nineveh", "البصرة": "Basra", "المثنى": "Muthanna"}
        gov_list = list(gov_opts.keys())
        idx_gov = gov_list.index(list(gov_opts.keys())[list(gov_opts.values()).index(st.session_state["selected_gov"])]) if st.session_state["selected_gov"] in gov_opts.values() and st.session_state["selected_gov"] != "" else 0
        selected_gov_txt = st.selectbox(gov_lbl, gov_list, index=idx_gov)
        st.session_state["selected_gov"] = gov_opts[selected_gov_txt]
        
        req_opts = ["", "بناء جديد", "إعادة بناء", "إضافة طابق", "ترميم", "مشاريع كبرى"] if lang == "AR" else ["", "New Construction", "Reconstruction", "Floor Addition", "Renovation", "Major Projects"]
        idx_req = req_opts.index(st.session_state["selected_req"]) if st.session_state["selected_req"] in req_opts else 0
        st.session_state["selected_req"] = st.selectbox("نوع المعاملة:", req_opts, index=idx_req)
        st.text_input("رقم قطعة العقار:", value="", placeholder="1024/5", key="lot_num")

    with col_f2:
        usage_opts = ["", "سكني", "تجاري", "خدمي", "صناعي", "مجمعات"] if lang == "AR" else ["", "Residential", "Commercial", "Service", "Industrial", "Complexes"]
        idx_use = usage_opts.index(st.session_state["selected_usage"]) if st.session_state["selected_usage"] in usage_opts else 0
        st.session_state["selected_usage"] = st.selectbox("نوع استعمال العقار:", usage_opts, index=idx_use)
        st.session_state["land_width"] = st.number_input("عرض الواجهة (متر):", min_value=0.0, value=st.session_state["land_width"], step=0.5)
        st.text_input("رقم المقاطعة والبلدية:", value="", placeholder="42 مكة", key="sector_num")

    with col_f3:
        st.number_input("عرض الشارع المقابل (m):", min_value=0.0, value=0.0, step=0.5, key="street_width")
        st.session_state["land_length"] = st.number_input("طول النزال (متر):", min_value=0.0, value=st.session_state["land_length"], step=0.5)
        corner_opts = ["", "عادي / وسطي", "ركن / زاوية"] if lang == "AR" else ["", "Standard", "Corner Plot"]
        idx_crn = corner_opts.index(st.session_state["selected_corner"]) if st.session_state["selected_corner"] in corner_opts else 0
        st.session_state["selected_corner"] = st.selectbox("موضع قطعة الأرض:", corner_opts, index=idx_crn)

    col_sub_f1, col_sub_f2 = st.columns(2)
    with col_sub_f1:
        basement_opts = ["", "موجود", "غير موجود"] if lang == "AR" else ["", "Present", "Not Present"]
        idx_bsm = basement_opts.index(st.session_state["has_basement_sel"]) if st.session_state["has_basement_sel"] in basement_opts else 0
        st.session_state["has_basement_sel"] = st.selectbox("طابق السرداب (Basement):", basement_opts, index=idx_bsm)
        has_basement = True if st.session_state["has_basement_sel"] in ["موجود", "Present"] else False

    with col_sub_f2:
        st.session_state["building_floors"] = st.number_input("عدد الطوابق المقترحة:", min_value=0, value=st.session_state["building_floors"])

    user_area = st.session_state["land_width"] * st.session_state["land_length"]
    building_floors = st.session_state["building_floors"]

    if building_floors >= 0 and user_area > 0:
        is_heavy = building_floors >= 4 or has_basement
        class_txt = "🏢 منشأ ثقيل / أحمال حرجة" if is_heavy else "🏡 منشأ خفيف / أحمال اعتيادية"
        class_clr = "#DC2626" if is_heavy else "#10B981"
        st.markdown(f"<div style='background-color:#F8FAFC; padding:8px; border-right:4px solid {class_clr}; font-size:0.85rem; font-weight:bold; color:{class_clr}; text-align:{align};'>{class_txt} | المساحة: {user_area:.1f} m²</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)
    return is_step1_ready, user_area, building_floors, st.session_state["selected_gov"], has_basement
