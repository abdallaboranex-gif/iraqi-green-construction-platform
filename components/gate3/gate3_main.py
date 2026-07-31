# components/gate3/gate3_main.py
import streamlit as st
import pandas as pd
# استدعاء محرك التسجيل والبث المفصول داخل المجلد الفرعي الجديد
from components.gate3.gate3_aggregator import run_statistical_aggregator

def render_analytics_gate(L, lang, direction, align):
    """رسم وعرض لوحة العدادات والرسوم الإحصائية المركزية المعزولة لـ غيت 3"""
    
    st.markdown(f"""
    <div class='compliance-card' style='text-align: {align};'>
        <h4 style='color: #2563EB; margin-top:0;'>📊 {L['gate_3_title']}</h4>
        <p style='color: #6B7280; font-size: 0.88rem;'>المحرك المركزي المعزول لتسجيل القياسات التراكمية وبث المؤشرات حياً إلى خارطة العراق.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 1. تشغيل محرك التجميع الإحصائي وسحب قاعدة البيانات المحدثة
    analytics_db = run_statistical_aggregator(lang)
    
    # 2. حساب إجمالي العدادات الوطنية الموحدة
    total_all = sum(v["total"] for v in analytics_db.values())
    passed_all = sum(v["passed"] for v in analytics_db.values())
    failed_all = sum(v["failed"] for v in analytics_db.values())
    
    # 3. فرش قطاع الكروت التراكمية الفخمة للمسؤولين
    c1, c2, c3 = st.columns(3)
    with c1: st.metric(label="📊 إجمالي المعاملات المسجلة", value=f"{total_all:,} رخصة", delta="بث مستمر حركي")
    with c2: st.metric(label="🟢 رخص مستوفية ومقبولة", value=f"{passed_all:,} رخصة", delta="مطابقة كودية")
    with c3: st.metric(label="🔴 رخص مخالفة ومرفوضة", value=f"{failed_all:,} رخصة", delta="قيد التصحيح الفني", delta_color="inverse")

    # 4. فرش الرسم البياني الشريطي الفخم لمقارنة الكثافة بين بلديات العراق
    st.markdown(f"<br><b style='color:#1E3A8A;'>📉 مقارنة حجم وتوزيع رخص البناء المسجلة والمبثوثة حسب المحافظة:</b>", unsafe_allow_html=True)
    chart_df = pd.DataFrame([{"المحافظة": v["name"], "المقبولة": v["passed"], "المخالفة": v["failed"]} for v in analytics_db.values()])
    st.bar_chart(chart_df.set_index("المحافظة"), use_container_width=True)
    
    # 5. عرض جدول الترتيب والامتثال الجغرافي للمحافظات الـ 4 الأكثر نشاطاً
    st.markdown(f"<br><b style='color:#1E3A8A;'>🏢 ملخص الامتثال الرقمي حسب النطاق الجغرافي:</b>", unsafe_allow_html=True)
    prov_data = pd.DataFrame([{"المحافظة": v["name"], "المشاريع": v["total"], "كفاءة الامتثال": v["energy_save"]} for v in analytics_db.values() if v["total"] > 150])
    st.dataframe(prov_data, use_container_width=True, hide_index=True)
