# pages/1_Compliance_Gate.py
import streamlit as st

# 1. إعداد الصفحة وتجميد السايدبار الافتراضي فوراً ومنع تمدد الشاشة المفرط
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. حقن الـ CSS المركزي المتقدم لقلب هوية ستريملت ومطابقة الصورة طبق الأصل
st.markdown("""
    <style>
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        .main .block-container { padding: 1.5rem 2rem !important; max-width: 100% !important; }
        body, .main { background-color: #F8FAFC !important; }
        div.stButton > button {
            background-color: white !important; color: #4B5563 !important;
            border: 1px solid #E5E7EB !important; border-radius: 12px !important;
            padding: 14px 18px !important; font-size: 0.92rem !important;
            font-weight: 600 !important; text-align: right !important;
            display: flex !important; align-items: center !important;
            justify-content: flex-start !important; gap: 12px !important;
            margin-bottom: 8px !important; transition: all 0.25s ease !important;
        }
        div.stButton > button[type="primary"] { background-color: #EFF6FF !important; color: #1E3A8A !important; border: 1px solid #3B82F6 !important; }
        div.stButton > button:hover { border-color: #3B82F6 !important; color: #1E3A8A !important; background-color: #F0FDF4 !important; transform: translateY(-1px) !important; }
        .stSelectbox, .stNumberInput, .stTextInput { background-color: white !important; border-radius: 10px !important; }
    </style>
""", unsafe_allow_html=True)

# 3. تأمين قيم الذاكرة الافتتاحية للمنصة في الجلسة الحية لمنع الـ KeyError
if "lang" not in st.session_state: st.session_state["lang"] = "AR"
if "active_gate" not in st.session_state: st.session_state["active_gate"] = "gate_1"
if "compliance_rate" not in st.session_state: st.session_state["compliance_rate"] = 42
if "step2_status" not in st.session_state: st.session_state["step2_status"] = "In Progress"

# 4. استدعاء الترويسة ومكونات المنصة الهندسية الكبرى من مساراتها النظيفة
from components.header import render_header
from components.steps_view import render_steps_and_calculators
from components.sidebar_metrics import render_sidebar_analytics
from components.gate2_sustainability import render_sustainability_gate
# استدعاء واجهة البوابة الثالثة الإحصائية المعزولة والمحميّة حديثاً بالملي
from components.gate3.gate3_main import render_analytics_gate

L = render_header()
lang = st.session_state["lang"]
align = "right" if lang == "AR" else "left"
direction = "rtl" if lang == "AR" else "ltr"

col_left_nav, col_center_stage, col_right_stats = st.columns([1.1, 1.7, 1.2], gap="large")

# ==================== 1️⃣ الجانب الأيسر: قائمة التنقل الاستراتيجية للبوابات الست ====================
with col_left_nav:
    st.markdown(f"<div style='margin-bottom: 12px; border-bottom: 2px solid #E2E8F0; padding-bottom: 6px; text-align: {align};'><b style='color: #1E3A8A; font-size: 1.05rem;'>🛠️ {'بوابات التحكم والمنظومة' if lang == 'AR' else 'Control Gates'}</b></div>", unsafe_allow_html=True)
    for g_id, g_title in [("gate_1", L['gate_1_title']), ("gate_2", L['gate_2_title']), ("gate_3", L['gate_3_title']), ("gate_4", L['gate_4_title']), ("gate_5", L['gate_5_title']), ("gate_6", L['gate_6_title'])]:
        if st.button(g_title, use_container_width=True, type="primary" if st.session_state["active_gate"] == g_id else "secondary", key=f"btn_nav_{g_id}"):
            st.session_state["active_gate"] = g_id
            st.rerun()

# ==================== 2️⃣ القطاع الأوسط الحركي: عرض شاشة البوابة المحددة ====================
with col_center_stage:
    current_gate = st.session_state["active_gate"]
    if current_gate == "gate_1":
        render_steps_and_calculators(L, lang)
    elif current_gate == "gate_2":
        render_sustainability_gate(L, lang, direction, align)
    elif current_gate == "gate_3":
        # تشغيل واستدعاء لوحة التحليلات والإحصائيات البيانية المستقلة للبوابة الثالثة
        render_analytics_gate(L, lang, direction, align)
    elif current_gate == "gate_4":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align};'><h3>{L['gate_4_title']}</h3><p style='color:#6B7280;'>🗺️ <b>خارطة العراق الرقمية:</b> جاري ربط قواعد البيانات الجغرافية GIS...</p></div>", unsafe_allow_html=True)
    elif current_gate == "gate_5":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align};'><h3>{L['gate_5_title']}</h3><p style='color:#6B7280;'>💳 بوابة البنية التحتية للاشتراكات والدفع الإلكتروني الحكومي...</p></div>", unsafe_allow_html=True)
    elif current_gate == "gate_6":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align};'><h3>{L['gate_6_title']}</h3><p style='color:#6B7280;'>📷 منظومة التفتيش الرقمي الميداني واستقبال صور الكشف البلدي الموقعي...</p></div>", unsafe_allow_html=True)

# ==================== 3️⃣ الجانب الأيمن: لوحة التحليلات والمؤشرات المركزية والطقس الحي ====================
with col_right_stats:
    render_sidebar_analytics(L, lang)
