import streamlit as st
import plotly.graph_objects as go

# 1. إعدادات الصفحة وهوية المنصة البصرية
st.set_page_config(page_title="Iraqi Green Construction Data Platform", page_icon="🏗️", layout="wide")

# تصميم الأسلوب المرئي وحقن التنسيقات بشكل آمن ومتوافق مع تحديثات 2026
theme_css = """
<style>
    .stApp { background-color: #F8FAFC !important; }
    .header-box { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; height: 100%; }
    .step-box { border: 1px solid #E2E8F0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #F8FAFC; }
    .step-active { border: 1px solid #FFEDD5; background-color: #FFFFf0; border-left: 5px solid #F97316; }
    .premium-box { background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%); color: white; padding: 20px; border-radius: 12px; margin-top: 20px; }
    .green-text { color: #059669; font-weight: bold; }
    .gray-text { color: #64748B; }
    .completed-badge { float: right; background-color: #D1FAE5; color: #065F46; padding: 2px 8px; border-radius: 12px; font-size: 12px; }
    .progress-badge { float: right; background-color: #FFEDD5; color: #9A3412; padding: 2px 8px; border-radius: 12px; font-size: 12px; }
</style>
"""
st.html(theme_css)

# 2. الهيدر العلوي (Header) مبرمج بدوال نظيفة خالية من الـ HTML المتعارض
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

# 3. تقسيم الشاشة الرئيسي (يسار: الخطوات / يمين: المؤشرات الإحصائية)
col_left, col_right = st.columns(2)

# --- الجانب الأيسر: الخطوات والمراحل الإنشائية ---
with col_left:
    st.markdown("#### 🔵 PHASE 1 : Engineering Compliance `Strict Sequential Order`")
    
    # الخطوة 1: مكتملة
    st.html("""
    <div class="step-box">
        <span style="color:#059669; font-weight:bold;">🟢 Step 1: Site Analysis & Zoning Regulations</span> 
        <span class="completed-badge">Completed</span>
        <p style="color:#64748B; font-size:13px; margin-top:5px;">Completed on 15 May 2025 • by Eng. Abdulla</p>
    </div>
    """)
    
    # الخطوة 2: قيد العمل وبها ميزة رفع الملفات التفاعلية
    st.markdown('<div class="step-box step-active">', unsafe_allowed_html=True)
    st.html("<span style='color:#F97316; font-weight:bold;'>¼ Step 2: Soil Inspection & Foundations</span> <span class='progress-badge'>In Progress</span>")
    uploaded_file = st.file_uploader("Upload (Soil Lab PDF) - Max 50MB", type=["pdf"], label_visibility="visible")
    st.markdown('</div>', unsafe_allowed_html=True)
    
    # الخطوات 3 و 4 و 5: مقفلة (Locked)
    steps_data = [
        ("3", "Structural Audit & Load Calculations"),
        ("4", "Hydro-Sanitary & Plumbing Design"),
        ("5", "Electrical Systems Analysis")
    ]
    for num, title in steps_data:
        html_code = f"""
        <div class="step-box" style="opacity: 0.6;">
            <span style="color:#64748B;">🔒 Step {num}: {title}</span>
        </div>
        """
        st.html(html_code)
        
    # بنر الترقية للنسخة المدفوعة (Premium Subscription)
    st.html("""
    <div class="premium-box">
        <h5>👑 Subscribe to Premium Pack <span style="background-color:#EAB308; color:black; padding:2px 6px; border-radius:4px; font-size:11px; font-weight:bold;">PREMIUM</span></h5>
        <p style="font-size:13px; color:#94A3B8;">Unlock all 14 automated compliance calculators, process soil lab data via AI, and generate legally verified PDF audit reports.</p>
        <button style="background-color:#EAB308; border:none; color:black; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">Upgrade Now 👑</button>
    </div>
    """)


