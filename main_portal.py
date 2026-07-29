import streamlit as st
import plotly.graph_objects as go

# 1. إعدادات الصفحة وهوية المنصة البصرية القياسية
st.set_page_config(page_title="Iraqi Green Construction Data Platform", page_icon="🏗️", layout="wide")

# تطبيق كود التنسيق الهيكلي (CSS) باستخدام الدالة الرسمية والآمنة لتحديثات بايثون 3.14
theme_css = """
<style>
    .stApp { background-color: #F8FAFC !important; }
    .header-box { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; height: 100%; }
    .step-box { border: 1px solid #E2E8F0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #F8FAFC; }
    .step-active { border: 1px solid #FFEDD5; background-color: #FFFFf0; border-left: 5px solid #F97316; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
    .premium-box { background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%); color: white; padding: 20px; border-radius: 12px; margin-top: 20px; }
    .green-text { color: #059669; font-weight: bold; }
    .gray-text { color: #64748B; }
    .completed-badge { float: right; background-color: #D1FAE5; color: #065F46; padding: 2px 8px; border-radius: 12px; font-size: 12px; }
    .progress-badge { float: right; background-color: #FFEDD5; color: #9A3412; padding: 2px 8px; border-radius: 12px; font-size: 12px; }
    .card-title { font-weight: bold; margin-bottom: 5px; color: #1E293B; }
    .card-value { font-size: 28px; font-weight: bold; margin: 0; color: #0F172A; }
</style>
"""
st.html(theme_css)

# 2. الهيدر العلوي للمنصة (Header Columns)
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

# 3. تخطيط الصفحة الرئيسي المتوازن (يسار: مسار العمليات / يمين: المؤشرات)
col_left, col_right = st.columns(2)

# --- الجانب الأيسر: المراحل والخطوات التتابعية للمشروع ---
with col_left:
    st.markdown("#### 🔵 PHASE 1 : Engineering Compliance `Strict Sequential Order`")
    
    # الخطوة 1: مكتملة (تم الرفع والتوثيق)
    st.html("""
    <div class="step-box">
        <span style="color:#059669; font-weight:bold;">🟢 Step 1: Site Analysis & Zoning Regulations</span> 
        <span class="completed-badge">Completed</span>
        <p style="color:#64748B; font-size:13px; margin-top:5px;">Completed on 15 May 2025 • by Eng. Abdulla</p>
    </div>
    """)
    
    # الخطوة 2: قيد العمل وبها ميزة رفع مستندات التربة والأسس تفاعلياً بدون تعارض HTML
    with st.container():
        st.html("<div class='step-active'><span style='color:#F97316; font-weight:bold;'>🟠 Step 2: Soil Inspection & Foundations</span> <span class='progress-badge'>In Progress</span></div>")
        uploaded_file = st.file_uploader("Upload (Soil Lab PDF) - Max 50MB", type=["pdf"], label_visibility="visible")
    
    # الخطوات 3 و 4 و 5: مقفلة ومؤمنة بالنظام (Locked)
    steps_data = [
        ("3", "Structural Audit & Load Calculations"),
        ("4", "Hydro-Sanitary & Plumbing Design"),
        ("5", "Electrical Systems Analysis")
    ]
    for num, title in steps_data:
        st.html(f"""
        <div class="step-box" style="opacity: 0.6;">
            <span style="color:#64748B;">🔒 Step {num}: {title}</span>
        </div>
        """)
        
    # بنر الترقية والاشتراكات السحابية المدفوعة (Premium Subscription Pack)
    st.html("""
    <div class="premium-box">
        <h5>👑 Subscribe to Premium Pack <span style="background-color:#EAB308; color:black; padding:2px 6px; border-radius:4px; font-size:11px; font-weight:bold;">PREMIUM</span></h5>
        <p style="font-size:13px; color:#94A3B8;">Unlock all 14 automated compliance calculators, process soil lab data via AI, and generate legally verified PDF audit reports.</p>
        <button style="background-color:#EAB308; border:none; color:black; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">Upgrade Now 👑</button>
    </div>
    """)


