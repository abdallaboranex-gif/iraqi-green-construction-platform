# main_portal.py
import streamlit as st

# توجيه محرك الملاحة السيادي للمنصة لفتح وتشغيل صفحة البوابات الموحدة فقط
pg = st.navigation([
    st.Page("pages/1_Compliance_Gate.py", title="بوابة الامتثال المركزي", icon="🏛️")
])

pg.run()
