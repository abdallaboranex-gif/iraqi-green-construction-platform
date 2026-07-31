# pages/1_Compliance_Gate.py
import streamlit as st
import pandas as pd

# إعداد الصفحة وتوسيعها لتبدو كمنصة برمجية متكاملة
st.set_page_config(page_title="Iraqi Green Construction Data Platform", layout="wide")

# تفعيل جلسة الذاكرة للمؤشرات إذا لم تكن موجودة
if "compliance_rate" not in st.session_state:
    st.session_state["compliance_rate"] = 42
if "step2_status" not in st.session_state:
    st.session_state["step2_status"] = "In Progress"

# --- 1. الشريط العلوي للمنصة (Header & Project Info) ---
col_logo, col_lang, col_loc, col_user = st.columns([2, 1, 2, 2])
with col_logo:
    st.markdown("### 🏢 **Iraqi Green Construction**")
    st.caption("Data • Compliance • Sustainability • Efficiency")
with col_lang:
    st.segmented_control("Language", ["العربية", "EN"], default="EN", label_visibility="collapsed")
with col_loc:
    st.markdown("📍 **Current Project Location:** <br><span style='color:#10B981; font-weight:bold;'>Baghdad</span>", unsafe_allow_html=True)
with col_user:
    st.markdown("👤 **Eng. Abdulla** <br><span style='color:#6B7280; font-size:0.85rem;'>Project Manager</span>", unsafe_allow_html=True)

st.divider()

# --- 2. تقسيم الشاشة الرئيسي (أعمدة الواجهة) ---
col_left, col_right = st.columns([5, 3], gap="large")

