import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from shared_utils.engines.engineering_compliance_engine import verify_soil_report
from shared_utils.engines.energy_sustainability_engine import calculate_energy_roi
from shared_utils.engines.data_anonymizer import anonymize_owner_data, get_provincial_green_stats

# 1. إعدادات الصفحة وهوية المنصة البصرية
st.set_page_config(page_title="Iraqi Green Construction Data Platform", page_icon="🏗️", layout="wide")

# تهيئة الذاكرة المؤقتة بشكل صريح ومضمون لمنع الـ AttributeError
if "step2_completed" not in st.session_state:
    st.session_state.step2_completed = False
if "compliance_rate" not in st.session_state:
    st.session_state.compliance_rate = 42
if "chart_data" not in st.session_state:
    st.session_state.chart_data = [20, 35, 40, 42, 42, 42]
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
    .roi-box { background-color: #F0FDF4; border: 1px solid #BBF7D0; padding: 15px; border-radius: 8px; margin-top: 15px; }
    .anonymizer-box { background-color: #F8FAFC; border: 1px dashed #CBD5E1; padding: 15px; border-radius: 8px; font-family: monospace; }
</style>
"""
st.html(theme_css)

# 2. القائمة الجانبية للتنقل بين المحاور (Sidebar Navigation)
with st.sidebar:
    st.markdown("### 🗺️ بوابات المنصة")
    app_mode = st.radio(
        "اختر الواجهة المطلوبة:",
        [
            "📊 لوحة القيادة والمؤشرات تماثل صورتك", 
            "⚡ حاسبة عزل الطاقة والجدوى للمولدات",
            "☁️ السحابة المركزية وتعمية بيانات الخصوصية"
        ]
    )
    st.markdown("---")
    st.caption("المنصة العراقية الموحدة للبناء الأخضر لعام 2026")

# 3. الهيدر العلوي الموحد للمنصة
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
# --- تابع لملف main_portal.py (القطعة الأولى من الجزء الثاني لغلق الأنظمة) ---

if app_mode == "📊 لوحة القيادة والمؤشرات تماثل صورتك":
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("#### 🔵 PHASE 1 : Engineering Compliance `Strict Sequential Order`")
        st.html("""
        <div class="step-box">
            <span style="color:#059669; font-weight:bold;">🟢 Step 1: Site Analysis & Zoning Regulations</span> 
            <span class="completed-badge">Completed</span>
            <p style="color:#64748B; font-size:13px; margin-top:5px;">Completed on 15 May 2025 • by Eng. Abdulla</p>
        </div>
        """)
        
        with st.container():
            # قراءة البيانات والتحقق من حالة الذاكرة بشكل صريح وآمن
            is_step2_done = st.session_state.get("step2_completed", False)
            
            if not is_step2_done:
                st.html("<div class='step-active'><span style='color:#F97316; font-weight:bold;'>🟠 Step 2: Soil Inspection & Foundations</span> <span class='progress-badge'>In Progress</span></div>")
                uploaded_file = st.file_uploader("Upload (Soil Lab PDF) - Max 50MB", type=["pdf"], key="soil_pdf")
                if uploaded_file is not None:
                    result = verify_soil_report(uploaded_file)
                    st.session_state.soil_results = result
                    if result.get("status", False):
                        st.session_state.step2_completed = True
                        st.session_state.compliance_rate = 55
                        st.session_state.chart_data =
                        st.rerun()
            else:
                st.html("<div class='step-done'><span style='color:#10B981; font-weight:bold;'>🟢 Step 2: Soil Inspection & Foundations</span> <span class='completed-badge'>Completed</span></div>")
                soil_res = st.session_state.get("soil_results", None)
                if soil_res:
                    st.info(f"📋 **بيانات المطابقة:** قدرة التحمل: {soil_res.get('bearing_capacity')} kPa | معامل الأمان: {soil_res.get('safety_factor')}")
                if st.button("🔄 Clear and Re-upload File"):
                    st.session_state.step2_completed = False
                    st.session_state.compliance_rate = 42
                    st.session_state.chart_data =
                    st.session_state.soil_results = None
                    st.rerun()

        if st.session_state.get("step2_completed", False):
            st.html("<div class='step-active'><span style='color:#F97316; font-weight:bold;'>🟠 Step 3: Structural Audit & Load Calculations</span><span class='progress-badge'>Unlocked</span></div>")
        else:
            st.html("<div class='step-box' style='opacity:0.5;'><span style='color:#64748B;'>🔒 Step 3: Structural Audit & Load Calculations</span></div>")
            
        st.html("""
        <div class="step-box" style="opacity: 0.5;"><span style="color:#64748B;">🔒 Step 4: Hydro-Sanitary & Plumbing Design</span></div>
        <div class="step-box" style="opacity: 0.5;"><span style="color:#64748B;">🔒 Step 5: Electrical Systems Analysis</span></div>
        <div class="premium-box">
            <h5>👑 Subscribe to Premium Pack <span style="background-color:#EAB308; color:black; padding:2px 6px; border-radius:4px; font-size:11px; font-weight:bold;">PREMIUM</span></h5>
            <p style="font-size:13px; color:#94A3B8;">Unlock all 14 automated compliance calculators, process soil lab data via AI, and generate legally verified PDF reports.</p>
        </div>
        """)

    with col_right:
        r1_c1, r1_c2 = st.columns(2)
        with r1_c1:
            with st.container(border=True):
                st.html("<div class='card-title'>🔵 1. Engineering Compliance</div>")
                current_rate = st.session_state.get("compliance_rate", 42)
                st.html(f"<div class='card-value'>{current_rate}%</div>")
                current_chart = st.session_state.get("chart_data", )
                fig_line = go.Figure(go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], y=current_chart, mode='lines+markers', line=dict(color='#2563EB', width=2)))
                fig_line.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_line, use_container_width=True, key="compliance_chart", config={'displayModeBar': False})
        with r1_c2:
            with st.container(border=True):
                st.html("<div class='card-title'>🟢 2. Structural Integrity</div>")
                st.html("<div class='card-value'>0%</div>")
                fig_bar = go.Figure(go.Bar(x=['Mar', 'Apr', 'May', 'Jun'], y=, marker_color='#10B981'))
                fig_bar.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=80, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_bar, use_container_width=True, key="structural_chart", config={'displayModeBar': False})

        r2_c1, r2_c2 = st.columns(2)
        with r2_c1:
            with st.container(border=True):
                st.html("<div class='card-title'>🟢 3. Energy Optimization</div>")
                st.html("<div class='card-value'>0%</div><span style='color:#059669; font-weight:bold;'>27%</span> <span style='font-size:12px; color:#64748B;'>Estimated Savings</span>")
        with r2_c2:
            with st.container(border=True):
                st.html("<div class='card-title'>🟢 4. Sustainability Impact</div>")
                st.html("<div class='card-value' style='color:#059669;'>61</div><span style='font-size:12px; color:#64748B;'>CO₂ Reduction: <b>128.5 Tons/Year</b></span>")

        r3_c1, r3_c2 = st.columns(2)
        with r3_c1:
            with st.container(border=True):
                st.html("<div class='card-title'>🟣 5. Cost Management</div>")
                st.html("<div class='card-value'>18%</div>")
                st.progress(0.18)
        with r3_c2:
            with st.container(border=True):
                st.html("<div class='card-title'>🔵 6. Project Timeline</div>")
                st.html("<div class='card-value'>14%</div>")
                st.progress(0.14)

elif app_mode == "⚡ حاسبة عزل الطاقة والجدوى للمولدات":
    st.markdown("### ⚡ بوابة إدارة الطاقة المستدامة وحساب فواتير المولدات الأهلية صيفاً")
    st.info("هذه الحاسبة متوافقة مع الكود الإنشائي العراقي وتعتمد على درجات الحرارة القصوى لمدينة بغداد.")
    
    col_input, col_output = st.columns(2)
    with col_input:
        with st.container(border=True):
            st.markdown("#### 📥 مدخلات المبنى والموقع")
            area = st.number_input("مساحة الغلاف الإنشائي المعرض للشمس (متر مربع):", min_value=50, max_value=5000, value=200, step=50)
            insulation = st.selectbox("نوع مادة الجدران والبناء المستخدمة:", ["طابوق عادي بدون عزل", "ثرمستون (صديق للبيئة)", "عزل حراري متكامل (صوف صخري/بولسترين)"])
            amps = st.number_input("حجم سحب الأمبيرات الحالي المخصص للتكييف والتبريد صيفاً:", min_value=5, max_value=200, value=30, step=5)
            calculate_btn = st.button("🧮 تشغيل محرك الجدوى المالية والطاقة", type="primary")

    with col_output:
        if calculate_btn:
            results = calculate_energy_roi(area, insulation, amps)
            with st.container(border=True):
                st.markdown("#### 📊 التقرير الهندسي والمالي للاستدامة")
                st.write(f"☀️ درجة الحرارة التصميمية صيفاً لوسط العراق: **{results.get('design_temp')}°C**")
                st.write(f"📉 معامل الكسب الحراري الكلي للجدران `U-Value`: **{results.get('u_value')} W/m²K**")
                st.html(f"""
                <div class="roi-box">
                    <h5 style="color:#065F46; margin:0;">📉 الوفر في استهلاك الكهرباء والأمبيرات:</h5>
                    <p style="font-size:20px; font-weight:bold; color:#047857; margin:5px 0;">تم توفير {results.get('amperage_saved')} أمبير! (الحاجة الجديدة: {results.get('new_amp_needed']} أمبير)</p>
                    <h5 style="color:#065F46; margin:10px 0 0 0;">💰 الوفر المالي السنوي التقديري (تعرفة المولد الأهلية):</h5>
                    <p style="font-size:22px; font-weight:bold; color:#15803D; margin:5px 0;">{results.get('annual_savings_iqd'):,} دينار عراقي سنوياً</p>
                    <h5 style="color:#1E3A8A; margin:10px 0 0 0;">⏳ فترة استرداد رأس مال تركيب العزل (Payback Period):</h5>
                    <p style="font-size:18px; font-weight:bold; color:#1D4ED8; margin:5px 0;">{results.get('payback_years')} سنة برأس مال مسترد بالكامل</p>
                </div>
                """)
        else:
            st.markdown("#### ⏳ بانتظار المدخلات")
# --- تابع لملف main_portal.py (القطعة الثانية والأخيرة لعرض السحابة والفوتر الموحد) ---

else:
    # عرض بوابة السحابة المركزية وتعمية الخصوصية (المحور الثالث)
    st.markdown("### ☁️ بوابة السحابة المركزية ومجمّع المؤشرات الوطنية")
    st.info("تستعرض هذه الواجهة البيانات المجمّعة للمحافظات مع تفعيل خوارزمية تعمية الخصوصية لحماية معلومات المواطنين.")
    
    col_mask, col_stats = st.columns(2)
    with col_mask:
        with st.container(border=True):
            st.markdown("#### 🔐 نظام حماية البيانات والخصوصية الفوري")
            raw_input = st.text_area(
                "بيانات المالك التجريبية:", 
                value="المالك: أحمد العبيدي، هاتف: 07701234567، الرقم الوطني الموحد: 199012345678، موقع المشروع: بغداد/المنصور"
            )
            if st.button("🔒 تشغيل فلتر الحجب والتعمية", type="primary"):
                masked_output = anonymize_owner_data(raw_input)
                st.markdown("**📄 النص المشفّر الجاهز للرفع للسحابة المركزية:**")
                st.html(f"<div class='anonymizer-box'>{masked_output}</div>")
                st.success("✅ تم حجب الهوية والحفاظ على السرية السيادية للبيانات!")

    with col_stats:
        with st.container(border=True):
            st.markdown("#### 📈 البيانات المجمّعة للمحافظات العراقية (البناء الأخضر)")
            raw_stats = get_provincial_green_stats()
            df = pd.DataFrame(raw_stats)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            fig_prov = go.Figure(go.Bar(
                x=df["المحافظة"], 
                y=df["الوفر الكربوني التراكمي (طن)"], 
                marker_color='#2563EB',
                text=df["نسبة الالتزام بالعزل (%)"].apply(lambda x: f"التزام {x}%"),
                textposition='auto'
            ))
            fig_prov.update_layout(title="ترتيب المحافظات الأعلى وفراً للكربون والطاقة لعام 2026", margin=dict(l=20, r=20, t=40, b=20), height=220, plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_prov, use_container_width=True, config={'displayModeBar': False})

st.markdown("---")

# 4. شريط التوثيقات الموحد للفوتر لإغلاق الصفحة بشكل برمي مستقر
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
