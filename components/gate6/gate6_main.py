# components/gate6/gate6_main.py
import streamlit as st
from components.gate6.gate6_safety_engine import process_site_safety_audit

def render_safety_inspection_gate(L, lang, direction, align):
    """رسم وعرض واجهة الكشف الميداني الرقمي والتفتيش على السلامة الموقعية لـ غيت 6"""
    
    st.markdown(f"""
    <div class='compliance-card' style='text-align: {align};'>
        <h4 style='color: #DC2626; margin-top:0;'>📷 {L['gate_6_title']}</h4>
        <p style='color: #6B7280; font-size: 0.88rem;'>المنظومة الإلكترونية للرقابة الميدانية، مطابقة بنود السلامة المهنية، وإصدار الغرامات الفورية في مواقع البناء.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 📑 تفعيل قطاعات العرض بنظام الأزرار المقسمة (Tabs)
    tab_chk = "📋 1. استمارة بنود السلامة المهنية" if lang == "AR" else "📋 1. Safety Checklist"
    tab_cam = "📷 2. رفع توثيق الكشف المصور" if lang == "AR" else "📷 2. Live Site Photos"
    t_chk, t_cam = st.tabs([tab_chk, tab_cam])
    
    # ==================== 📋 التبويب الأول: استمارة بنود السلامة المهنية ====================
    with t_chk:
        st.markdown(f"<div style='text-align: {align}; padding-top:10px;'><b style='color:#1E3A8A;'>🧱 تدقيق الالتزام الميداني بمدونة السلامة العراقية:</b></div>", unsafe_allow_html=True)
        
        with st.container(border=True):
            fence = st.checkbox("توفر سياج حماية خارجي وحواجز تحذيرية للموقع لمنع سقوط المارة", value=True, key="chk_fence")
            ppe = st.checkbox("التزام الكادر والعمال بارتداء خوذ الأمان والأحذية الواقية الصارمة", value=True, key="chk_ppe")
            shoring = st.checkbox("تأمين دعامات جدران الحفر العميقة (Shoring) منعاً لتهدم التربة في السراديب", value=True, key="chk_shoring")
            
        safety_items = {"fence": fence, "ppe": ppe, "shoring": shoring}

    # ==================== 📷 التبويب الثاني: رفع توثيق الكشف المصور ====================
    with t_cam:
        st.markdown(f"<div style='text-align: {align}; padding-top:10px;'><b style='color:#1E3A8A;'>📷 كاميرا المفتش البلدي وتوثيق المخالفات:</b></div>", unsafe_allow_html=True)
        uploaded_ins_file = st.file_uploader("ارفع صورة حية من موقع الإنشاء (حديد التسليح، الحفر، الصب):", type=["jpg", "jpeg", "png"], key="g6_cam_file")
        has_violation_photo = st.checkbox("🚨 هل تؤكد الصورة المرفوعة وجود غش في مواد العزل أو شقوق إنشائية حاسمة؟", key="chk_g6_viol")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # 🚨 زر معالجة الفحص الفوري وإصدار العقوبات
    if st.button("🚨 تشغيل محرك المطابقة الميدانية وإصدار تقرير التفتيش البلدي", type="primary", use_container_width=True):
        safety_res = process_site_safety_audit(safety_items, has_violation_photo)
        
        if safety_res["status"] == "FAILED":
            st.error(safety_res["summary"])
            st.markdown(f"""
            <div class='compliance-card' style='border-right: 4px solid #DC2626;'>
                <h4 style='color:#DC2626; margin:0;'>💰 الغرامة المالية الفورية المفروضة: {safety_res['fine']}</h4>
                <p style='margin:10px 0; color:#991B1B; font-size:0.88rem;'>{safety_res['penalty']}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success(safety_res["summary"])
            st.info(safety_res["penalty"])
