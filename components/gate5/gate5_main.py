# components/gate5/gate5_main.py
import streamlit as st
from components.gate5.gate5_billing_engine import calculate_sovereign_fees

def render_billing_gate(L, lang, direction, align):
    """رسم وعرض واجهة جباية الرسوم وبوابة الدفع الإلكتروني والاشتراكات لـ غيت 5"""
    
    st.markdown(f"""
    <div class='compliance-card' style='text-align: {align};'>
        <h4 style='color: #7C3AED; margin-top:0;'>💳 {L['gate_5_title']}</h4>
        <p style='color: #6B7280; font-size: 0.88rem;'>بوابة جباية الرسوم البلدية المأتمتة وإدارة الباقات السنوية للمكاتب الهندسية الاستشارية في العراق.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 1. استدعاء المعطيات المالية والوصولات من المحرك
    fee_res = calculate_sovereign_fees()
    
    # 📑 تفعيل قطاعات العرض بنظام الأزرار المقسمة (Tabs)
    tab_invoice = "🧾 1. كشف حساب ورسوم المعاملة الحالية" if lang == "AR" else "🧾 1. Current Transaction Invoice"
    tab_subs = "🏢 2. اشتراكات باقات المكاتب الاستشارية" if lang == "AR" else "🏢 2. Consultancy Subscription Plans"
    t_inv, t_sub = st.tabs([tab_invoice, tab_subs])
    
    # ==================== 🧾 التبويب الأول: فاتورة المعاملة الحالية ومحاكاة الدفع ====================
    with t_inv:
        st.markdown(f"<div style='text-align: {align}; padding-top:10px;'><b style='color:#1E3A8A;'>🧮 فاتورة تدقيق رخصة البناء ومطابقة المدونات:</b></div>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown(f"📐 <b>إجمالي مساحة العقار المستند إليها:</b> {fee_res['user_area']:.1f} m²", unsafe_allow_html=True)
            st.markdown(f"🏛️ <b>رسوم التدقيق الفني الكودي للبلدية:</b> {fee_res['base_fee']:,.0f} د.ع", unsafe_allow_html=True)
            st.markdown(f"🏷️ <b>رسم الطابع النقابي والمصادقة السيادية:</b> {fee_res['stamp_fee']:,.0f} د.ع", unsafe_allow_html=True)
            st.markdown(f"<h4 style='color:#7C3AED; margin:10px 0;'>💰 إجمالي مبلغ الجباية المستحق: {fee_res['total_fee']:,.0f} د.ع</h4>", unsafe_allow_html=True)
            
        # محاكاة واجهة الدفع الإلكتروني الرسمي (POS Gateway)
        pay_method = st.selectbox("💳 اختر وسيلة الدفع الإلكتروني المفعلة:", ["", "بطاقة ماستر كارد / فيزا كارد (الرافدين والرشيد)", "زين كاش (Zain Cash QuickPay)", "بوابة الدفع السيادية الموحدة للبنك المركزي"])
        
        if st.button("🚀 تأكيد الدفع وجباية الرسوم البلدية إلكترونياً", type="primary", use_container_width=True):
            if pay_method == "":
                st.error("⚠️ يرجى تحديد وسيلة الدفع الإلكتروني أولاً لإتمام تصفية القيد المالي.")
            else:
                st.success(f"🟢 تم الدفع الإلكتروني بنجاح تام! رقم صك الإيصال المشفر: {fee_res['receipt_id']}")
                st.info(f"💾 تم إلحاق باركود الـ QR والوصول الرقمي بملف المعاملة لإصدار الإجازة البلدية.")

    # ==================== 🏢 التبويب الثاني: باقات واشتراكات المكاتب الاستشارية ====================
    with t_sub:
        st.markdown(f"<div style='text-align: {align}; padding-top:10px;'><b style='color:#1E3A8A;'>👑 باقات الاستفادة المهنية للمؤسسات والمكاتب الهندسية:</b></div>", unsafe_allow_html=True)
        for plan_name, info in fee_res["plans"].items():
            with st.container(border=True):
                st.markdown(f"<b style='color:#7C3AED; font-size:0.95rem;'>🌟 {plan_name}</b>", unsafe_allow_html=True)
                st.markdown(f"💳 <b>الكلفة السنوية:</b> {info['price']}", unsafe_allow_html=True)
                st.markdown(f"✅ <b>الميزات:</b> {info['perks']}", unsafe_allow_html=True)
                st.button(f"🛒 تجديد الاشتراك أو الترقية الحية لـ {plan_name.split()[1] if len(plan_name.split())>1 else 'الباقة'}", use_container_width=True)
