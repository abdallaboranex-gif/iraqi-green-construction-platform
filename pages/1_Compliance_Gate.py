# pages/1_Compliance_Gate.py
import streamlit as st

# 1. إعداد الصفحة وقفل وإغلاق الشريط الجانبي الافتراضي تلقائياً فور الفتح
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform", 
    layout="wide",
    initial_sidebar_state="collapsed"  # تجميد ومنع ظهور السايدبار الرمادي الافتراضي
)

# 2. حجب وحذف زر الأسهم (<<) وقائمة التنقل الافتراضية نهائياً من جذورها لتطابق صورتك
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
        section[data-testid="stSidebar"] {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# 3. إرساء وتأمين قيم الذاكرة الافتتاحية للمنصة في الجلسة الحية لمنع الـ KeyError
if "lang" not in st.session_state:
    st.session_state["lang"] = "AR"
if "active_gate" not in st.session_state:
    st.session_state["active_gate"] = "gate_1"
if "compliance_rate" not in st.session_state:
    st.session_state["compliance_rate"] = 42
if "step2_status" not in st.session_state:
    st.session_state["step2_status"] = "In Progress"

# 4. استدعاء الترويسة والمكونات الهندسية من مجلد الـ components
from components.header import render_header
from components.steps_view import render_steps_and_calculators
from components.sidebar_metrics import render_sidebar_analytics

# 5. رسم الترويسة العلوية للمنصة وجلب قاموس اللغة المباشر
L = render_header()
lang = st.session_state["lang"]
align = "right" if lang == "AR" else "left"

# 6. فتح التوزيع الثلاثي المتوازن للشاشة (اليمين للتحليلات، الوسط للشاشات الفنية، اليسار للبوابات الست)
col_left_nav, col_center_stage, col_right_stats = st.columns([1.1, 1.6, 1.2], gap="large")

# ==================== 1️⃣ الجانب الأيسر: قائمة التنقل الاستراتيجية للبوابات الست ====================
with col_left_nav:
    st.markdown(f"<h5 style='color: #1F2937; text-align: {align};'>🛠️ {'بوابات التحكم والمنظومة' if lang == 'AR' else 'Control & Platform Gates'}</h5>", unsafe_allow_html=True)
    
    if st.button(L['gate_1_title'], use_container_width=True, type="primary" if st.session_state["active_gate"] == "gate_1" else "secondary"):
        st.session_state["active_gate"] = "gate_1"
        st.rerun()
        
    if st.button(L['gate_2_title'], use_container_width=True, type="primary" if st.session_state["active_gate"] == "gate_2" else "secondary"):
        st.session_state["active_gate"] = "gate_2"
        st.rerun()
        
    if st.button(L['gate_3_title'], use_container_width=True, type="primary" if st.session_state["active_gate"] == "gate_3" else "secondary"):
        st.session_state["active_gate"] = "gate_3"
        st.rerun()
        
    if st.button(L['gate_4_title'], use_container_width=True, type="primary" if st.session_state["active_gate"] == "gate_4" else "secondary"):
        st.session_state["active_gate"] = "gate_4"
        st.rerun()
        
    if st.button(L['gate_5_title'], use_container_width=True, type="primary" if st.session_state["active_gate"] == "gate_5" else "secondary"):
        st.session_state["active_gate"] = "gate_5"
        st.rerun()
        
    if st.button(L['gate_6_title'], use_container_width=True, type="primary" if st.session_state["active_gate"] == "gate_6" else "secondary"):
        st.session_state["active_gate"] = "gate_6"
        st.rerun()

# ==================== 2️⃣ القطاع الأوسط الحركي: عرض شاشة البوابة المحددة ====================
with col_center_stage:
    current_gate = st.session_state["active_gate"]
    
    if current_gate == "gate_1":
        render_steps_and_calculators(L, lang)
        
    elif current_gate == "gate_2":
        st.markdown(f"<div style='text-align: {align};'><h3>{L['gate_2_title']}</h3><p>⏳ حاسبات العزل الحراري وكفاءة استهلاك الطاقة والبصمة الكربونية قيد المعايرة الكودية...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_3":
        st.markdown(f"<div style='text-align: {align};'><h3>{L['gate_3_title']}</h3><p>⏳ لوحة الرسوم البيانية الإحصائية لنسب القبول والرفض الكودي قيد الهندسة للبيانات...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_4":
        st.markdown(f"<div style='text-align: {align};'><h3>{L['gate_4_title']}</h3><p>🗺️ <b>خارطة العراق الرقمية السيادية:</b> يتم الآن ربط قواعد البيانات الجغرافية (GIS) لتتبع انتشار المشاريع في كل قضاء وبلدية...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_5":
        st.markdown(f"<div style='text-align: {align};'><h3>{L['gate_5_title']}</h3><p>⏳ بوابة الدفع الإلكتروني الحكومي وسوق مواد البناء المستدامة وتأمين حماية البيانات...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_6":
        st.markdown(f"<div style='text-align: {align};'><h3>{L['gate_6_title']}</h3><p>📷 <b>منظومة التفتيش الرقمي الميداني:</b> قطاع استقبال صور وفيديوهات الكشف البلدي الموقعي لمطابقة تقدم التنفيذ الفعلي...</p></div>", unsafe_allow_html=True)

# ==================== 3️⃣ الجانب الأيمن: لوحة التحليلات والمؤشرات المركزية والطقس الحي ====================
with col_right_stats:
    render_sidebar_analytics(L, lang)
