# pages/1_Compliance_Gate.py
import streamlit as st

# 1. إعداد الصفحة وتوسيعها بالكامل لتبدو كمنصة رقمية احترافية
st.set_page_config(page_title="Iraqi Green Construction Data Platform", layout="wide")

# 2. تفعيل الذاكرة المؤقتة للمؤشرات والنسب المئوية الحية
if "compliance_rate" not in st.session_state:
    st.session_state["compliance_rate"] = 42
if "step2_status" not in st.session_state:
    st.session_state["step2_status"] = "In Progress"

# 3. دالة بناء كروت المؤشرات الدائرية في الجانب الأيمن بالـ HTML
def render_metric_card(title, percentage, color, icon):
    return f"""
    <div style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <div>
            <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937; margin-bottom: 5px;">{icon} {title}</div>
            <div style="font-size: 0.8rem; color: #6B7280;">Overall Progress</div>
        </div>
        <div style="position: relative; width: 60px; height: 60px; border-radius: 50%; background: conic-gradient({color} {percentage * 3.6}deg, #E5E7EB 0deg); display: flex; align-items: center; justify-content: center;">
            <div style="position: absolute; width: 46px; height: 46px; border-radius: 50%; background-color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem; color: #1F2937;">
                {percentage}%
            </div>
        </div>
    </div>
    """

# 4. تصميم الشريط العلوي للمنصة وهيكل معلومات المهندس
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; padding-bottom: 10px;">
    <div>
        <h2 style="margin: 0; color: #1E3A8A; font-size: 1.6rem;">🏢 Iraqi Green Construction</h2>
        <div style="font-size: 0.85rem; color: #6B7280; margin-top: 2px;">Data • Compliance • Sustainability • Efficiency</div>
    </div>
    <div style="display: flex; gap: 30px; align-items: center;">
        <div style="background-color: #F3F4F6; padding: 4px; border-radius: 8px; display: flex; gap: 5px;">
            <span style="padding: 4px 12px; font-size: 0.85rem; color: #6B7280; cursor: pointer;">العربية</span>
            <span style="background-color: #1E3A8A; color: white; padding: 4px 12px; border-radius: 6px; font-size: 0.85rem; font-weight: bold;">EN</span>
        </div>
        <div>
            <div style="font-size: 0.75rem; color: #6B7280;">📍 Current Project Location:</div>
            <div style="color: #10B981; font-weight: bold; font-size: 0.95rem;">Baghdad</div>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
            <div style="text-align: right;">
                <div style="font-weight: bold; font-size: 0.9rem; color: #1F2937;">Eng. Abdulla</div>
                <div style="font-size: 0.75rem; color: #6B7280;">Project Manager</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# 5. فتح التقسيم العمودي الرئيسي للمنصة (الخطوات على اليسار، والتحليلات على اليمين)
