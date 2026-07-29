import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Iraqi Green Construction Platform", page_icon="🏗️", layout="wide")

# 2. Strict Navigation Routing based on our final tree architecture
pg = st.navigation([
    st.Page("pages/1_Compliance_Gate.py", title="1. Engineering Compliance Gate", icon="🏢"),
    st.Page("pages/2_Energy_Management.py", title="2. Energy & Sustainability", icon="⚡"),
    st.Page("pages/3_Central_Cloud.py", title="3. Central Cloud Data", icon="☁️"),
    st.Page("pages/4_Executive_Dashboard.py", title="4. Executive Dashboard", icon="📊"),
    st.Page("pages/5_Government_Portal.py", title="5. Government Link & Reports", icon="🏛️"),
    st.Page("pages/6_Site_Safety.py", title="6. Site Safety & Environment", icon="🦺")
])

pg.run()