# ==================== الجانب الأيسر: إدارة الخطوات والمراحل ====================
with col_left:
    st.markdown("<h4>PHASE 1 &nbsp; 🎯 Engineering Compliance <span style='font-size:0.9rem; color:#6B7280; font-weight:normal;'>(Strict Sequential Order)</span></h4>", unsafe_allow_html=True)
    
    # --- الخطوة 1 ---
    with st.container(border=True):
        c1, c2, c3 = st.columns([1, 6, 3])
        with c1: st.markdown("### 🟢 `1` ")
        with c2:
            st.markdown("**Step 1: Site Analysis & Zoning Regulations**")
            st.caption("Completed on 15 May 2026 • by Eng. Abdulla")
        with c3:
            st.markdown("<span style='color:#10B981; font-weight:bold;'>🟢 Completed</span>", unsafe_allow_html=True)
            st.button("📄 Download Site Report", key="dl_s1", size="small")

    st.markdown("<div style='text-align:center; color:#D1D5DB; margin:-5px 0;'>│</div>", unsafe_allow_html=True)

    # --- الخطوة 2 (النشطة والخاصة بفحص التربة) ---
    step2_border_color = "#F59E0B" if st.session_state["step2_status"] == "In Progress" else "#10B981"
    with st.container(border=True):
        st.markdown(f"<div style='border-right: 4px solid {step2_border_color}; padding-right:10px;'>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1, 6, 3])
        with c1: st.markdown("### 🟠 `2` ")
        with c2:
            st.markdown("**Step 2: Soil Inspection & Foundations**")
            st.caption("قيد المعالجة - يرجى رفع تقرير المختبر الجيوتقني للمطابقة الذكية")
        with c3:
            status_text = "🟠 In Progress" if st.session_state["step2_status"] == "In Progress" else "🟢 Completed"
            st.markdown(f"<b>{status_text}</b>", unsafe_allow_html=True)
        
        # صندوق رفع الملفات الذكي (Drag & Drop)
        uploaded_file = st.file_uploader("(Soil Lab PDF) سحب وإفلات تقرير المختبر هنا", type=["pdf"])
        
        # حقول إدخال المعطيات السريعة لمحاكاة الفحص الرقمي
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            bearing_cap = st.number_input("قدرة تحمل التربة المقاسة (kPa):", min_value=10, max_value=500, value=120)
            gypsum = st.number_input("محتوى الجبس في التربة (%):", min_value=0.0, max_value=100.0, value=4.5)
        with sub_col2:
            building_height = st.number_input("الارتفاع الكلي للمنشأ (متر):", min_value=3, max_value=50, value=10)
            report_status = st.selectbox("اعتمادية الختم والتقرير:", ["معتمد ومجاز ومصادق", "غير مصادق"])
            
        if st.button("🚨 تشغيل التدقيق الكودي والبلدي الفوري", type="primary", use_container_width=True):
            # استدعاء محرك التربة والـ JSON المرفوع في الخلفية لتشغيل الفحص
            from shared_engines.compliance_engine import IraqiSoilValidationEngine
            soil_engine = IraqiSoilValidationEngine(rules_file_path="soil_rules.json")
            
            payload = {
                "governorate": "Baghdad", "total_land_area_m2": 300, 
                "total_floors": int(building_height / 3), "soil_bearing_capacity": bearing_cap,
                "soil_report_status": report_status, "report_age_months": 1, "actual_boreholes_count": 2, 
                "actual_borehole_depth_meters": 6.0, "actual_compaction_degree_percentage": 96.0,
                "actual_gypsum_percentage": gypsum, "actual_so3_percentage": 1.5
            }
            
            soil_result = soil_engine.validate_soil_report(payload)
            
            # عرض التقرير الهندسي أسفل الصندوق مباشرة وبشكل متناسق
            st.markdown("#### 🔬 تقرير مطابقة مدونة التربة:")
            if soil_result["status"] == "PASSED":
                st.success(soil_result["summary"])
                st.session_state["compliance_rate"] = 68  # رفع النسبة عند النجاح
                st.session_state["step2_status"] = "Completed"
                st.rerun()
            else:
                st.error(soil_result["summary"])
                for err in soil_result["failures"]:
                    st.warning(err)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='text-align:center; color:#D1D5DB; margin:-5px 0;'>│</div>", unsafe_allow_html=True)

    # --- الخطوات المغلقة (قيد الانتظار) ---
    for step_num, step_title in [("3", "Step 3: Structural Audit & Load Calculations"), 
                                 ("4", "Step 4: Hydro-Sanitary & Plumbing Design"), 
                                 ("5", "Step 5: Electrical Systems Analysis")]:
        with st.container(border=True):
            c1, c2, c3 = st.columns([1, 6, 3])
            with c1: st.markdown(f"### 🔒 `{step_num}`")
            with c2: st.markdown(f"<span style='color:#9CA3AF;'>{step_title}</span>", unsafe_allow_html=True)
            with c3: st.markdown("<span style='color:#9CA3AF;'>🔒 Locked</span>", unsafe_allow_html=True)
            
    # بنر الترقية (Premium Pack) في نهاية العمود الأيسر
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("<div style='background-color:#1E3A8A; color:white; padding:15px; border-radius:8px;'>👑 <b>Subscribe to Premium Pack</b><br><span style='font-size:0.85rem; color:#93C5FD;'>Unlock all 14 automated compliance calculators and background verification hooks.</span></div>", unsafe_allow_html=True)


# ==================== الجانب الأيمن: لوحة القيادة والمؤشرات ====================
with col_right:
    st.markdown("<h4>📊 Executive Analytics Dashboard</h4>", unsafe_allow_html=True)
    
    # كرت 1: نسبة المطابقة الهندسية العامة
    with st.container(border=True):
        rc1, rc2 = st.columns([2, 1])
        with rc1:
            st.markdown(f"🌐 **1. Engineering Compliance**<br><h2 style='color:#1D4ED8;'>{st.session_state['compliance_rate']}%</h2>Overall Progress", unsafe_allow_html=True)
        with rc2:
            st.progress(st.session_state["compliance_rate"] / 100)
            
    # كرت 2: السلامة الإنشائية والأسس
    with st.container(border=True):
        rc1, rc2 = st.columns([2, 1])
        with rc1:
            struct_rate = 100 if st.session_state["step2_status"] == "Completed" else 0
            st.markdown(f"🟢 **2. Structural Integrity**<br><h2 style='color:#10B981;'>{struct_rate}%</h2>Overall Progress", unsafe_allow_html=True)
        with rc2:
            st.progress(struct_rate / 100)

    # كرت 3: كفاءة الطاقة
    with st.container(border=True):
        rc1, rc2 = st.columns([2, 1])
        with rc1:
            st.markdown("⚡ **3. Energy Optimization**<br><h2 style='color:#D97706;'>0%</h2>Overall Progress", unsafe_allow_html=True)
        with rc2:
            st.progress(0.0)

    # كرت 4: مؤشر الاستدامة والأثر البيئي
    with st.container(border=True):
        st.markdown("🌱 **4. Sustainability Impact**", unsafe_allow_html=True)
        st.metric(label="Green Score", value="61", delta="CO₂ Reduction Potential: 128.5 Tons/Year")
        
    # كرت 5: إدارة الميزانية والجدول الزمني
    with st.container(border=True):
        st.markdown("📅 **5. Timeline & Cost Management**", unsafe_allow_html=True)
        st.caption("Project Duration: 42 / 300 Days (14%)")
        st.caption("Budget Overview: $1.28M / $7.00M (18%)")
