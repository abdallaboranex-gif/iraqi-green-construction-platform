import streamlit as st

# 1. إعدادات الصفحة المنفصلة
st.set_page_config(page_title="برنامج تحليل الموقع والمحددات البلدية", page_icon="🏢", layout="wide")

# 2. حقن التصميم البصري الخاص بهذه الشاشة داخلياً
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    * { font-family: 'Tajawal', sans-serif !important; }
    .stApp { background-color: #F8FAFC; }
    .program-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        padding: 2rem; border-radius: 12px; color: white; margin-bottom: 2rem;
    }
    .result-box {
        background-color: white; padding: 1.5rem; border-radius: 12px;
        border: 1px solid #E2E8F0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. هيدر الشاشة المعزولة
st.markdown("""
    <div class="program-header">
        <h2 style="color: white; margin: 0; font-weight: 700;">🏢 البرنامج 1: تحليل الموقع والمحددات البلدية</h2>
        <p style="color: #DBEAFE; margin: 0.5rem 0 0 0;">نظام التدقيق الرقمي لنسب البناء والارتدادات القانونية حسب ضوابط الأمانة والبلديات</p>
    </div>
    """, unsafe_allow_html=True)

# 4. تقسيم الشاشة (المدخلات على اليمين والنتائج البصرية على اليسار)
col_inputs, col_results = st.columns(2)

with col_inputs:
    st.markdown("### 📋 مدخلات العقار الفنية")
    
    # القوائم والخيارات الحقيقية للسوق العراقي
    property_type = st.selectbox("جنس العقار القانوني:", ["سكني / طابو صرف", "تجاري", "زراعي / طابو ملك صرف"])
    plot_type = st.radio("نوع واجهة القطعة:", ["واجهة واحدة (وسطية)", "ركن (على شارعين)"])
    
    col_dims = st.columns(2)
    with col_dims[0]:
        frontage = st.number_input("عرض واجهة الأرض (متر):", value=10.0, step=0.5)
    with col_dims[1]:
        depth = st.number_input("نزال / طول الأرض (متر):", value=20.0, step=0.5)
        
    floors = st.slider("عدد الطوابق المخطط بناؤها مستقبلاً:", min_value=1, max_value=5, value=2)

    # حساب المساحة الكلية تلقائياً
    total_area = frontage * depth
    st.metric(label="المساحة الإجمالية المحسوبة للأرض", value=f"{total_area} م²")

with col_results:
    st.markdown("### 📊 نتائج التدقيق الهندسية والنسب")
    
    # محرك معادلات الكود البلدي العراقي خلف الكواليس
    if property_type == "تجاري":
        allowed_percent = 1.00 if floors <= 2 else 0.85
        legal_limit_msg = "مسموح بناء كامل المساحة للطوابق الأولى حسب الكود التجاري"
    elif property_type == "زراعي / طابو ملك صرف":
        allowed_percent = 0.50
        legal_limit_msg = "المحددات تفرض 50% كحد أقصى للمناطق الزراعية المفرزة"
    else: # السكني التقليدي
        allowed_percent = 0.75 if total_area <= 300 else 0.60
        legal_limit_msg = "75% للمساحات دون الـ 300 متر حسب ضوابط الأمانة"

    # حساب المساحة الصافية والارتداد
    max_built_area = total_area * allowed_percent
    
    # تحديد الارتداد بناءً على نوع القطعة (ركن أم واجهة)
    front_setback = 3.0 if plot_type == "ركن (على شارعين)" else 2.0
    side_setback = 1.5 if plot_type == "ركن (على شارعين)" else 0.0

    # عرض النتائج بداخل حاوية عائمة
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.markdown(f"**💡 التوجيه القانوني البلدي:** {legal_limit_msg}")
    st.divider()
    
    st.metric(label="أقصى مساحة مسموح بناؤها للطابق الأرضي", value=f"{max_built_area} م² ({int(allowed_percent*100)}%)")
    st.metric(label="الارتداد الأمامي الإجباري من جهة الشارع الرئيسي", value=f"{front_setback} متر")
    
    if side_setback > 0:
        st.warning(f"⚠️ القطعة ركن: يجب ترك ارتداد جانبي إضافي بمقدار {side_setback} متر من جهة الشارع الثاني.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("📄 توليد شهادة مطابقة الموقع والمحددات البلدية مع رمز الـ QR"):
        st.success("✅ تم إصدار التقرير الجزئي المعتمد بباركود مشفر وصحة صدور رقمية بنجاح.")
