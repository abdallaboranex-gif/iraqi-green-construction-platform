# pages/3_Cloud_Data_Center.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from shared_engines.safety_engine import anonymize_citizen_data, get_provincial_consumption_stats

st.title("☁️ 3. Central Cloud Data Center")
st.info("مستودع البيانات الوطني الموحد لمراقبة استهلاك الطاقة مع تفعيل خوارزميات تعمية الخصوصية السيادية.")

col_mask, col_stats = st.columns(2)

with col_mask:
    with st.container(border=True):
        st.subheader("🔐 نظام حماية الهوية والخصوصية الفوري")
        st.caption("ادخل بيانات المالك والمهندس لاختبار خوارزمية الحجب الفوري قبل رفع البيانات للسحابة:")
        
        raw_input = st.text_area(
            "بيانات المشروع التجريبية:", 
            value="المالك: علي حسن، هاتف: 07801234567، رقم البطاقة الموحدة: 199212345678، موقع المنشأ: بغداد"
        )
        
        if st.button("🔒 تشغيل فلتر الحجب والتعمية", type="primary"):
            masked_output = anonymize_citizen_data(raw_input)
            st.markdown("**📄 النص المشفّر الجاهز للتخزين السحابي:**")
            st.code(masked_output, language="text")
            st.success("✅ تم حجب البيانات الحساسة بنجاح للحفاظ على السرية السيادية!")

with col_stats:
    with st.container(border=True):
        st.subheader("📈 الإحصاءات المجمّعة للمحافظات العراقية")
        
        # جلب البيانات الحقيقية من المحرك المركزي المشترك
        raw_stats = get_provincial_consumption_stats()
        df = pd.DataFrame(raw_stats)
        
        # عرض جدول البيانات الحكومي المنظم
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # رسم بياني تفاعلي لترتيب المحافظات حسب الوفر الكربوني السنوي
        fig_prov = go.Figure(go.Bar(
            x=df["Governorate"], 
            y=df["CO2 Reduction (Tons/Year)"], 
            marker_color='#2563EB'
        ))
        fig_prov.update_layout(
            title="المحافظات الأعلى وفراً للكربون والطاقة لعام 2026",
            margin=dict(l=10, r=10, t=30, b=10), 
            height=180, 
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_prov, use_container_width=True, config={'displayModeBar': False})
