import streamlit as st
import plotly.graph_objects as go
# استدعاء الثوابت ومحرك الفحص العراقي الذي أنشأته في الدفعات السابقة
from shared_utils.engines.engineering_compliance_engine import verify_soil_report

# 1. إعدادات الصفحة وهوية المنصة البصرية
st.set_page_config(page_title="Iraqi Green Construction Data Platform", page_icon="🏗️", layout="wide")

# تهيئة الذاكرة المؤقتة (Session State) لحفظ حالة الخطوات ونتائج الفحص الهندسي
if "step2_completed" not in st.session_state:
    st.session_state.step2_completed = False
if "compliance_rate" not in st.session_state:
    st.session_state.compliance_rate = 42
if "chart_data" not in st.session_state:
    st.session_state.chart_data = [20, 25, 30, 35, 42, 42]
if "soil_results" not in st.session_state:
    st.session_state.soil_results = None

# تطبيق كود التنسيق الهيكلي (CSS) بطريقة آمنة
theme_css = """
<style>
    .stApp { background-color: #F8FAFC !important; }
    .card { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px; height: 100%; }
    .step-box { border: 1px solid #E2E8F0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #F8FAFC; }
    .step-active { border: 1px solid #FFEDD5; background-color: #FFFFf0; border-left: 5px solid #F97316; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
    .step-done { border: 1px solid #D1FAE5; background-color: #F0FDF4; border-left: 5px solid #10B981; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
    .premium-box { background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%); color: white; padding: 20px; border-radius: 12px; margin-top: 20px; }
    .green-text { color: #059669; font-weight: bold; }
    .gray-text { color: #64748B; }
    .completed-badge { float: right; background-color: #D1FAE5; color: #065F46; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; }
    .progress-badge { float: right; background-color: #FFEDD5; color: #9A3412; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; }
    .card-title { font-weight: bold; margin-bottom: 5px; color: #1E293B; }
    .card-value { font-size: 28px; font-weight: bold; margin: 0; color: #0F172A; }
</style>
"""
st.html(theme_css)

# 2. الهيدر العلوي للمنصة
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
# --- تابع لملف main_portal.py (الجزء الثاني والأخير) ---

# 3. تخطيط الصفحة الرئيسي المتوازن (يسار: مسار العمليات / يمين: المؤشرات)
col_left, col_right = st.columns(2)

