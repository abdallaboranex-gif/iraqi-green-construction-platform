import streamlit as st

st.set_page_config(page_title="Iraqi Green Platform", page_icon="🏗️", layout="wide")

# إعداد نظام الصفحات المنفصلة لمنع تداخل الأكواد
pg = st.navigation([
    st.Page("pages/dashboard.py", title="1. Dashboard", icon="📊"),
    st.Page("pages/energy.py", title="2. Energy Management", icon="⚡"),
    st.Page("pages/cloud.py", title="3. Central Cloud", icon="☁️"),
    st.Page("pages/auth.py", title="5. Identity Auth", icon="🔐"),
    st.Page("pages/marketplace.py", title="5. Green Marketplace", icon="🛒")
])

pg.run()
