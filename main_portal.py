import streamlit as st

# 1. إعدادات المظهر البصري وهوية الشركة الاستشارية
st.set_page_config(page_title="منصة البناء المستدام العراقي", page_icon="🏢", layout="wide")

# 2. حقن ثيم الـ CSS الحديث لإلغاء المظهر التقليدي (تدرجات ألوان نيلي، كتل عائمة، خطوط عصرية)
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    * {
        font-family: 'Tajawal', sans-serif !important;
    }
    .stApp {
        background-color: #F8FAFC;
    }
    .main-header {
        background: linear-gradient(135deg, #0A2540 0%, #1E3A8A 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(10, 37, 64, 0.15);
    }
    .axis-container {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
    }
    .axis-title-1 {
        color: #0A2540;
        border-right: 5px solid #00CC96;
        padding-right: 10px;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .axis-title-2 {
        color: #0A2540;
        border-right: 5px solid #FF9F43;
        padding-right: 10px;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    /* تنسيق أزرار البرامج لتظهر كروابط وكتل ويب فاخرة */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #334155 !important;
        border: 1px solid #E2E8F0 !important;
        padding: 0.75rem 1rem !important;
        border-radius: 8px !important;
        text-align: right !important;
        font-weight: 500 !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        transition: all 0.2s ease-in-out !important;
    }
    div.stButton > button:hover {
        border-color: #00CC96 !important;
        color: #00CC96 !important;
        background-color: #F0FDF4 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0, 204, 150, 0.1) !important;
    }
    .premium-badge {
        background-color: #FEF3C7;
        color: #D97706;
        padding: 0.25rem 0.5rem;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة وتبديل اللغات بداخل جلسة العميل الموحدة
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

col_logo, col_lang = st.columns([6, 1])
with col_lang:
    if st.button("🌐 EN" if st.session_state.lang == "ar" else "🌐 العربية", use_container_width=True):
        st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"
        st.rerun()

# قاموس المصطلحات المحدث كلياً للواجهة الفاخرة
t = {
    "title": {"ar": "منصة البيانات الوطنية للبناء المستدام العراقي 🏢", "en": "Iraqi National Green Construction Data Platform 🏢"},
    "subtitle": {"ar": "بوابة الشركة لأتمتة كودات البناء وإدارة الطاقة واستشارات السوق العقاري", "en": "Automated Compliance, Energy Optimization & Market Intelligence Portal"},
    "project_loc": {"ar": "📍 موقع المشروع الحالي: بغداد", "en": "📍 Current Project Location: Baghdad"},
    "user_profile": {"ar": "👤 حساب المهندس: عبدالله علي", "en": "👤 Engineer Profile: Abdulla Ali"},
    "upgrade_btn": {"ar": "👑 تفعيل الباقة الفاخرة", "en": "👑 Upgrade to Premium Suite"},
    "axis1": {"ar": "🏛️ المحور الأول: بوابة مطابقة الكودات الهندسية والأمان", "en": "🏛️ Axis 1: Engineering Compliance & Safety Gate"},
    "axis2": {"ar": "⚡ المحور الثاني: بوابة إدارة الطاقة والاستدامة المالية", "en": "⚡ Axis 2: Energy Optimization & Financial ROI"},
    "locked_msg": {"ar": "🔒 عذراً، هذه الخدمة تتطلب اشتراكاً مدفوعاً وتدفق عمل متسلسل إجباري. يرجى البدء بالبرنامج 1 أولاً.", "en": "🔒 Locked. This service requires a premium subscription and strict sequential workflow. Please start with Program 1."},
    
    "prog1": {"ar": "🏢 البرنامج 1: تحليل الموقع والمحددات البلدية (مفتوح للتجربة) ➔", "en": "🏢 Program 1: Site Analysis & Zoning Regulations (Open for Demo) ➔"},
    "prog2": {"ar": "🧪 البرنامج 2: فحص التربة وتصميم الأسس 🔒", "en": "🧪 Program 2: Geotechnical Inspection & Foundation Design 🔒"},
    "prog3": {"ar": "🧱 البرنامج 3: التدقيق الإنشائي وحساب الأحمال والسلامة 🔒", "en": "🧱 Program 3: Structural Audit & Load Calculations 🔒"},
    "prog4": {"ar": "🚰 البرنامج 4: هندسة التأسيسات الصحية والمائية 🔒", "en": "🚰 Program 4: Hydro-Sanitary & Plumbing Design 🔒"},
    "prog5": {"ar": "⚡ البرنامج 5: هندسة التأسيسات الكهربائية 🔒", "en": "⚡ Program 5: Electrical Systems Analysis 🔒"},
    
    "prog6": {"ar": "❄️ البرنامج 6: حسابات العزل الحراري وغلاف المبنى 🔒", "en": "❄️ Program 6: Thermal Insulation & Building Envelope 🔒"},
    "prog7": {"ar": "💨 البرنامج 7: تخمين أحمال التكييف وتصميم المنظومات 🔒", "en": "💨 Program 7: HVAC Load Estimation & System Design 🔒"},
    "prog8": {"ar": "💰 البرنامج 8: حاسبة كلف التشغيل وفترة استرداد رأس المال 🔒", "en": "💰 Program 8: Operational Cost & ROI Calculator 🔒"},
    
    "prog1_sub": {"ar": "🏢 البرنامج 1: واجهة فحص حدود البناء والارتدادات", "en": "🏢 Program 1: Zoning Limits & Road Setbacks Interface"},
    "input_area": {"ar": "أدخل مساحة الأرض الكلية (متر مربع):", "en": "Enter Total Land Area (sqm):"},
    "input_street": {"ar": "أدخل عرض الشارع الأمامي (متر):", "en": "Enter Front Street Width (meters):"},
    "res_title": {"ar": "📊 النتائج والنسب الفورية الصادرة من محرك التدقيق:", "en": "📊 Real-Time Results From Audit Engine:"},
    "res_area": {"ar": "المساحة الصافية المسموح بناؤها قانوناً حسب البلدية", "en": "Max Allowable Built-Up Area by Municipality"},
    "res_setback": {"ar": "الارتداد الأمامي الإجباري لتفادي الغرامات", "en": "Mandatory Front Road Setback"},
    "pdf_btn": {"ar": "📄 توليد تقرير فحص الموقع الجزئي (PDF مع QR وصحة صدور)", "en": "📄 Generate Certified Audit Report (PDF with Secure QR Code)"},
    "pdf_success": {"ar": "✅ تم إصدار وثيقة المطابقة الرقمية للموقع بنجاح، ومحمية بباركود صحة الصدور.", "en": "✅ Digital Compliance Certificate Issued Successfully. Protected by Secure QR verification Verification."},
}
lang = st.session_state.lang

# 4. تصفيف الهيدر الموحد الفاخر (تدرج لوني نيلي)
st.markdown(f"""
    <div class="main-header">
        <h1 style="color: white; margin: 0; font-size: 2.2rem; font-weight: 700;">{t["title"][lang]}</h1>
        <p style="color: #94A3B8; margin: 0.5rem 0 0 0; font-size: 1.1rem;">{t["subtitle"][lang]}</p>
    </div>
    """, unsafe_allow_html=True)

col_meta1, col_meta2, col_meta3 = st.columns(3)
with col_meta1: st.info(t["project_loc"][lang])
with col_meta2: st.success(t["user_profile"][lang])
with col_meta3: st.button(t["upgrade_btn"][lang], type="primary", use_container_width=True)

st.divider()

# 5. عرض كتل المحاور الستة على شكل حاويات أنيقة ومتباعدة
# المحور الأول
st.markdown(f'<div class="axis-container"><div class="axis-title-1">{t["axis1"][lang]}</div>', unsafe_allow_html=True)
prog1 = st.button(t["prog1"][lang], use_container_width=True)
prog2 = st.button(t["prog2"][lang], use_container_width=True)
prog3 = st.button(t["prog3"][lang], use_container_width=True)
prog4 = st.button(t["prog4"][lang], use_container_width=True)
prog5 = st.button(t["prog5"][lang], use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# المحور الثاني
st.markdown(f'<div class="axis-container"><div class="axis-title-2">{t["axis2"][lang]}</div>', unsafe_allow_html=True)
prog6 = st.button(t["prog6"][lang], use_container_width=True)
prog7 = st.button(t["prog7"][lang], use_container_width=True)
prog8 = st.button(t["prog8"][lang], use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 6. محاكاة التوجيه السحابي المعزول لخط المطابقة المتسلسل
if prog1:
    st.toast("🚀 Open Program 1 UI..." if lang == "en" else "🚀 جاري فتح واجهة البرنامج 1...")
    st.markdown("""
        <div class="axis-container" style="border-color: #00CC96; background-color: #F8FAFC;">
        """, unsafe_allow_html=True)
    st.subheader(t["prog1_sub"][lang])
    
    col_ui1, col_ui2 = st.columns(2)
    with col_ui1:
        area = st.number_input(t["input_area"][lang], value=200, step=50)
        street = st.number_input(t["input_street"][lang], value=10, step=2)
    
    allowed_area = area * 0.75
    setback = 3 if street > 8 else 2
    
    with col_ui2:
        st.write(t["res_title"][lang])
        st.metric(label=t["res_area"][lang], value=f"{allowed_area} m²" if lang == "en" else f"{allowed_area} م²")
        st.metric(label=t["res_setback"][lang], value=f"{setback} meters" if lang == "en" else f"{setback} متر")
    
    if st.button(t["pdf_btn"][lang]):
        st.success(t["pdf_success"][lang])
    st.markdown('</div>', unsafe_allow_html=True)

if prog2 or prog3 or prog4 or prog5 or prog6 or prog7 or prog8:
    st.error(t["locked_msg"][lang])
