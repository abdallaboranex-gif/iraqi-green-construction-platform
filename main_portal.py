import streamlit as st

# 1. إعدادات المظهر البصري للمنصة
st.set_page_config(page_title="منصة البناء المستدام العراقي", page_icon="🏢", layout="wide")

# 2. إدارة وتبديل اللغات بداخل جلسة العميل
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

col_logo, col_lang = st.columns(2)
with col_lang:
    if st.button("🌐 EN" if st.session_state.lang == "ar" else "🌐 العربية", use_container_width=True):
        st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"

# قاموس المصطلحات الشامل والمحدث لجميع الأزرار والبرامج بالكامل
t = {
    "title": {"ar": "🏢 منصة البيانات الوطنية للبناء المستدام العراقي", "en": "🏢 Iraqi National Green Construction Data Platform"},
    "subtitle": {"ar": "بوابة أتمتة كودات البناء وإدارة الطاقة واستشارات السوق العقاري العراقي", "en": "Automated Compliance, Energy Optimization & Market Intelligence Portal"},
    "project_loc": {"ar": "📍 موقع المشروع الحالي: بغداد", "en": "📍 Current Project Location: Baghdad"},
    "user_profile": {"ar": "👤 حساب المهندس: عبدالله علي", "en": "👤 Engineer Profile: Abdulla Ali"},
    "upgrade_btn": {"ar": "👑 تفعيل الباقة الفاخرة واشتراك المنصة", "en": "👑 Upgrade to Premium Suite"},
    "axis1": {"ar": "🏛️ المحور الأول: بوابة مطابقة الكودات الهندسية والأمان", "en": "🏛️ Axis 1: Engineering Compliance & Safety Gate"},
    "axis2": {"ar": "⚡ المحور الثاني: بوابة إدارة الطاقة والاستدامة المالية", "en": "⚡ Axis 2: Energy Optimization & Financial ROI"},
    "locked_msg": {"ar": "🔒 عذراً، هذه الخدمة تتطلب اشتراكاً مدفوعاً وتدفق عمل متسلسل إجباري. يرجى البدء بالبرنامج 1 أولاً.", "en": "🔒 Locked. This service requires a premium subscription and strict sequential workflow. Please start with Program 1."},
    
    # ترجمة أزرار المحور الأول
    "prog1": {"ar": "🏢 البرنامج 1: تحليل الموقع والمحددات البلدية (مفتوح للتجربة) ➔", "en": "🏢 Program 1: Site Analysis & Zoning Regulations (Open for Demo) ➔"},
    "prog2": {"ar": "🧪 البرنامج 2: fحص التربة وتصميم الأسس 🔒", "en": "🧪 Program 2: Geotechnical Inspection & Foundation Design 🔒"},
    "prog3": {"ar": "🧱 البرنامج 3: التدقيق الإنشائي وحساب الأحمال والسلامة 🔒", "en": "🧱 Program 3: Structural Audit & Load Calculations 🔒"},
    "prog4": {"ar": "🚰 البرنامج 4: هندسة التأسيسات الصحية والمائية 🔒", "en": "🚰 Program 4: Hydro-Sanitary & Plumbing Design 🔒"},
    "prog5": {"ar": "⚡ البرنامج 5: هندسة التأسيسات الكهربائية 🔒", "en": "⚡ Program 5: Electrical Systems Analysis 🔒"},
    
    # ترجمة أزرار المحور الثاني
    "prog6": {"ar": "❄️ البرنامج 6: حسابات العزل الحراري وغلاف المبنى 🔒", "en": "❄️ Program 6: Thermal Insulation & Building Envelope 🔒"},
    "prog7": {"ar": "💨 البرنامج 7: تخمين أحمال التكييف وتصميم المنظومات 🔒", "en": "💨 Program 7: HVAC Load Estimation & System Design 🔒"},
    "prog8": {"ar": "💰 البرنامج 8: حاسبة كلف التشغيل وفترة استرداد رأس المال 🔒", "en": "💰 Program 8: Operational Cost & ROI Calculator 🔒"},
    
    # ترجمة محاكاة واجهة البرنامج الأول
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

# 3. هيدر اللوحة الأم والبيانات الجغرافية
st.title(t["title"][lang])
st.caption(t["subtitle"][lang])

col_meta1, col_meta2, col_meta3 = st.columns(3)
with col_meta1: st.info(t["project_loc"][lang])
with col_meta2: st.success(t["user_profile"][lang])
with col_meta3: st.button(t["upgrade_btn"][lang], type="primary", use_container_width=True)

st.divider()

# 4. أزرار البرامج الـ 14 (تم ربطها ديناميكياً بقاموس اللغات هنا)
st.markdown(f"### {t['axis1'][lang]}")
prog1 = st.button(t["prog1"][lang], use_container_width=True)
prog2 = st.button(t["prog2"][lang], use_container_width=True)
prog3 = st.button(t["prog3"][lang], use_container_width=True)
prog4 = st.button(t["prog4"][lang], use_container_width=True)
prog5 = st.button(t["prog5"][lang], use_container_width=True)

st.markdown(f"### {t['axis2'][lang]}")
prog6 = st.button(t["prog6"][lang], use_container_width=True)
prog7 = st.button(t["prog7"][lang], use_container_width=True)
prog8 = st.button(t["prog8"][lang], use_container_width=True)

# 5. محاكاة التوجيه السحابي المعزول وقفل جدار الحماية المالي
if prog1:
    st.toast("🚀 Open Program 1 UI..." if lang == "en" else "🚀 جاري فتح واجهة البرنامج 1...")
    st.markdown("---")
    st.subheader(t["prog1_sub"][lang])
    
    col_ui1, col_ui2 = st.columns(2)
    with col_ui1:
        area = st.number_input(t["input_area"][lang], value=200, step=50)
        street = st.number_input(t["input_street"][lang], value=10, step=2)
    
    # حسابات الكود خلف الكواليس
    allowed_area = area * 0.75
    setback = 3 if street > 8 else 2
    
    with col_ui2:
        st.write(t["res_title"][lang])
        st.metric(label=t["res_area"][lang], value=f"{allowed_area} m²" if lang == "en" else f"{allowed_area} م²")
        st.metric(label=t["res_setback"][lang], value=f"{setback} meters" if lang == "en" else f"{setback} متر")
    
    if st.button(t["pdf_btn"][lang]):
        st.success(t["pdf_success"][lang])

if prog2 or prog3 or prog4 or prog5 or prog6 or prog7 or prog8:
    st.error(t["locked_msg"][lang])
