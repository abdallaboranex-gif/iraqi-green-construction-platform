import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from shared_utils.engines.engineering_compliance_engine import verify_soil_report
from shared_utils.engines.energy_sustainability_engine import calculate_energy_roi
from shared_utils.engines.data_anonymizer import anonymize_owner_data, get_provincial_green_stats

st.set_page_config(page_title="Iraqi Green Construction", page_icon="🏗️", layout="wide")

# تهيئة الذاكرة بطريقة رياضية آمنة تمنع الحذف والـ SyntaxError
if "step2_completed" not in st.session_state:
    st.session_state["step2_completed"] = False
if "compliance_rate" not in st.session_state:
    st.session_state["compliance_rate"] = 42
if "val1" not in st.session_state:
    st.session_state["val1"] = 10
if "val2" not in st.session_state:
    st.session_state["val2"] = 20
if "val3" not in st.session_state:
    st.session_state["val3"] = 30
if "val4" not in st.session_state:
    st.session_state["val4"] = 35
if "val5" not in st.session_state:
    st.session_state["val5"] = 42
if "val6" not in st.session_state:
    st.session_state["val6"] = 42
if "soil_results" not in st.session_state:
    st.session_state["soil_results"] = None

theme_css = """
<style>
    .stApp { background-color: #F8FAFC !important; }
    .step-box { border: 1px solid #E2E8F0; padding: 15px; border-radius: 10px; margin-bottom: 12px; background-color: #F8FAFC; }
    .step-active { border: 1px solid #FFEDD5; background-color: #FFFFf0; border-left: 5px solid #F97316; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
    .step-done { border: 1px solid #D1FAE5; background-color: #F0FDF4; border-left: 5px solid #10B981; padding: 15px; border-radius: 10px; margin-bottom: 12px; }
    .premium-box { background: linear-gradient(90deg, #0F172A 0%, #1E293B 100%); color: white; padding: 20px; border-radius: 12px; margin-top: 20px; }
    .completed-badge { float: right; background-color: #D1FAE5; color: #065F46; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; }
    .progress-badge { float: right; background-color: #FFEDD5; color: #9A3412; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: bold; }
    .card-title { font-weight: bold; margin-bottom: 5px; color: #1E293B; }
    .card-value { font-size: 28px; font-weight: bold; margin: 0; color: #0F172A; }
    .roi-box { background-color: #F0FDF4; border: 1px solid #BBF7D0; padding: 15px; border-radius: 8px; margin-top: 15px; }
    .anonymizer-box { background-color: #F8FAFC; border: 1px dashed #CBD5E1; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
"""
st.html(theme_css)

with st.sidebar:
    st.markdown("### 🗺️ بوابات المنصة")
    app_mode = st.radio("اختر الواجهة المطلوبة:", ["Dashboard", "Energy ROI", "Cloud Aggregation"])

with st.container():
    col1, col2, col3 = st.columns(3)
    col1.markdown("### 🏢 Iraqi Green Construction")
    col2.markdown("**📍 Location:** Baghdad")
    col3.markdown("**👨‍💼 Manager:** Eng. Abdulla")
st.markdown("---")
# --- Part 2: Dynamic Interfaces & Layout Logic (Strict Syntactic Check) ---

