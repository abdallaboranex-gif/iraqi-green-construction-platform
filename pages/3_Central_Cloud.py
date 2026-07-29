import streamlit as st
import pandas as pd
from shared_engines.safety_engine import anonymize_citizen_data, get_provincial_consumption_stats

st.title("☁️ 3. Central Cloud Data Center")
st.info("مستودع البيانات السيادي وتفعيل خوارزمية تعمية الهوية لحماية الخصوصية.")

col_a, col_b = st.columns(2)
with col_a:
    with st.container(border=True):
        st.subheader("🔒 فلتر حجب البيانات الحساسة")
        raw_text = st.text_area("بيانات المالك والمهندس التجريبية للتدقيق:", value="المالك: محمد، هاتف: 07701234567، الرقم الوطني الموحد: 199512345678")
        if st.button("🔒 تشغيل الحجب"):
            st.code(anonymize_citizen_data(raw_text))

with col_b:
    with st.container(border=True):
        st.subheader("📈 الإحصاءات المجمّعة للمحافظات")
        df = pd.DataFrame(get_provincial_consumption_stats())
        st.dataframe(df, use_container_width=True, hide_index=True)
