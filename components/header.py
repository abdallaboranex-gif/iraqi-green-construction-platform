# components/header.py
import streamlit as st

def initialize_language_state():
    """تفعيل وإرساء قيم الذاكرة الحية للغة والبوابات الست الافتتاحية للمنصة"""
    if "lang" not in st.session_state:
        st.session_state["lang"] = "AR"  # جعل العربية هي اللغة الافتراضية السيادية للمنصة
    if "active_gate" not in st.session_state:
        st.session_state["active_gate"] = "gate_1"  # تفعيل البوابة الأولى كشاشة افتراضية عند الفتح
    if "compliance_rate" not in st.session_state:
        st.session_state["compliance_rate"] = 42
    if "step2_status" not in st.session_state:
        st.session_state["step2_status"] = "In Progress"

def toggle_language():
    """دالة تحويل وتبديل اللغة الفورية بضغطة زر مفردة دون تكرار"""
    st.session_state["lang"] = "AR" if st.session_state["lang"] == "EN" else "EN"

def get_translations():
    """القاموس المركزي السيادي الشامل للمنصة والبوابات الست والمحددات الـ 12 للعقار"""
    return {
        "AR": {
            "title": "🏢 المنصة الرقمية السيادية للبناء الأخضر العراقي",
            "sub_title": "التحول الرقمي • المطابقة الكودية الآلية • كفاءة الطاقة والاستدامة الرصينة",
            "loc_label": "📍 النطاق الجغرافي المركزي للمشروع الحالي:",
            "loc_val": "بغداد / المنصور",
            "user_name": "م. عبد الله",
            "user_role": "رئيس مهندسي تدقيق رخص البناء والمدونات",
            
            # أسماء البوابات الست الاستراتيجية في الجانب الأيسر
            "gate_1_title": "📐 بوابة مطابقة الكودات الهندسية والمدونات العراقية",
            "gate_2_title": "🌱 بوابة إدارة الطاقة والاستدامة",
            "gate_3_title": "📊 بوابة البيانات الإحصائية والتحليلية للمشروعات",
            "gate_4_title": "🗺️ بوابة التحكم السيادية (خارطة العراق التفاعلية)",
            "gate_5_title": "💳 بوابة البنية التحتية والاشتراك والدفع الإلكتروني",
            "gate_6_title": "🔍 بوابة إدارة السلامة الموقعية والتفتيش الرقمي",
            
            # محددات بوابة المطابقة والفلترة الـ 12
            "phase": "المرحلة الأولى",
            "eng_comp": "الهندسة الإنشائية والمطابقة الكودية الآلية للرخص",
            "seq_order": "(نظام تعاقب الخطوات الإلزامي الصارم)",
            "step1_title": "الخطوة 1: تحليل الموقع والمحددات والتنظيمات البلدية",
            "step1_desc": "اكتملت في 15 أيار 2026 • بواسطة م. عبد الله",
            "step2_title": "الخطوة 2: فحص التربة والأسس الجيوتقنية المختبرية",
            "step2_desc": "بوابة التحقق ومطابقة ميكانيك التربة والخصائص الكيميائية الحركية",
            "step3_title": "الخطوة 3: التدقيق الإنشائي وحسابات الأحمال وجدران الأبنية",
            "step4_title": "الخطوة 4: التصاميم الميكانيكية والصحية وشبكات الأنابيب والمياه",
            "step5_title": "الخطوة 5: التصاميم والمنظومات الكهربائية وتحليل أحمال الشبكة",
            "completed": "🟢 مكتمل ومطابق",
            "in_progress": "🟠 قيد المعالجة والتدقيق",
            "locked": "🔒 مقفل إلكترونياً بالتسلسل الكودي",
            "dl_btn": "تحميل تقرير محددات الموقع المقر بلديّاً",
            "file_uploader_lbl": "(Soil Lab PDF) سحب وإفلات تقرير فحص التربة المختبري والمصادق عليه هنا",
            
            # حقول مدخلات الواجهة المحددة بدقة لطلبك
            "input_bearing": "قدرة تحمل التربة المقاسة المختبرية القصوى (kPa):",
            "input_gypsum": "محتوى ونسبة الجبس الكلية الكيميائية في التربة (%):",
            "input_height": "الارتفاع الكلي للمبنى المعماري المصمم من وجه الأرض (متر):",
            "input_auth": "حالة اعتماد ومصادقة الختم النقابي الجيوتقني:",
            "auth_yes": "معتمد ومجاز ومصادق برقم نقابي استشاري حقيقي",
            "auth_no": "غير مصادق / فحص مكتب عشوائي غير معتمد بلديّاً",
            "run_audit": "🚨 تشغيل التدقيق الكودي والبلدي الفوري الشامل للمخططات",
            "soil_report_header": "#### 🔬 تقرير مطابقة مدونة التربة والأسس العراقية القائم على ملف الإكسل والداتا الحية:"
        },
        "EN": {
            "title": "🏢 Sovereign Iraqi Green Construction Data Platform",
            "sub_title": "Digital Transformation • Automated Code Compliance • Sustainability & Efficiency",
            "loc_label": "📍 Geographic Project Scope Context:",
            "loc_val": "Baghdad / Mansour",
            "user_name": "Eng. Abdulla",
            "user_role": "Chief Construction Compliance Auditor",
            
            # Six Strategic Gate Names
            "gate_1_title": "📐 Iraqi Engineering Codes & Compliance Gate",
            "gate_2_title": "🌱 Energy Management & Sustainability Gate",
            "gate_3_title": "📊 Project Statistics & Analytics Gate",
            "gate_4_title": "🗺️ Sovereign Control Command (Interactive Iraq Map)",
            "gate_5_title": "💳 Infrastructure, Payment & Market Ecosystem Gate",
            "gate_6_title": "🔍 On-Site Safety & Digital Inspection Gate",
            
            # Compliance workflow vocabulary
            "phase": "PHASE 1",
            "eng_comp": "Structural Engineering & Automated Code Compliance",
            "seq_order": "(Strict Sequential Order Rules Activated)",
            "step1_title": "Step 1: Site Analysis & Zoning Regulations",
            "step1_desc": "Completed on 15 May 2026 • by Eng. Abdulla",
            "step2_title": "Step 2: Soil Inspection & Foundations Audit",
            "step2_desc": "Soil mechanics and geotechnical biochemical parameters gateway",
            "step3_title": "Step 3: Structural Audit & Load Calculations",
            "step4_title": "Step 4: Hydro-Sanitary & Plumbing Design",
            "step5_title": "Step 5: Electrical Systems Analysis & Load Distribution",
            "completed": "🟢 Completed & Compliant",
            "in_progress": "🟠 Under Active Audit Process",
            "locked": "🔒 Electronically Locked by Order",
            "dl_btn": "Download Endorsed Site Zoning Document",
            "file_uploader_lbl": "(Soil Lab PDF) Drag and drop certified geotechnical report here",
            
            # Inputs
            "input_bearing": "Measured Soil Bearing Capacity (kPa):",
            "input_gypsum": "Total Chemical Gypsum Content in Soil (%):",
            "input_height": "Total Architectural Building Height From Ground (meters):",
            "input_auth": "Geotechnical Report Endorsement Status:",
            "auth_yes": "Authorized and Certified by Syndicate",
            "auth_no": "Unverified / Non-certified Unofficial Lab",
            "run_audit": "🚨 Run Instant Code & Municipal Audit",
            "soil_report_header": "#### 🔬 Iraqi Soil Code Matching Report Generated from Live Database Asset:"
        }
    }