if app_mode == "Dashboard":
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### 🔵 PHASE 1 : Engineering Compliance (Strict Order)")
        st.html("""
        <div class="step-box">
            <span style="color:#059669; font-weight:bold;">🟢 Step 1: Site Analysis & Zoning Regulations</span> 
            <span class="completed-badge">Completed</span>
            <p style="color:#64748B; font-size:13px; margin-top:5px;">Completed on 15 May 2025 • by Eng. Abdulla</p>
        </div>
        """)
        
        with st.container():
            if not st.session_state.get("step2_completed", False):
                st.html("<div class='step-active'><span style='color:#F97316; font-weight:bold;'>🟠 Step 2: Soil Inspection & Foundations</span> <span class='progress-badge'>In Progress</span></div>")
                uploaded_file = st.file_uploader("Upload (Soil Lab PDF) - Max 50MB", type=["pdf"], key="soil_pdf")
                if uploaded_file is not None:
                    result = verify_soil_report(uploaded_file)
                    st.session_state["soil_results"] = result
                    if result.get("status", False):
                        st.session_state["step2_completed"] = True
                        st.session_state["compliance_rate"] = 55
                        st.session_state["val6"] = 55
                        st.rerun()
            else:
                st.html("<div class='step-done'><span style='color:#10B981; font-weight:bold;'>🟢 Step 2: Soil Inspection & Foundations</span> <span class='completed-badge'>Completed</span></div>")
                soil_res = st.session_state.get("soil_results", {})
                if soil_res:
                    st.info(f"📋 قدرة التحمل: {soil_res.get('bearing_capacity')} kPa | معامل الأمان: {soil_res.get('safety_factor')}")
                if st.button("🔄 Clear and Re-upload File"):
                    st.session_state["step2_completed"] = False
                    st.session_state["compliance_rate"] = 42
                    st.session_state["val6"] = 42
                    st.session_state["soil_results"] = None
                    st.rerun()

        if st.session_state.get("step2_completed", False):
            st.html("<div class='step-active'><span style='color:#F97316; font-weight:bold;'>🟠 Step 3: Structural Audit & Load Calculations</span><span class='progress-badge'>Unlocked</span></div>")
        else:
            st.html("<div class='step-box' style='opacity:0.5;'><span style='color:#64748B;'>🔒 Step 3: Structural Audit & Load Calculations</span></div>")
            
        st.html("""
        <div class="step-box" style="opacity: 0.5;"><span style="color:#64748B;">🔒 Step 4: Hydro-Sanitary & Plumbing Design</span></div>
        <div class="step-box" style="opacity: 0.5;"><span style="color:#64748B;">🔒 Step 5: Electrical Systems Analysis</span></div>
        """)

    with col_right:
        r1_c1, r1_c2 = st.columns(2)
        with r1_c1:
            with st.container(border=True):
                st.html("<div class='card-title'>🔵 1. Engineering Compliance</div>")
                current_rate = st.session_state.get("compliance_rate", 42)
                st.html(f"<div class='card-value'>{current_rate}%</div>")
                
                chart_list = [
                    st.session_state.get("val1", 10),
                    st.session_state.get("val2", 20),
                    st.session_state.get("val3", 30),
                    st.session_state.get("val4", 35),
                    st.session_state.get("val5", 42),
                    st.session_state.get("val6", 42)
                ]
                fig_line = go.Figure(go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], y=chart_list, mode='lines+markers', line=dict(color='#2563EB', width=2)))
                fig_line.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_line, use_container_width=True, key="compliance_chart", config={'displayModeBar': False})
        with r1_c2:
            with st.container(border=True):
                st.html("<div class='card-title'>🟢 2. Structural Integrity</div>")
                st.html("<div class='card-value'>0%</div>")
                # تم معالجة مصفوفة الهيكل الإنشائي برمجياً لتجنب الحذف تماماً
                structural_list = list(map(int, "0000"))
                fig_bar = go.Figure(go.Bar(x=['Mar', 'Apr', 'May', 'Jun'], y=structural_list, marker_color='#10B981'))
                fig_bar.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_bar, use_container_width=True, key="structural_chart", config={'displayModeBar': False})

        r2_c1, r2_c2 = st.columns(2)
        with r2_c1:
            with st.container(border=True):
                st.html("<div class='card-title'>🟢 3. Energy Optimization</div>")
                st.html("<div class='card-value'>0%</div><span style='color:#059669; font-weight:bold;'>27%</span>")
        with r2_c2:
            with st.container(border=True):
                st.html("<div class='card-title'>🟢 4. Sustainability Impact</div>")
                st.html("<div class='card-value' style='color:#059669;'>61</div>")

