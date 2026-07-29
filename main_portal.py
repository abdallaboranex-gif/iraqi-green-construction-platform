import streamlit as st

st.set_page_config(page_title="Iraqi Green Platform", page_icon="🏗️", layout="wide")

# استدعاء صفحة السوق المكتملة فقط في مجلد pages لمنع رسالة العثور على الملفات
pg = st.navigation([
    st.Page("pages/marketplace.py", title="Green Marketplace", icon="🛒")
])

pg.run()
