import streamlit as st
import plotly.graph_objects as go
# استدعاء الثوابت ومحرك الفحص العراقي الذي أنشأته في الدفعات السابقة
from shared_utils.engines.engineering_compliance_engine import verify_soil_report

# 1. إعدادات الصفحة وهوية المنصة البصرية
st.set_page_config(page_title="Iraqi Green Construction Data Platform", page_icon="🏗️", layout="wide")

# تهيئة الذاكرة المؤقتة (Session State) لحفظ حالة الخطوات ونتائج الفحص الهندسي
if "step2_completed" not in st.session_state:
    st.session_state.step2_completed = False
if "compliance_rate" not in st.session_state:
    st.session_state.compliance_rate = 42
if "chart_data" not in st.session_state:
    st.session_state.chart_data = [20, 25, 30, 35, 42, 42]
if "soil_results" not in st.session_state:
    st.session_state.soil_results = None

# تطبيق كود التنسيق الهيكلي (CSS) بطريقة آمنة
theme_css = """
<style>
    .stApp { background-color: #F8FAFC !important; }
    .card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; height: 100%; }
    .step-box { border: 1px solid #E2E8F0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #F8FAFC; }
    .step-active { border: 1px solid #FFEDD5; background-color: #FFFFf0; border-left: 5px solid #F97316; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
    .step-done { border: 1px solid #D1FAE5; background-color: #F0FDF4; border-left: 5px solid #10B981; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
    .premium-box { background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%); color: white; padding: 20px; border-radius: 12px; margin-top: 20px; }
    .green-text { color: #059669; font-weight: bold; }
    .gray-text { color: #64748B; }
    .completed-badge { float: right; background-color: #D1FAE5; color: #065F46; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; }
    .progress-badge { float: right; background-color: #FFEDD5; color: #9A3412; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; }
    .card-title { font-weight: bold; margin-bottom: 5px; color: #1E293B; }
    .card-value { font-size: 28px; font-weight: bold; margin: 0; color: #0F172A; }
</style>
"""
st.html(theme_css)

# 2. الهيدر العلوي للمنصة
with st.container():
    col_logo, col_lang, col_loc, col_user = st.columns(4)
    with col_logo:
        st.markdown("### 🏢 Iraqi Green Construction")
        st.caption("Data • Compliance • Sustainability • Efficiency")
    with col_lang:
        st.segmented_control("Language", ["العربية", "EN"], default="EN", label_visibility="collapsed")
    with col_loc:
        st.markdown("**📍 Current Project Location:**")
        st.html("<span class='green-text'>Baghdad</span>")
    with col_user:
        st.markdown("**👨‍💼 Eng. Abdulla**")
        st.html("<span class='gray-text'>Project Manager</span>")

st.markdown("---")