# --- الجانب الأيمن: لوحات قياس المؤشرات والرسوم البيانية التفاعلية (KPI Cards) ---
with col_right:
    
    # الصف الأول للمؤشرات
    r1_c1, r1_c2 = st.columns(2)
    
    with r1_c1:
        with st.container(border=True):
            st.html("<div class='card-title'>🔵 1. Engineering Compliance</div>")
            st.html("<div class='card-value'>42%</div><p style='color:#64748B; font-size:12px;'>Overall Progress</p>")
            fig_line = go.Figure(go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], y=[10, 15, 22, 28, 35, 42], mode='lines+markers', line=dict(color='#2563EB', width=2)))
            fig_line.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_line, use_container_width=True, key="compliance_chart", config={'displayModeBar': False})
        
    with r1_c2:
        with st.container(border=True):
            st.html("<div class='card-title'>🟢 2. Structural Integrity</div>")
            st.html("<div class='card-value'>0%</div><p style='color:#64748B; font-size:12px;'>Overall Progress</p>")
            fig_bar = go.Figure(go.Bar(x=['Mar', 'Apr', 'May', 'Jun'], y=[0, 0, 0, 0], marker_color='#10B981'))
            fig_bar.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_bar, use_container_width=True, key="structural_chart", config={'displayModeBar': False})

    # الصف الثاني للمؤشرات (الاستدامة والطاقة المتوافقة مع المباني الخضراء)
    r2_c1, r2_c2 = st.columns(2)
    
    with r2_c1:
        with st.container(border=True):
            st.html("<div class='card-title'>🟢 3. Energy Optimization</div>")
            st.html("<div class='card-value'>0%</div><p style='color:#64748B; font-size:12px;'>Overall Progress</p>")
            st.html("<span style='color:#059669; font-weight:bold;'>27%</span> <span style='font-size:12px; color:#64748B;'>Estimated Savings</span>")
        
    with r2_c2:
        with st.container(border=True):
            st.html("<div class='card-title'>🟢 4. Sustainability Impact</div>")
            st.html("<div class='card-value' style='color:#059669;'>61</div><p style='color:#64748B; font-size:12px;'>Green Score</p>")
            st.html("<span style='font-size:12px; color:#64748B;'>CO₂ Reduction Potential:</span><br><span style='font-weight:bold; color:#059669;'>128.5 Tons/Year</span>")

    # الصف الثالث للمؤشرات (الميزانيات المالية وفترات المشروع الزمنية المقررة)
    r3_c1, r3_c2 = st.columns(2)
    
    with r3_c1:
        with st.container(border=True):
            st.html("<div class='card-title'>🟣 5. Cost Management</div>")
            st.html("<div class='card-value'>18%</div>")
            st.progress(0.18)
            st.html("<p style='font-size:12px; color:#64748B; margin-top:5px;'>Budget Overview:<br><b>$1.28M</b> / $7.00M</p>")
        
    with r3_c2:
        with st.container(border=True):
            st.html("<div class='card-title'>🔵 6. Project Timeline</div>")
            st.html("<div class='card-value'>14%</div>")
            st.progress(0.14)
            st.html("<p style='font-size:12px; color:#64748B; margin-top:5px;'>Project Duration:<br><b>42</b> / 300 Days</p>")

st.markdown("---")

# 4. الميزات الأساسية والتوثيقات الأمنية للمنصة في ذيل الصفحة (Footer Features)
f1, f2, f3, f4 = st.columns(4)
with f1:
    st.markdown("🛡️ **Secure & Sovereign**")
    st.caption("End-to-end data protection with local compliance")
with f2:
    st.markdown("🧠 **AI-Powered Analytics**")
    st.caption("Smarter insights for better construction decisions")
with f3:
    st.markdown("✅ **Regulatory Compliance**")
    st.caption("Aligned with national & international green building standards")
with f4:
    st.markdown("🎧 **Expert Support**")
    st.caption("Dedicated engineering support team")