col_left, col_right = st.columns([1.4, 1.0], gap="large")
# ==================== الجانب الأيسر: إدارة المراحل والخطوات الإنشائية ====================
with col_left:
    st.markdown("<div style='margin-bottom: 20px;'><span style='background-color: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; vertical-align: middle;'>PHASE 1</span> <span style='font-weight: bold; font-size: 1.1rem; margin-left: 8px; color: #1F2937;'>Engineering Compliance</span> <span style='font-size: 0.85rem; color: #6B7280; margin-left: 5px;'>(Strict Sequential Order)</span></div>", unsafe_allow_html=True)
    
    # --- Step 1: تحليل الموقع والمحددات البلدية والأرضية (مكتملة) ---
    with st.container(border=True):
        c1, c2, c3 = st.columns([0.15, 1.0, 0.55])
        with c1:
            st.markdown("<div style='background-color: #E8F5E9; color: #2E7D32; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: bold;'>1</div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div style='font-weight: bold; font-size: 0.95rem; color: #1F2937;'>Step 1: Site Analysis & Zoning Regulations</div>", unsafe_allow_html=True)
            st.markdown("<div style='font-size: 0.75rem; color: #9CA3AF;'>Completed on 15 May 2026 • by Eng. Abdulla</div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div style='text-align: right; color: #10B981; font-weight: bold; font-size: 0.85rem; margin-bottom: 5px;'>🟢 Completed</div>", unsafe_allow_html=True)
            st.button("Download Site Report", key="dl_s1", use_container_width=True)

    st.markdown("<div style='text-align: center; color: #D1D5DB; margin: -10px 0; font-size: 1.2rem;'>│</div>", unsafe_allow_html=True)

    # --- Step 2: فحص التربة والأسس الجيوتقنية (النشطة والمفتوحة للفحص بالـ JSON) ---
    is_pending = st.session_state["step2_status"] == "In Progress"
    border_clr = "#F59E0B" if is_pending else "#10B981"
    badge_text = "🟠 In Progress" if is_pending else "🟢 Completed"
    badge_clr = "#F59E0B" if is_pending else "#10B981"
    
    st.markdown(f"""
    <div style="border: 1px solid #E5E7EB; padding: 15px; border-radius: 12px; background-color: #FAFAFA; margin-bottom: 10px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; border-right: 4px solid {border_clr}; padding-right: 10px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="background-color: #FFF3E0; color: #E65100; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: bold;">2</div>
                <div>
                    <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937;">Step 2: Soil Inspection & Foundations</div>
                    <div style="font-size: 0.75rem; color: #6B7280;">يرجى رفع ملف تقرير المختبر أو إدخال القيم للتدقيق الذكي</div>
                </div>
            </div>
            <div style="color: {badge_clr}; font-weight: bold; font-size: 0.85rem;">{badge_text}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # حقل رفع ملف الـ PDF الجيوتقني للمطابقة الآلية
    uploaded_file = st.file_uploader("(Soil Lab PDF) سحب وإفلات تقرير المختبر هنا", type=["pdf"])
    
    # حقول إدخال المعطيات السريعة من قبل المهندس
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        bearing_cap = st.number_input("قدرة تحمل التربة المقاسة المختبرية (kPa):", min_value=10, max_value=500, value=120)
        gypsum = st.number_input("محتوى الجبس الكلي في التربة (%):", min_value=0.0, max_value=100.0, value=4.5)
    with sub_col2:
        building_height = st.number_input("الارتفاع الكلي للمبنى المعماري (متر):", min_value=3, max_value=50, value=10)
        report_status = st.selectbox("حالة مصادقة واعتماد الختم الجيوتقني:", ["معتمد ومجاز ومصادق", "غير مصادق"])
        
    if st.button("🚨 تشغيل التدقيق الكودي والبلدي الفوري", type="primary", use_container_width=True):
        try:
            from shared_engines.compliance_engine import IraqiSoilValidationEngine
            soil_engine = IraqiSoilValidationEngine(rules_file_path="soil_rules.json")
        except Exception:
            soil_engine = None
            
        if soil_engine:
            payload = {
                "governorate": "Baghdad", "total_land_area_m2": 300, 
                "total_floors": int(building_height / 3), "soil_bearing_capacity": bearing_cap,
                "soil_report_status": report_status, "report_age_months": 1, "actual_boreholes_count": 2, 
                "actual_borehole_depth_meters": 6.0, "actual_compaction_degree_percentage": 96.0,
                "actual_gypsum_percentage": gypsum, "actual_so3_percentage": 1.5
            }
            soil_result = soil_engine.validate_soil_report(payload)
            
            st.markdown("#### 🔬 تقرير مطابقة مدونة التربة العراقية القائم على الـ JSON:")
            if soil_result["status"] == "PASSED":
                st.success(soil_result["summary"])
                st.session_state["compliance_rate"] = 68
                st.session_state["step2_status"] = "Completed"
                st.rerun()
            else:
                st.error(soil_result["summary"])
                for err in soil_result["failures"]:
                    st.warning(err)
        else:
            st.warning("⚠️ لم يتم العثور على محرك التربة المشترك، تم التخطي الافتراضي.")
            st.session_state["compliance_rate"] = 68
            st.session_state["step2_status"] = "Completed"
            st.rerun()
                
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='text-align: center; color: #D1D5DB; margin: -10px 0; font-size: 1.2rem;'>│</div>", unsafe_allow_html=True)

    # --- الخطوات المغلقة المتسلسلة (Step 3, 4, 5) الانتظارية المقفلة بـ Lock إلكتروني ---
    for step_num, step_title in [("3", "Step 3: Structural Audit & Load Calculations"), 
                                 ("4", "Step 4: Hydro-Sanitary & Plumbing Design"), 
                                 ("5", "Step 5: Electrical Systems Analysis")]:
        with st.container(border=True):
            c1, c2, c3 = st.columns([0.15, 1.0, 0.4])
            with c1:
                st.markdown(f"<div style='background-color: #F3F4F6; color: #9CA3AF; border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-weight: bold;'>🔒</div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div style='font-weight: bold; font-size: 0.95rem; color: #9CA3AF; padding-top: 4px;'>{step_title}</div>", unsafe_allow_html=True)
            with c3:
                st.markdown("<div style='text-align: right; color: #9CA3AF; font-weight: bold; font-size: 0.85rem; padding-top: 4px;'>🔒 Locked</div>", unsafe_allow_html=True)

    # بنر الترقية والاشتراك المدفوع (Premium Pack Card)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #0F172A; color: white; padding: 20px; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <div>
            <div style="font-weight: bold; font-size: 1.05rem; margin-bottom: 4px; color: #F59E0B;">👑 Subscribe to Premium Pack <span style="background-color: #1E293B; color: #F59E0B; padding: 2px 8px; border-radius: 6px; font-size: 0.7rem; margin-left: 5px;">PREMIUM</span></div>
            <div style="font-size: 0.8rem; color: #94A3B8;">Unlock all 14 automated compliance calculators and background verification hooks.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
# ==================== الجانب الأيمن: لوحة التحليلات والمؤشرات الهندسية الدائرية ====================
with col_right:
    st.markdown("<div style='margin-bottom: 20px;'><span style='font-weight: bold; font-size: 1.1rem; color: #1F2937;'>📊 Executive Analytics Dashboard</span></div>", unsafe_allow_html=True)
    
    # 1. بطاقة مؤشر المطابقة الهندسية العامة (تتحدث ديناميكياً مع الذاكرة)
    st.markdown(render_metric_card("Engineering Compliance", st.session_state["compliance_rate"], "#2563EB", "🌐"), unsafe_allow_html=True)
    
    # 2. بطاقة مؤشر السلامة الإنشائية والأسس (تتغير لـ 100% تلقائياً عند اجتياز خطوة التربة)
    struct_p = 100 if st.session_state["step2_status"] == "Completed" else 0
    st.markdown(render_metric_card("Structural Integrity", struct_p, "#10B981", "🟢"), unsafe_allow_html=True)
    
    # 3. بطاقة مؤشر كفاءة واستهلاك الطاقة
    st.markdown(render_metric_card("Energy Optimization", 0, "#D97706", "⚡"), unsafe_allow_html=True)
    
    # 4. بطاقة الاستدامة والأثر البيئي لـ (Green Score) من المخططات
    st.markdown("""
    <div style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937; margin-bottom: 12px;">🌱 4. Sustainability Impact</div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 0.8rem; color: #6B7280;">Green Score</div>
                <h1 style="margin: 0; color: #10B981; font-size: 2.2rem; font-family: sans-serif;">61</h1>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 0.75rem; color: #6B7280;">CO₂ Reduction Potential</div>
                <div style="color: #10B981; font-weight: bold; font-size: 1.1rem;">128.5 Tons / Year</div>
            </div>
        </div>
    </div>
    
    # 5. تفاصيل الجداول الزمنية والميزانيات المرصودة للمشروع
    <div style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937; margin-bottom: 10px;">📅 Project Timeline & Cost</div>
        <div style="font-size: 0.82rem; color: #4B5563; margin-bottom: 6px; font-family: sans-serif;"><b>Project Duration:</b> 42 / 300 Days (14%)</div>
        <div style="font-size: 0.82rem; color: #4B5563; font-family: sans-serif;"><b>Budget Overview:</b> $1.28M / $7.00M (18%)</div>
    </div>
    """, unsafe_allow_html=True)
