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

# سطر تجريبي مؤقت للتأكد من عمل الجزء الأول بنجاح
st.write("تم تحميل الثيم البصري بنجاح...")