elif app_mode == "Energy ROI":
    st.markdown("### ⚡ بوابة إدارة الطاقة وحساب فواتير المولدات")
    col_input, col_output = st.columns(2)
    with col_input:
        with st.container(border=True):
            area = st.number_input("مساحة الغلاف الإنشائي المعرض للشمس (متر مربع):", min_value=50, max_value=5000, value=200, step=50)
            insulation = st.selectbox("نوع مادة الجدران والبناء المستخدمة:", ["طابوق عادي بدون عزل", "ثرمستون (صديق للبيئة)", "عزل حراري متكامل (صوف صخري/بولسترين)"])
            amps = st.number_input("حجم سحب الأمبيرات الحالي للتكييف صيفاً:", min_value=5, max_value=200, value=30, step=5)
            calculate_btn = st.button("🧮 تشغيل محرك الجدوى المالية والطاقة", type="primary")

    with col_output:
        if calculate_btn:
            results = calculate_energy_roi(area, insulation, amps)
            with st.container(border=True):
                st.markdown("#### 📊 التقرير الهندسي والمالي للاستدامة")
                st.write(f"☀️ درجة الحرارة التصميمية صيفاً لبغداد: **{results.get('design_temp')}°C**")
                st.write(f"📉 معامل الكسب الحراري `U-Value`: **{results.get('u_value')} W/m²K**")
                st.html(f"""
                <div class="roi-box">
                    <p style="font-size:18px; font-weight:bold; color:#047857; margin:5px 0;">تم توفير {results.get('amperage_saved', 0)} أمبير! (الحاجة الجديدة: {results.get('new_amp_needed', 0)} أمبير)</p>
                    <p style="font-size:18px; font-weight:bold; color:#15803D; margin:5px 0;">الوفر: {results.get('annual_savings_iqd', 0):,} دينار عراقي سنوياً</p>
                    <p style="font-size:16px; font-weight:bold; color:#1D4ED8; margin:5px 0;">فترة استرداد رأس المال: {results.get('payback_years', 0)} سنة</p>
                </div>
                """)

else:
    st.markdown("### ☁️ بوابة السحابة المركزية ومجمّع المؤشرات الوطنية")
    col_mask, col_stats = st.columns(2)
    with col_mask:
        with st.container(border=True):
            raw_input = st.text_area(
                "بيانات المالك التجريبية:", 
                value="المالك: أحمد العبيدي، هاتف: 07701234567، البطاقة الموحدة: 199012345678"
            )
            if st.button("🔒 تشغيل فلتر الحجب والتعمية", type="primary"):
                masked_output = anonymize_owner_data(raw_input)
                st.markdown("**📄 النص المشفّر الجاهز للرفع للسحابة المركزية:**")
                st.html(f"<div class='anonymizer-box'>{masked_output}</div>")
                st.success("✅ تم حجب الهوية والحفاظ على السرية السيادية للبيانات!")

    with col_stats:
        with st.container(border=True):
            st.markdown("#### 📈 البيانات المجمّعة للمحافظات العراقية")
            raw_stats = get_provincial_green_stats()
            df = pd.DataFrame(raw_stats)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            carbon_list = df["الوفر الكربوني التراكمي (طن)"].tolist()
            fig_prov = go.Figure(go.Bar(
                x=df["المحافظة"], 
                y=carbon_list, 
                marker_color='#2563EB'
            ))
            fig_prov.update_layout(title="ترتيب المحافظات الأعلى وفراً للكربون لعام 2026", margin=dict(l=20, r=20, t=40, b=20), height=220, plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_prov, use_container_width=True, config={'displayModeBar': False})

st.markdown("---")
st.caption("🛡️ Secure & Sovereign | 🧠 AI-Powered Analytics | ✅ Regulatory Compliance")
