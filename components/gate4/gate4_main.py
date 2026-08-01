# components/gate4/gate4_main.py
import streamlit as st
import pandas as pd
from components.gate4.gate4_geo_engine import calculate_national_telemetry

def render_sovereign_map_gate(L, lang, direction, align):
    """الواجهة النهائية التفاعلية للبوابة الرابعة - الخارطة ونظام الاستشراف الاقتصادي"""
    
    st.markdown(f"<div class='compliance-card' style='text-align: {align};'><h4 style='color: #047857; margin-top:0;'>🗺️ {L['gate_4_title']}</h4><p style='color: #6B7280; font-size: 0.88rem;'>نظام الاستشراف التخطيطي والرصد الفوري لتضخم الأسعار وكفاءة استهلاك الطاقة لجمهورية العراق.</p></div>", unsafe_allow_html=True)
    
    # 1. استدعاء القياسات من المحرك الاقتصادي المربوط بالبث
    res = calculate_national_telemetry()
    
    # 2. فرش عداد الأداء الوطني الشامل (البيوت، الميجاوات، والمقنن)
    st.markdown("<b style='color:#1E3A8A;'>📈 عداد الأداء الوطني والوفورات السيادية للدولة:</b>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1: st.metric(label="🏠 إجمالي البيوت المسجلة", value=f"{res['total_houses']:,} عقار")
    with m2: st.metric(label="⚡ مجموع الميجاوات الموفرة (MW)", value=f"{res['mw_saved']:.3f} MW", delta="كبح أحمال الذروة")
    with m3: st.metric(label="🧱 إجمالي مقنن الحديد المستهلك", value=f"{res['steel']:,} طن تسليح")
    
    # 3. نظام التنبيه والاستشراف التخطيطي الاقتصادي لتضخم الأسعار
    st.markdown("<br><b style='color:#DC2626;'>🚨 رادار الكشف والتنبيه الاقتصادي لتضخم مواد البناء في العراق:</b>", unsafe_allow_html=True)
    for mat, info in res["inflation"].items():
        st.markdown(f"<div class='compliance-card' style='margin-bottom:6px;'><b>{mat}:</b> الحالي: <span style='color:#2563EB;'>{info['current']}</span> | مؤشر التضخم: <span style='color:#DC2626; font-weight:bold;'>{info['change']}</span></div>", unsafe_allow_html=True)
        
    # 4. الخارطة الجغرافية الذكية وتوصيات دعم القرار لبلديات المحافظات
    st.markdown("<br><b style='color:#047857;'>🗺️ لوحة المراقبة الجغرافية التفاعلية للمحافظات:</b>", unsafe_allow_html=True)
    gov_list = ["بغداد", "صلاح الدين", "النجف الأشرف", "الأنبار", "نينوى", "البصرة"] if lang == "AR" else ["Baghdad", "Salah Al-Din", "Najaf", "Anbar", "Nineveh", "Basra"]
    selected_province = st.selectbox("🎯 اختر المحافظة لعرض نقاط البناء وتوصيات دعم القرار البلدي الحركي:", [""] + gov_list)
    
    if selected_province != "":
        st.markdown("<div class='compliance-card' style='border-right: 4px solid #047857;'><b>📢 توصية دعم القرار البلدي للمحافظ الاستشاري:</b> يتوجب التوجيه الفوري لبلدية المحافظة لتشديد الرقابة على أسعار السمنت والحديد الموقعي، مع إلزام الدوائر الهندسية بتسريع رخص الأبنية الخضراء لتحقيق قفزة في الوفورات الطاقية الوطنية قبل موسم الصيف القادم.</div>", unsafe_allow_html=True)
