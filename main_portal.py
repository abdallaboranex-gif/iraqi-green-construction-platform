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
# =====================================================================
# 5. قاموس الترجمة الشامل للأزرار والكتل الاستراتيجية الـ 14
# =====================================================================
p_t = {
    "left_title": {"ar": "🔷 خط الإنتاج المتسلسل لمطابقة الكودات والأمان (Strict Pipeline)", "en": "🔷 Engineering Compliance & Safety (Strict Sequential Pipeline)"},
    "right_title": {"ar": "📊 المؤشرات والتحليلات الاستراتيجية الحية للشركة (SaaS Dashboard)", "en": "📊 Live Enterprise Analytics & System Dashboards (SaaS Dashboard)"},
    
    # المحور الأول
    "step1": {"ar": "✅ الخطوة 1: تحليل الموقع والمحددات البلدية (مفتوح للتجربة) ➔", "en": "✅ Step 1: Site Analysis & Zoning Regulations (Open for Demo) ➔"},
    "step2": {"ar": "🧪 الخطوة 2: فحص التربة وتصميم الأسس 🔒", "en": "🧪 Step 2: Soil Inspection & Foundations 🔒"},
    "step3": {"ar": "🧱 الخطوة 3: التدقيق الإنشائي وحساب الأحمال والسلامة 🔒", "en": "🧱 Step 3: Structural Audit & Load Calculations 🔒"},
    "step4": {"ar": "🚰 الخطوة 4: هندسة التأسيسات الصحية والمائية 🔒", "en": "🚰 Step 4: Hydro-Sanitary & Plumbing Design 🔒"},
    "step5": {"ar": "⚡ الخطوة 5: هندسة التأسيسات الكهربائية وموازنة الأحمال 🔒", "en": "⚡ Step 5: Electrical Systems Analysis 🔒"},
    
    # المحور الثاني
    "step6": {"ar": "❄️ الخطوة 6: حسابات العزل الحراري وغلاف المبنى 🔒", "en": "❄️ Step 6: Thermal Insulation & Building Envelope 🔒"},
    "step7": {"ar": "💨 الخطوة 7: تخمين أحمال التكييف وتصميم المنظومات 🔒", "en": "💨 Step 7: HVAC Load Estimation & System Design 🔒"},
    "step8": {"ar": "💰 الخطوة 8: حاسبة كلف التشغيل وفترة استرداد رأس المال 🔒", "en": "💰 Step 8: Operational Cost & ROI Calculator 🔒"},
    
    # كتل الاشتراكات وباقي الخدمات
    "premium_title": {"ar": "👑 اشترك في الباقة الفاخرة لتفعيل الـ 14 برنامجاً بالكامل", "en": "👑 Subscribe to Premium Pack (PREMIUM)"},
    "premium_desc": {"ar": "قم بفتح كافة الحواسب والمحركات البرمجية والتدقيق الذكي، مع إصدار شهادات الـ PDF المشفرة بالـ QR وصحة الصدور.", "en": "Unlock all 14 automated compliance calculators, process soil lab data via AI, and generate legally verified PDF audit reports with secure QR Code verification."},
    "premium_btn": {"ar": "الاشتراك الآن ⚡", "en": "Upgrade Now 👑"},
}

# =====================================================================
# 6. تقسيم وتوزيع فضاء الشاشة الكلية إلى العمودين الرئيسيين
# =====================================================================
col_left_main, col_right_main = st.columns([1.1, 0.9]) # توزيع هندسي متوازن بالملي 

with col_left_main:
    st.markdown(f"### {p_t['left_title'][lang]}")
    
    # عرض خط إنتاج المحور الأول
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    prog1 = st.button(p_t["step1"][lang], use_container_width=True)
    prog2 = st.button(p_t["step2"][lang], use_container_width=True)
    prog3 = st.button(p_t["step3"][lang], use_container_width=True)
    prog4 = st.button(p_t["step4"][lang], use_container_width=True)
    prog5 = st.button(p_t["step5"][lang], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # عرض خط إنتاج المحور الثاني
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    prog6 = st.button(p_t["step6"][lang], use_container_width=True)
    prog7 = st.button(p_t["step7"][lang], use_container_width=True)
    prog8 = st.button(p_t["step8"][lang], use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # حاوية وبانر الاشتراك المالي المدفوع للشركة وحماية الأرباح
    st.markdown(f"""
    <div class="premium-banner">
        <h3 style="color: white; margin-top: 0;">{p_t["premium_title"][lang]}</h3>
        <p style="color: #93C5FD; font-size: 0.95rem;">{p_t["premium_desc"][lang]}</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.button(p_t["premium_btn"][lang], type="primary", use_container_width=True)

with col_right_main:
    st.markdown(f"### {p_t['right_title'][lang]}")
    
    # سطر تجريبي مؤقت بداخل العمود الأيمن سيتم ملؤه بالعدادات الستة فوراً في الجزء القادم
    st.write("فضاء العدادات والمؤشرات الستة الملونة جاهز للاستقبال...")
