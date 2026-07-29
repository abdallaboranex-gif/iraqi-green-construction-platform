import streamlit as st

# 1. إعدادات المظهر البصري وهوية شركة الاستدامة الخضراء
st.set_page_config(page_title="منصة البناء المستدام - الاستدامة الخضراء", page_icon="🏢", layout="wide")

# 2. حقن ثيم الـ CSS المتطابق مع هيكلية المجلدات المحلية والامتداد الحقيقي .jpeg
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    * {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    /* قراءة الخلفية محلياً ومباشرة من مجلد assets بالامتداد الصحيح .jpeg الظاهر في غيت هاب */
    .stApp {
        background: linear-gradient(rgba(10, 37, 64, 0.75), rgba(10, 37, 64, 0.75)), 
                    url('app/static/assets/cloud_grid_bg.jpeg') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }
    
    /* تنسيق حاوية اللوغو لتكون أنيقة وحجمها 180 بكسل فقط في الزاوية */
    [data-testid="stImage"] img {
        width: 180px !important;
        height: auto !important;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* تنسيق الحاويات العائمة للأزرار والبرامج */
    .axis-container {
        background-color: rgba(255, 255, 255, 0.95) !important;
        padding: 1.75rem !important;
        border-radius: 14px !important;
        border: 1px solid rgba(226, 232, 240, 0.8) !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important;
        margin-bottom: 1.5rem !important;
        backdrop-filter: blur(8px) !important;
    }
    
    .axis-title-1 {
        color: #0A2540 !important;
        border-right: 5px solid #00CC96 !important;
        padding-right: 10px !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        margin-bottom: 1.25rem !important;
    }
    
    .axis-title-2 {
        color: #0A2540 !important;
        border-right: 5px solid #FF9F43 !important;
        padding-right: 10px !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        margin-bottom: 1.25rem !important;
    }

    /* أزرار الخدمات والبرامج الممتدة الفاخرة */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #334155 !important;
        border: 1px solid #E2E8F0 !important;
        padding: 0.8rem 1.2rem !important;
        border-radius: 10px !important;
        text-align: right !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
        transition: all 0.25s ease-in-out !important;
    }
    
    div.stButton > button:hover {
        border-color: #00CC96 !important;
        color: #00CC96 !important;
        background-color: #F0FDF4 !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 20px rgba(0, 204, 150, 0.15) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة وتبديل اللغات بداخل جلسة العميل الموحدة
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

# صف هيدر علوي مخصص لعرض اللوغو وزر اللغة بالامتداد الفعلي .jpeg من مجلد الأصول المحلي
col_logo_img, col_empty, col_lang = st.columns(3)
with col_logo_img:
    st.image("assets/corporate_logo.jpeg")

with col_lang:
    if st.button("🌐 EN" if st.session_state.lang == "ar" else "🌐 العربية", use_container_width=True):
        st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"
        st.rerun()

# قاموس المصطلحات المترجم بالكامل للوحة الأم
t = {
    "title": {"ar": "منصة البيانات الوطنية للبناء المستدام 🏢", "en": "National Green Construction Data Platform 🏢"},
    "subtitle": {"ar": "بوابة شركة الاستدامة الخضراء لأتمتة الكودات الهندسية واستشارات السوق العقاري", "en": "Automated Compliance, Energy Optimization & Market Intelligence Portal"},
    "project_loc": {"ar": "📍 موقع المشروع الحالي: بغداد", "en": "📍 Current Project Location: Baghdad"},
    "user_profile": {"ar": "👤 حساب المهندس: عبدالله علي", "en": "👤 Engineer Profile: Abdulla Ali"},
    "upgrade_btn": {"ar": "👑 تفعيل الباقة الفاخرة واشتراك المنصة", "en": "👑 Upgrade to Premium Suite"},
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
}
lang = st.session_state.lang

# 4. عرض نصوص العناوين الرئيسية بلون أبيض ناصع ليظهر فوق الخلفية الداكنة
st.markdown(f'<h1 style="color: white; font-weight: 700;">{t["title"][lang]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="color: #E2E8F0; font-size: 1.2rem; margin-top: -10px;">{t["subtitle"][lang]}</p>', unsafe_allow_html=True)

col_meta1, col_meta2, col_meta3 = st.columns(3)
with col_meta1: st.info(t["project_loc"][lang])
with col_meta2: st.success(t["user_profile"][lang])
with col_meta3: st.button(t["upgrade_btn"][lang], type="primary", use_container_width=True)

st.divider()

# 5. عرض كتل المحاور كحاويات عائمة أنيقة فوق الخلفية الملكية
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

# 6. إطلاق رسالة القفل المالي عند الضغط على الأزرار المحمية
if prog1:
    st.toast("🚀 Open Program 1 UI..." if lang == "en" else "🚀 جاري فتح واجهة البرنامج 1...")
if prog2 or prog3 or prog4 or prog5 or prog6 or prog7 or prog8:
    st.error(t["locked_msg"][lang])
