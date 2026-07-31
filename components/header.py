# components/header.py
import streamlit as st

def initialize_language_state():
    """تفعيل ذاكرة الجلسة للغة النشطة إذا لم تكن موجودة سابقاً"""
    if "lang" not in st.session_state:
        st.session_state["lang"] = "EN"

def toggle_language():
    """دالة التبديل الفوري والذكي بضغطة زر واحدة"""
    st.session_state["lang"] = "AR" if st.session_state["lang"] == "EN" else "EN"

def get_translations():
    """قاموس المصطلحات المركزي لإدارة اللغتين في المنصة"""
    return {
        "EN": {
            "title": "🏢 Iraqi Green Construction Data Platform",
            "sub_title": "Data • Compliance • Sustainability • Efficiency",
            "loc_label": "📍 Current Project Location:",
            "loc_val": "Baghdad",
            "user_name": "Eng. Abdulla",
            "user_role": "Project Manager",
            "phase": "PHASE 1",
            "eng_comp": "Engineering Compliance",
            "seq_order": "(Strict Sequential Order)",
            "step1_title": "Step 1: Site Analysis & Zoning Regulations",
            "step1_desc": "Completed on 15 May 2026 • by Eng. Abdulla",
            "step2_title": "Step 2: Soil Inspection & Foundations",
            "step2_desc": "Please upload soil lab report or enter values for smart audit",
            "step3_title": "Step 3: Structural Audit & Load Calculations",
            "step4_title": "Step 4: Hydro-Sanitary & Plumbing Design",
            "step5_title": "Step 5: Electrical Systems Analysis",
            "completed": "🟢 Completed",
            "in_progress": "🟠 In Progress",
            "locked": "🔒 Locked",
            "dl_btn": "Download Site Report",
            "file_uploader_lbl": "(Soil Lab PDF) Drag and drop laboratory report here",
            "input_bearing": "Measured Soil Bearing Capacity (kPa):",
            "input_gypsum": "Total Gypsum Content in Soil (%):",
            "input_height": "Total Architectural Building Height (Meters):",
            "input_auth": "Soil Report Endorsement Status:",
            "auth_yes": "Authorized and Certified",
            "auth_no": "Not Certified / Unofficial",
            "run_audit": "🚨 Run Instant Code & Municipal Audit",
            "premium_title": "👑 Subscribe to Premium Pack",
            "premium_desc": "Unlock all 14 automated compliance calculators and background verification hooks.",
            "dashboard_title": "📊 Executive Analytics Dashboard",
            "sustainability_title": "🌱 4. Sustainability Impact",
            "green_score": "Green Score",
            "co2_reduction": "CO₂ Reduction Potential",
            "co2_val": "128.5 Tons / Year",
            "timeline_title": "📅 Project Timeline & Cost",
            "duration_lbl": "Project Duration:",
            "budget_lbl": "Budget Overview:",
            "duration_val": "42 / 300 Days (14%)",
            "budget_val": "$1.28M / $7.00M (18%)",
            "soil_report_header": "#### 🔬 Iraqi Soil Code Matching Report:"
        },
        "AR": {
            "title": "🏢 المنصة الرقمية لبيانات البناء الأخضر العراقي",
            "sub_title": "بيانات • مطابقة كودية • استدامة • كفاءة طاقة",
            "loc_label": "📍 نطاق المشروع الجغرافي الحالي:",
            "loc_val": "بغداد",
            "user_name": "م. عبد الله",
            "user_role": "مدير المشروع",
            "phase": "المرحلة الأولى",
            "eng_comp": "المطابقة والهندسة الإنشائية",
            "seq_order": "(نظام تعاقب الخطوات الإلزامي)",
            "step1_title": "الخطوة 1: تحليل الموقع والمحددات والتنظيمات البلدية",
            "step1_desc": "اكتملت في 15 أيار 2026 • بواسطة م. عبد الله",
            "step2_title": "الخطوة 2: فحص التربة والأسس الجيوتقنية",
            "step2_desc": "يرجى رفع ملف تقرير المختبر أو إدخال القيم للتدقيق الذكي",
            "step3_title": "الخطوة 3: التدقيق الإنشائي وحسابات الأحمال والجدران",
            "step4_title": "الخطوة 4: التصاميم الميكانيكية والصحية وشبكات الأنابيب",
            "step5_title": "الخطوة 5: التصاميم والمنظومات الكهربائية وتحليل الأحمال",
            "completed": "🟢 مكتمل",
            "in_progress": "🟠 قيد المعالجة",
            "locked": "🔒 مقفل إلكترونياً",
            "dl_btn": "تحميل تقرير الموقع المقر",
            "file_uploader_lbl": "(Soil Lab PDF) سحب وإفلات تقرير فحص التربة المختبري هنا",
            "input_bearing": "قدرة تحمل التربة المقاسة المختبرية (kPa):",
            "input_gypsum": "محتوى ونسبة الجبس الكلية في التربة (%):",
            "input_height": "الارتفاع الكلي للمبنى المعماري المصمم (متر):",
            "input_auth": "حالة اعتماد ومصادقة الختم الجيوتقني:",
            "auth_yes": "معتمد ومجاز ومصادق برقم نقابي حقيقي",
            "auth_no": "غير مصادق / فحص عشوائي غير رسمي",
            "run_audit": "🚨 تشغيل التدقيق الكودي والبلدي الفوري للمخططات",
            "premium_title": "👑 الاشتراك في الحزمة المهنية المدفوعة",
            "premium_desc": "تفعيل كافة الحاسبات الآلية الـ 14 للمطابقة الكودية المباشرة والربط الرقمي بالوزارات.",
            "dashboard_title": "📊 لوحة التحليلات والمؤشرات المركزية للتنفيذ",
            "sustainability_title": "🌱 4. الأثر البيئي ومؤشرات الاستدامة",
            "green_score": "التقييم الأخضر للمبنى",
            "co2_reduction": "إمكانيات خفض الانبعاثات الكاربونية",
            "co2_val": "128.5 طن / سنوياً برؤية بيئية",
            "timeline_title": "📅 الجداول الزمنية وميزانيات المشروع",
            "duration_lbl": "المدة الزمنية المنقضية للمشروع:",
            "budget_lbl": "ملخص الميزانية المرصودة والمستهلكة:",
            "duration_val": "42 / 300 يوم فعلي (14%)",
            "budget_val": "1.28 مليون $ / 7.00 مليون $ (18%)",
            "soil_report_header": "#### 🔬 تقرير مطابقة مدونة التربة والأسس العراقية القائم على الـ JSON:"
        }
    }

def render_header():
    """رسم وإخراج الشريط العلوي بالكامل وإدارة منطق الزر المفرد"""
    initialize_language_state()
    translations = get_translations()
    L = translations[st.session_state["lang"]]
    
    col_title, col_toggle_btn = st.columns([3, 1])
    
    with col_title:
        st.markdown(f"""
        <div>
            <h2 style="margin: 0; color: #1E3A8A; font-size: 1.6rem;">{L['title']}</h2>
            <div style="font-size: 0.85rem; color: #6B7280; margin-top: 2px;">{L['sub_title']}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_toggle_btn:
        btn_label = "Switch to العربية" if st.session_state["lang"] == "EN" else "الانتقال للغة الإنجليزية"
        st.button(btn_label, on_click=toggle_language, use_container_width=True, type="secondary")
        
    direction_top = "rtl" if st.session_state["lang"] == "AR" else "ltr"
    st.markdown(f"""
    <div dir="{direction_top}" style="display: flex; justify-content: flex-end; gap: 30px; margin-top: -15px; margin-bottom: 10px;">
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
