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

# سطر تجريبي مؤقت للتأكد من ربط محرك الرسوم البيانية بنجاح
st.write("تم تحميل محرك الرسوم البيانية والجارتات بنجاح...")
