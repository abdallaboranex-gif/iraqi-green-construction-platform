import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. إعدادات الصفحة الكلية لتكون عريضة ومطابقة لأبعاد لوحات التحكم العالمية
st.set_page_config(page_title="Iraqi Green Construction Data Platform", page_icon="🏢", layout="wide")

# 2. حقن ثيم الـ CSS المتطور لصناعة البطاقات العائمة والظلال الناعمة والخطوط العصريّة
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* ضبط الخط والألوان الخلفية الكلية للمنصة */
    * {
        font-family: 'Tajawal', sans-serif !important;
    }
    .stApp {
        background-color: #F1F5F9 !important; /* الرمادي الفاتح الفخم المتواجد بالصورة */
    }
    
    /* تصميم البطاقات البيضاء العائمة ذات الحواف المستديرة والظلال الناعمة */
    .dashboard-card {
        background-color: #FFFFFF !important;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 18px rgba(15, 23, 42, 0.04);
        border: 1px solid rgba(226, 232, 240, 0.8);
        margin-bottom: 1rem;
    }
    
    /* تسميات مؤشرات الحالة (Status Badges) */
    .badge-completed {
        background-color: #DCFCE7; color: #15803D;
        padding: 4px 10px; border-radius: 20px; font-size: 0.85rem; font-weight: bold;
    }
    .badge-progress {
        background-color: #FFEDD5; color: #C2410C;
        padding: 4px 10px; border-radius: 20px; font-size: 0.85rem; font-weight: bold;
    }
    
    /* حاوية الإعلان الفاخر للاشتراك المدفوع باللون النيلي والتاج الذهبي */
    .premium-banner {
        background: linear-gradient(135deg, #0A2540 0%, #1E3A8A 100%);
        padding: 1.75rem;
        border-radius: 16px;
        color: white;
        box-shadow: 0 10px 25px rgba(10, 37, 64, 0.15);
        margin-top: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# =====================================================================
# 3. محرك الرسوم البيانية التفاعلية (Plotly Gauge & Trend Engine)
# =====================================================================

def draw_gauge_chart(percent, title, color):
    """رسم الدوائر البيانية الملونة لنسب الإنجاز والمطابقة"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = percent,
        number = {'suffix': "%", 'font': {'size': 20, 'family': 'Tajawal'}},
        title = {'text': title, 'font': {'size': 14, 'family': 'Tajawal', 'color': '#334155'}},
        gauge = {
            'axis': {'range':, 'tickwidth': 1, 'tickcolor': "#CBD5E1"},
            'bar': {'color': color},
            'bgcolor': "#E2E8F0",
            'borderwidth': 0,
        }
    ))
    fig.update_layout(
        margin=dict(l=10, r=10, t=40, b=10),
        height=140,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def draw_trend_chart():
    """رسم المخطط الانسيابي الأزرق لمؤشر الالتزام (Compliance Trend)"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    values = [45, 52, 48, 60, 72, 85]
    
    df = pd.DataFrame({'Month': months, 'Progress': values})
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Month'], y=df['Progress'],
        mode='lines+markers',
        line=dict(color='#2563EB', width=3),
        marker=dict(size=6, color='#1D4ED8'),
        fill='tozeroy',
        fillcolor='rgba(37, 99, 235, 0.08)'
    ))
    fig.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        height=120,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=True, gridcolor='#E2E8F0', zeroline=False)
    )
    return fig

# =====================================================================
# 4. نظام إدارة اللغات والهيدر العلوي الفاخر (Header & Identity Grid)
# =====================================================================

if "lang" not in st.session_state:
    st.session_state.lang = "ar"

# صف هيدر علوي لعرض اللوغو وزر تحويل اللغة الفوري
col_logo_area, col_lang_area = st.columns([3, 1])

with col_logo_area:
    st.image("assets/corporate_logo.jpeg")  # استدعاء لوغو الاستدامة الخضراء الأنيق

with col_lang_area:
    st.write("")
    if st.button("🌐 EN" if st.session_state.lang == "ar" else "🌐 العربية", use_container_width=True):
        st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"
        st.rerun()

lang = st.session_state.lang

# قاموس الترجمة الفورية الكامل لهيدر الواجهة الإستراتيجية
h_t = {
    "loc_title": {"ar": "📍 موقع المشروع الحالي:", "en": "📍 Current Project Location:"},
    "loc_val": {"ar": "بغداد", "en": "Baghdad"},
    "pm_title": {"ar": "👤 مدير المشروع:", "en": "👤 Project Manager:"},
    "pm_val": {"ar": "المهندس عبدالله علي", "en": "Eng. Abdulla Ali"},
}

# صف البيانات التعريفية (مقسم إلى 3 أعمدة عائمة مستديرة الحواف)
st.write("")
col_meta1, col_meta2, col_meta3 = st.columns(3)

with col_meta1:
    st.markdown(f"""
    <div class="dashboard-card" style="padding: 1rem; border-right: 4px solid #3B82F6;">
        <span style="color: #64748B; font-size: 0.9rem;">{h_t["loc_title"][lang]}</span><br>
        <strong style="color: #0F172A; font-size: 1.1rem;">{h_t["loc_val"][lang]}</strong>
    </div>
    """, unsafe_allow_html=True)

with col_meta2:
    st.markdown(f"""
    <div class="dashboard-card" style="padding: 1rem; border-right: 4px solid #10B981;">
        <span style="color: #64748B; font-size: 0.9rem;">{h_t["pm_title"][lang]}</span><br>
        <strong style="color: #0F172A; font-size: 1.1rem;">{h_t["pm_val"][lang]}</strong>
    </div>
    """, unsafe_allow_html=True)

with col_meta3:
    st.markdown(f"""
    <div class="dashboard-card" style="padding: 1rem; border-right: 4px solid #6366F1; text-align: center; background-color: #EEF2F6 !important;">
        <span style="color: #475569; font-size: 1rem; font-weight: bold;">Enterprise Portal v2.0</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# سطر تجريبي مؤقت للتأكد من ربط الهيدر واللغات بنجاح
st.write("تم تحميل الهيدر العلوي وصف الهوية بنجاح...")
