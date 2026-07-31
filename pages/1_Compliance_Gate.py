# pages/1_Compliance_Gate.py
import streamlit as st

# 1. تفعيل قيم الذاكرة المؤقتة في المقدمة لحل الـ KeyError نهائياً
if "compliance_rate" not in st.session_state:
    st.session_state["compliance_rate"] = 42
if "step2_status" not in st.session_state:
    st.session_state["step2_status"] = "In Progress"
if "lang" not in st.session_state:
    st.session_state["lang"] = "EN"

# 2. استدعاء المكونات البرمجية الثلاثة المستقلة من مجلد الـ components
from components.header import render_header
from components.steps_view import render_steps_and_calculators
from components.sidebar_metrics import render_sidebar_analytics

# 3. رسم واستدعاء المكون الأول: الترويسة وزر اللغة (ويقوم بإرجاع قاموس اللغة النشط)
L = render_header()
lang = st.session_state["lang"]

# 4. فتح التقسيم العمودي الرئيسي للمنصة (الخطوات على اليسار، والتحليلات على اليمين)
col_left, col_right = st.columns([1.4, 1.0], gap="large")

# 5. رسم واستدعاء المكون الثاني: شجرة الخطوات الـ 5 وصندوق الفحص (الجانب الأيسر)
with col_left:
    render_steps_and_calculators(L, lang)

# 6. رسم واستدعاء المكون الثالث: المؤشرات الدائرية والجرين سكور (الجانب الأيمن)
with col_right:
    render_sidebar_analytics(L, lang)
