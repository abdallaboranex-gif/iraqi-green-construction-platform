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
        /* إلغاء حواف وهوامش السايدبار والصفحة الافتراضية الجافة لجعلها ممتدة واحترافية */
        [data-testid="stSidebarNav"], [data-testid="collapsedControl"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        .main .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1.5rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 100% !important;
        }
        
        /* ضبط خلفية عامة للمنصة باللون الرمادي الخفيف جداً الفاخر كما في صورتك المرجعية */
        body, .main {
            background-color: #F8FAFC !important;
        }
        
        /* تنسيق أزرار التنقل الرأسية للبوابات الست لتصبح كروت تفاعلية مخصصة (Custom Nav Cards) */
        div.stButton > button {
            background-color: white !important;
            color: #4B5563 !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 12px !important;
            padding: 14px 18px !important;
            font-size: 0.92rem !important;
            font-weight: 600 !important;
            text-align: right !important;
            display: flex !important;
            align-items: center !important;
            justify-content: flex-start !important;
            gap: 12px !important;
            box-shadow: 0 1px 2px rgba(0,0,0,0.02) !important;
            transition: all 0.25s ease !important;
            margin-bottom: 8px !important;
            height: auto !important;
        }
        
        /* تلوين الزر النشط باللون الأزرق الملكي والفخم لتأمين البوابة المحددة */
        div.stButton > button[type="primary"] {
            background-color: #EFF6FF !important;
            color: #1E3A8A !important;
            border: 1px solid #3B82F6 !important;
            box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.08) !important;
        }
        
        /* تأثيرات التحويم المريحة للعين للمدقق البلدي */
        div.stButton > button:hover {
            border-color: #3B82F6 !important;
            color: #1E3A8A !important;
            background-color: #F0FDF4 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
        }
        
        /* تحسين وتنعيم حقول الإدخال وصناديق الفلترة لستريملت بالمنتصف */
        .stSelectbox, .stNumberInput, .stTextInput {
            background-color: white !important;
            border-radius: 10px !important;
        }
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

# 6. فتح التوزيع الثلاثي المتوازن للأبعاد الكبرى (اليسار للبوابات، الوسط للخطوات والفلترة، اليمين للمؤشرات الحية)
col_left_nav, col_center_stage, col_right_stats = st.columns([1.1, 1.7, 1.2], gap="large")

# ==================== 1️⃣ الجانب الأيسر: قائمة التنقل الاستراتيجية للبوابات الست المخصصة ====================
with col_left_nav:
    st.markdown(f"""
        <div style='margin-bottom: 12px; border-bottom: 2px solid #E2E8F0; padding-bottom: 6px; text-align: {align};'>
            <b style='color: #1E3A8A; font-size: 1.05rem;'>🛠️ {'بوابات التحكم والمنظومة' if lang == 'AR' else 'Control & Platform Gates'}</b>
        </div>
    """, unsafe_allow_html=True)
    
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

# ==================== 2️⃣ القطاع الأوسط الحركي: عرض شاشة البوابة المحددة بنظام التبديل ====================
with col_center_stage:
    current_gate = st.session_state["active_gate"]
    
    if current_gate == "gate_1":
        render_steps_and_calculators(L, lang)
        
    elif current_gate == "gate_2":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);'><h3>{L['gate_2_title']}</h3><p style='color:#6B7280;'>🌱 حاسبات العزل الحراري وكفاءة استهلاك الطاقة والبصمة الكربونية للمواد قيد المعايرة الكودية الحية...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_3":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);'><h3>{L['gate_3_title']}</h3><p style='color:#6B7280;'>📊 لوحة الرسوم البيانية الإحصائية لنسب القبول والرفض الكودي قيد الهندسة المركزية للبيانات...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_4":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);'><h3>{L['gate_4_title']}</h3><p style='color:#6B7280;'>🗺️ <b>خارطة العراق الرقمية السيادية:</b> يتم الآن ربط قواعد البيانات الجغرافية (GIS) لتتبع انتشار المشاريع رخص البناء في كل قضاء وبلدية وناحية حياً...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_5":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);'><h3>{L['gate_5_title']}</h3><p style='color:#6B7280;'>💳 بوابة البنية التحتية للاشتراكات، الدفع الإلكتروني الحكومي لإجازات البناء وسوق مواد البناء المستدامة وتأمين حماية البيانات السيادية...</p></div>", unsafe_allow_html=True)
        
    elif current_gate == "gate_6":
        st.markdown(f"<div style='background-color: white; padding: 25px; border-radius: 16px; border: 1px solid #E5E7EB; text-align: {align}; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);'><h3>{L['gate_6_title']}</h3><p style='color:#6B7280;'>📷 <b>منظومة التفتيش الرقمي الميداني:</b> قطاع استقبال صور وفيديوهات الكشف الميداني للبلديات لمطابقة تقدم التنفيذ الفعلي على أرض الواقع...</p></div>", unsafe_allow_html=True)

# ==================== 3️⃣ الجانب الأيمن: لوحة التحليلات والمؤشرات المركزية والطقس الحي العراقي ====================
with col_right_stats:
    render_sidebar_analytics(L, lang)
