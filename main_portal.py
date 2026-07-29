import streamlit as st
import plotly.express as px
import pandas as pd

# 1. إعدادات المظهر البصري للمنصة (الشركة الاستشارية)
st.set_page_config(page_title="منصة البناء المستدام العراقي", page_icon="🏢", layout="wide")

# 2. إدارة وتبديل اللغات بداخل جلسة العميل الموحدة
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

col_logo, col_lang = st.columns()
with col_lang:
    if st.button("🌐 EN" if st.session_state.lang == "ar" else "🌐 العربية", use_container_width=True):
        st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"

# قاموس المصطلحات الفوري لترجمة الواجهة بالكامل
t = {
    "title": {"ar": "🏢 منصة البيانات الوطنية للبناء المستدام العراقي", "en": "🏢 Iraqi National Green Construction Data Platform"},
    "subtitle": {"ar": "بوابة أتمتة كودات البناء وإدارة الطاقة واستشارات السوق العقاري العراقي", "en": "Automated Compliance, Energy Optimization & Market Intelligence Portal"},
    "project_loc": {"ar": "📍 موقع المشروع الحالي: بغداد", "en": "📍 Current Project Location: Baghdad"},
    "user_profile": {"ar": "👤 حساب المهندس: عبدالله علي", "en": "👤 Engineer Profile: Abdulla Ali"},
    "upgrade_btn": {"ar": "👑 تفعيل الباقة الفاخرة واشتراك المنصة", "en": "👑 Upgrade to Premium Suite"},
    "axis1": {"ar": "🏛️ المحور الأول: بوابة مطابقة الكودات الهندسية والأمان", "en": "🏛️ Axis 1: Engineering Compliance & Safety Gate"},
    "axis2": {"ar": "⚡ المحور الثاني: بوابة إدارة الطاقة والاستدامة المالية", "en": "⚡ Axis 2: Energy Optimization & Financial ROI"},
    "axis4": {"ar": "📊 المحور الرابع: لوحة التحليلات الاستراتيجية والمؤشرات العمرانية (B2B)", "en": "📊 Axis 4: Enterprise Market Insights (B2B/Gov)"},
    "locked_msg": {"ar": "🔒 عذراً، هذه الخدمة تتطلب اشتراكاً مدفوعاً وتدفق عمل متسلسل إجباري. يرجى البدء بالبرنامج 1 أولاً.", "en": "🔒 Locked. This service requires a premium subscription and strict sequential workflow. Please start with Program 1."},
}
lang = st.session_state.lang

# 3. هيدر اللوحة الأم والبيانات الجغرافية والتعريفية للمشروع
st.title(t["title"][lang])
st.caption(t["subtitle"][lang])

col_meta1, col_meta2, col_meta3 = st.columns(3)
with col_meta1: st.info(t["project_loc"][lang])
with col_meta2: st.success(t["user_profile"][lang])
with col_meta3: st.button(t["upgrade_btn"][lang], type="primary", use_container_width=True)

st.divider()

# 4. تقسيم الشاشة بلمح البصر (الأزرار على اليسار وعينة التحليلات على اليمين)
col_left, col_right = st.columns()

with col_left:
    st.markdown(f"### {t['axis1'][lang]}")
    # خط إنتاج متسلسل للمطابقة (البرنامج الأول مفتوح للتجربة كـ طُعم للعميل)
    prog1 = st.button("🏢 البرنامج 1: تحليل الموقع والمحددات البلدية (مفتوح للتجربة) ➔", use_container_width=True)
    prog2 = st.button("🧪 البرنامج 2: فحص التربة وتصميم الأسس 🔒", use_container_width=True)
    prog3 = st.button("🧱 البرنامج 3: التدقيق الإنشائي وحساب الأحمال والسلامة 🔒", use_container_width=True)
    prog4 = st.button("🚰 البرنامج 4: هندسة التأسيسات الصحية والمائية 🔒", use_container_width=True)
    prog5 = st.button("⚡ البرنامج 5: هندسة التأسيسات الكهربائية 🔒", use_container_width=True)
    
    st.markdown(f"### {t['axis2'][lang]}")
    prog6 = st.button("❄️ البرنامج 6: حسابات العزل الحراري وغلاف المبنى 🔒", use_container_width=True)
    prog7 = st.button("💨 البرنامج 7: تخمين أحمال التكييف وتصميم المنظومات 🔒", use_container_width=True)
    prog8 = st.button("💰 البرنامج 8: حاسبة كلف التشغيل وفترة استرداد رأس المال 🔒", use_container_width=True)

with col_right:
    st.markdown(f"### {t['axis4'][lang]}")
    st.write("عينة تشويقية من البيانات الجارية لحركة الإعمار وكفاءة العزل في المحافظات العراقية:")
    
    # رسم جارت تفاعلي داخل نفس ملف الواجهة لشد نظر العميل
    df_demo = pd.DataFrame({
        "المحافظة": ["بغداد", "البصرة", "نينوى", "النجف"],
        "التزام المشاريع بالعزل": [35, 12, 55, 28]
    })
    fig = px.bar(df_demo, x="المحافظة", y="التزام المشاريع بالعزل", color="المحافظة", title="نسبة التزام الأبنية بكود العزل الحراري العراقي %")
    st.plotly_chart(fig, use_container_width=True)

# 5. محاكاة التوجيه السحابي المعزول وقفل جدار الحماية المالي
if prog1:
    st.toast("🚀 جاري فتح واجهة البرنامج 1 والمطابقة البلدية...")
    st.markdown("---")
    st.subheader("🏢 البرنامج 1: واجهة فحص حدود البناء والارتدادات")
    
    col_ui1, col_ui2 = st.columns(2)
    with col_ui1:
        area = st.number_input("أدخل مساحة الأرض الإجمالية (متر مربع):", value=200, step=50)
        street = st.number_input("أدخل عرض الشارع الأمامي (متر):", value=10, step=2)
    
    # حسابات الكود خلف الكواليس في نفس الملف
    allowed_area = area * 0.75
    setback = 3 if street > 8 else 2
    
    with col_ui2:
        st.write("📊 النتائج والنسب الفورية الصادرة من محرك التدقيق:")
        st.metric(label="المساحة الصافية المسموح بناؤها قانوناً حسب البلدية", value=f"{allowed_area} م²")
        st.metric(label="الارتداد الأمامي الإجباري لتفادي الغرامات", value=f"{setback} متر")
    
    if st.button("📄 توليد تقرير فحص الموقع الجزئي (PDF مع QR وصحة صدور)"):
        st.success("✅ تم إصدار وثيقة المطابقة الرقمية للموقع بنجاح، ومحمية بباركود صحة الصدور.")

if prog2 or prog3 or prog4 or prog5 or prog6 or prog7 or prog8:
    st.error(t["locked_msg"][lang])