# --- الجانب الأيمن: المؤشرات والرسوم البيانية (KPI Cards) ---
with col_right:
    
    # صف المؤشرات الأول (Engineering Compliance & Structural Integrity)
    r1_c1, r1_c2 = st.columns(2)
    
    with r1_c1:
        st.markdown('<div class="card">', unsafe_allowed_html=True)
        st.markdown("<h6>🔵 1. Engineering Compliance</h6>", unsafe_allowed_html=True)
        st.markdown("<h3 style='margin-bottom:0;'>42%</h3><p style='color:#64748B; font-size:12px;'>Overall Progress</p>", unsafe_allowed_html=True)
        # رسم بياني خطي صغير للتطور التراكمي للبيانات
        fig_line = go.Figure(go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], y=[20, 25, 30, 45, 60, 75], mode='lines+markers', line=dict(color='#2563EB', width=2)))
        fig_line.update_layout(margin=dict(l=10,r=10,t=10,b=10), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_line, use_container_width=True, key="compliance_chart")
        st.markdown('</div>', unsafe_allowed_html=True)
        
    with r1_c2:
        st.markdown('<div class="card">', unsafe_allowed_html=True)
        st.markdown("<h6>🟢 2. Structural Integrity</h6>", unsafe_allowed_html=True)
        st.markdown("<h3 style='margin-bottom:0;'>0%</h3><p style='color:#64748B; font-size:12px;'>Overall Progress</p>", unsafe_allowed_html=True)
        # رسم بياني أعمدة لحالة الهيكل الإنشائي
        fig_bar = go.Figure(go.Bar(x=['Mar', 'Apr', 'May', 'Jun'], y=[0, 10, 40, 90], marker_color='#10B981'))
        fig_bar.update_layout(margin=dict(l=10,r=10,t=10,b=10), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_bar, use_container_width=True, key="structural_chart")
        st.markdown('</div>', unsafe_allowed_html=True)

    # صف المؤشرات الثاني (Energy Optimization & Sustainability Impact)
    r2_c1, r2_c2 = st.columns(2)
    
    with r2_c1:
        st.markdown('<div class="card">', unsafe_allowed_html=True)
        st.markdown("<h6>🟢 3. Energy Optimization</h6>", unsafe_allowed_html=True)
        st.markdown("<h3 style='margin-bottom:0;'>0%</h3><p style='color:#64748B; font-size:12px;'>Overall Progress</p>", unsafe_allowed_html=True)
        st.markdown("<span style='color:#059669; font-weight:bold;'>27%</span> <span style='font-size:12px; color:#64748B;'>Estimated Savings</span>", unsafe_allowed_html=True)
        st.markdown('</div>', unsafe_allowed_html=True)
        
    with r2_c2:
        st.markdown('<div class="card">', unsafe_allowed_html=True)
        st.markdown("<h6>🟢 4. Sustainability Impact</h6>", unsafe_allowed_html=True)
        st.markdown("<h3 style='margin-bottom:0; color:#059669;'>61</h3><p style='color:#64748B; font-size:12px;'>Green Score</p>", unsafe_allowed_html=True)
        st.markdown("<span style='font-size:12px; color:#64748B;'>CO₂ Reduction Potential:</span><br><span style='font-weight:bold; color:#059669;'>128.5 Tons/Year</span>", unsafe_allowed_html=True)
        st.markdown('</div>', unsafe_allowed_html=True)

    # صف المؤشرات الثالث (Cost Management & Project Timeline)
    r3_c1, r3_c2 = st.columns(2)
    
    with r3_c1:
        st.markdown('<div class="card">', unsafe_allowed_html=True)
        st.markdown("<h6>🟣 5. Cost Management</h6>", unsafe_allowed_html=True)
        st.markdown("<h3>18%</h3>", unsafe_allowed_html=True)
        st.progress(0.18)
        st.markdown("<p style='font-size:12px; color:#64748B; margin-top:5px;'>Budget Overview:<br><b>$1.28M</b> / $7.00M</p>", unsafe_allowed_html=True)
        st.markdown('</div>', unsafe_allowed_html=True)
        
    with r3_c2:
        st.markdown('<div class="card">', unsafe_allowed_html=True)
        st.markdown("<h6>🔵 6. Project Timeline</h6>", unsafe_allowed_html=True)
        st.markdown("<h3>14%</h3>", unsafe_allowed_html=True)
        st.progress(0.14)
        st.markdown("<p style='font-size:12px; color:#64748B; margin-top:5px;'>Project Duration:<br><b>42</b> / 300 Days</p>", unsafe_allowed_html=True)
        st.markdown('</div>', unsafe_allowed_html=True)

st.markdown("---")

# 4. شريط الميزات السفلي الفوتر (Footer Features)
f1, f2, f3, f4 = st.columns(4)
f1.markdown("🛡️ **Secure & Sovereign**")
f1.caption("End-to-end data protection with local compliance")

f2.markdown("🧠 **AI-Powered Analytics**")
f2.caption("Smarter insights for better construction decisions")

f3.markdown("✅ **Regulatory Compliance**")
f3.caption("Aligned with national & international green building standards")

f4.markdown("🎧 **Expert Support**")
f4.caption("Dedicated engineering support team")
