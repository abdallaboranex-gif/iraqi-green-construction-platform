# pages/1_Compliance_Gate.py
import streamlit as st

# 1. تجميد السايدبار الافتراضي للتحكم بهوية وأبعاد المنصة السيادية حياً
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. حقن الـ CSS المركزي المتقدم لقلب هوية ستريملت ومطابقة الأبعاد بالملي
# components/steps_view.py
import streamlit as st

def render_steps_and_calculators(L, lang):
    """منظومة الخطوات التتابعية بأمان بايثون الصافي 100%"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"

    # تقسيم الشاشة لخمسة أعمدة صغيرة متوازية لتمثيل الـ 5 خطوات
    s_col1, s_col2, s_col3, s_col4, s_col5 = st.columns(5)
    with s_col1:
        st.info("✓ الخطوة 1" if lang=="AR" else "✓ Step 1")
    with s_col2:
        st.success("⏳ الخطوة 2" if lang=="AR" else "⏳ Step 2")
    with s_col3:
        st.text("🔒 الخطوة 3" if lang=="AR" else "🔒 Step 3")
    with s_col4:
        st.text("🔒 الخطوة 4" if lang=="AR" else "🔒 Step 4")
    with s_col5:
        st.text("🔒 الخطوة 5" if lang=="AR" else "🔒 Step 5")

    st.markdown("---")
    
    # حقول الإدخال والمقاييس لـ (الخطوة 1) تبدأ مباشرة هنا بالسطر التالي
    with st.container(border=True):
        st.markdown(f"<div style='text-align: {align}; font-weight: bold; color: #1E293B; margin-bottom: 12px;'>📋 معطيات الموقع والمحددات الحالية:</div>", unsafe_allow_html=True)

# 3. تأمين قيم الذاكرة الافتتاحية للمنصة في الجلسة الحية لمنع الـ KeyError
if "lang" not in st.session_state: st.session_state["lang"] = "AR"
if "active_gate" not in st.session_state: st.session_state["active_gate"] = "gate_1"
if "compliance_rate" not in st.session_state: st.session_state["compliance_rate"] = 42
if "step2_status" not in st.session_state: st.session_state["step2_status"] = "In Progress"

# 4. استدعاء الترويسة ومكونات المنصة الهندسية الكبرى من مساراتها المفرزة النظيفة
from components.header import render_header
from components.steps_view import render_steps_and_calculators
from components.sidebar_metrics import render_sidebar_analytics
# تحديث مسار استدعاء البوابة الثانية لتشير إلى المجلد المفرز الجديد
from components.gate2.gate2_sustainability import render_sustainability_gate
from components.gate3.gate3_main import render_analytics_gate
from components.gate4.gate4_main import render_sovereign_map_gate
from components.gate5.gate5_main import render_billing_gate
from components.gate6.gate6_main import render_safety_inspection_gate

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

# ==================== 2️⃣ القطاع الأوسط الحركي: عرض شاشة البوابة المحددة حياً ====================
with col_center_stage:
    current_gate = st.session_state["active_gate"]
    if current_gate == "gate_1":
        render_steps_and_calculators(L, lang)
    elif current_gate == "gate_2":
        render_sustainability_gate(L, lang, direction, align)
    elif current_gate == "gate_3":
        render_analytics_gate(L, lang, direction, align)
    elif current_gate == "gate_4":
        render_sovereign_map_gate(L, lang, direction, align)
    elif current_gate == "gate_5":
        render_billing_gate(L, lang, direction, align)
    elif current_gate == "gate_6":
        # تفعيل واستدعاء البوابة السادسة والأخيرة: التفتيش الرقمي والسلامة الموقعية حياً
        render_safety_inspection_gate(L, lang, direction, align)

# ==================== 3️⃣ الجانب الأيمن: لوحة التحليلات والمؤشرات المركزية والطقس الحي ====================
with col_right_stats:
    render_sidebar_analytics(L, lang)

# --- كود جرد وتفتيش شجرة ملفات المشروع حياً (اسحبه بعد المراجعة) ---
st.markdown("---")
st.markdown("### 🔍 **شجرة ملفات ومسارات المشروع الحالية حياً:**")

import os
def get_project_tree(startpath="."):
    tree_str = ""
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['venv', '__pycache__', '.git']]
        level = root.replace(startpath, '').count(os.sep)
        indent = '&nbsp;' * 6 * level
        tree_str += f"{indent} 📁 <b>{os.path.basename(root)}/</b><br>"
        for f in files:
            if not f.startswith('.'):
                file_indent = '&nbsp;' * 6 * (level + 1)
                tree_str += f"{file_indent} 📄 {f}<br>"
    return tree_str

st.markdown(f"<div style='background-color: #0F172A; color: #10B981; padding: 15px; border-radius: 12px; font-family: monospace; font-size: 0.9rem;'>{get_project_tree()}</div>", unsafe_allow_html=True)