# --- الجانب الأيسر: المراحل والخطوات التتابعية للمشروع ---
with col_left:
    st.markdown("#### 🔵 PHASE 1 : Engineering Compliance `Strict Sequential Order`")
    
    # الخطوة 1: تحليل الموقع
    st.html("""
    <div class="step-box">
        <span style="color:#059669; font-weight:bold;">🟢 Step 1: Site Analysis & Zoning Regulations</span> 
        <span class="completed-badge">Completed</span>
        <p style="color:#64748B; font-size:13px; margin-top:5px;">Completed on 15 May 2025 • by Eng. Abdulla</p>
    </div>
    """)
    
    # الخطوة 2: فحص التربة التفاعلي والمرتبط بالمحرك المركزي
    with st.container():
        if not st.session_state.step2_completed:
            st.html("<div class='step-active'><span style='color:#F97316; font-weight:bold;'>🟠 Step 2: Soil Inspection & Foundations</span> <span class='progress-badge'>In Progress</span></div>")
            uploaded_file = st.file_uploader("Upload (Soil Lab PDF) - Max 50MB", type=["pdf"], key="soil_pdf")
            
            if uploaded_file is not None:
                # تشغيل محرك الفحص الهندسي عالي الأداء
                result = verify_soil_report(uploaded_file)
                st.session_state.soil_results = result
                
                if result["status"]:
                    st.session_state.step2_completed = True
                    st.session_state.compliance_rate = 55
                    st.session_state.chart_data = [42, 45, 48, 50, 52, 55]
                    st.success("🎉 " + result["message"])
                    st.rerun()
                else:
                    st.error("❌ " + result["message"])
        else:
            st.html("""
            <div class="step-done">
                <span style="color:#10B981; font-weight:bold;">🟢 Step 2: Soil Inspection & Foundations</span> 
                <span class="completed-badge">Completed</span>
            </div>
            """)
            # طباعة نتائج الفحص التي أرجعها المحرك
            if st.session_state.soil_results:
                res = st.session_state.soil_results
                st.info(f"📋 **بيانات المطابقة:** قدرة التحمل المقبولة: {res['bearing_capacity']} kPa | معامل الأمان المعتمد: {res['safety_factor']}")
            
            if st.button("🔄 Clear and Re-upload File"):
                st.session_state.step2_completed = False
                st.session_state.compliance_rate = 42
                st.session_state.chart_data = [42, 42, 42, 42, 42, 42]
                st.session_state.soil_results = None
                st.rerun()
    
    # الخطوات التالية (تفتح الخطوة 3 تلقائياً عند نجاح المطابقة الكودية!)
    if st.session_state.step2_completed:
        st.html("""
        <div class="step-active">
            <span style="color:#F97316; font-weight:bold;">🟠 Step 3: Structural Audit & Load Calculations</span>
            <span class="progress-badge">Unlocked</span>
        </div>
        """)
        st.button("⚙️ Start Structural Calculations", type="primary")
    else:
        st.html("""
        <div class="step-box" style="opacity: 0.5;">
            <span style="color:#64748B;">🔒 Step 3: Structural Audit & Load Calculations</span>
        </div>
        """)
        
    st.html("""
    <div class="step-box" style="opacity: 0.5;"><span style="color:#64748B;">🔒 Step 4: Hydro-Sanitary & Plumbing Design</span></div>
    <div class="step-box" style="opacity: 0.5;"><span style="color:#64748B;">🔒 Step 5: Electrical Systems Analysis</span></div>
    """)
        
    # بنر الترقية والاشتراكات السحابية المدفوعة
    st.html("""
    <div class="premium-box">
        <h5>👑 Subscribe to Premium Pack <span style="background-color:#EAB308; color:black; padding:2px 6px; border-radius:4px; font-size:11px; font-weight:bold;">PREMIUM</span></h5>
        <p style="font-size:13px; color:#94A3B8;">Unlock all 14 automated compliance calculators, process soil lab data via AI, and generate legally verified PDF audit reports.</p>
        <button style="background-color:#EAB308; border:none; color:black; padding:8px 16px; border-radius:6px; font-weight:bold; cursor:pointer;">Upgrade Now 👑</button>
    </div>
    """)


# --- الجانب الأيمن: لوحات قياس المؤشرات والرسوم البيانية التفاعلية (KPI Cards) ---
with col_right:
    r1_c1, r1_c2 = st.columns(2)
    
    with r1_c1:
        with st.container(border=True):
            st.html("<div class='card-title'>🔵 1. Engineering Compliance</div>")
            st.html(f"<div class='card-value'>{st.session_state.compliance_rate}%</div><p style='color:#64748B; font-size:12px;'>Overall Progress</p>")
            fig_line = go.Figure(go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], y=st.session_state.chart_data, mode='lines+markers', line=dict(color='#2563EB', width=2)))
            fig_line.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_line, use_container_width=True, key="compliance_chart", config={'displayModeBar': False})
        
    with r1_c2:
        with st.container(border=True):
            st.html("<div class='card-title'>🟢 2. Structural Integrity</div>")
            st.html("<div class='card-value'>0%</div><p style='color:#64748B; font-size:12px;'>Overall Progress</p>")
            fig_bar = go.Figure(go.Bar(x=['Mar', 'Apr', 'May', 'Jun'], y=[0, 0, 0, 0], marker_color='#10B981'))
            fig_bar.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_bar, use_container_width=True, key="structural_chart", config={'displayModeBar': False})

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