def render_header():
    """رسم وإخراج الشريط العلوي السيادي للمنصة بالكامل وإدارة زر تحويل اللغة"""
    initialize_language_state()
    translations = get_translations()
    L = translations[st.session_state["lang"]]
    
    col_title, col_toggle_btn = st.columns([3.5, 1.0])
    
    with col_title:
        st.markdown(f"""
        <div>
            <h2 style="margin: 0; color: #1E3A8A; font-size: 1.6rem;">{L['title']}</h2>
            <div style="font-size: 0.85rem; color: #6B7280; margin-top: 2px; font-weight: 500;">{L['sub_title']}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_toggle_btn:
        btn_label = "Switch to العربية" if st.session_state["lang"] == "EN" else "الانتقال للغة الإنجليزية"
        st.button(btn_label, on_click=toggle_language, use_container_width=True, type="secondary")
        
    direction_top = "rtl" if st.session_state["lang"] == "AR" else "ltr"
    st.markdown(f"""
    <div dir="{direction_top}" style="display: flex; justify-content: flex-end; gap: 30px; margin-top: -15px; margin-bottom: 5px;">
        <div>
            <span style="font-size: 0.78rem; color: #6B7280;">{L['loc_label']}</span>
            <span style="color: #10B981; font-weight: bold; font-size: 0.95rem; margin-left: 4px; margin-right: 4px;">{L['loc_val']}</span>
        </div>
        <div>
            <span style="font-weight: bold; font-size: 0.95rem; color: #1F2937;">{L['user_name']}</span>
            <span style="font-size: 0.78rem; color: #6B7280; margin-left: 4px; margin-right: 4px;">({L['user_role']})</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    return L
