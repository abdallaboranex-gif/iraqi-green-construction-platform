import streamlit as st
import plotly.graph_objects as go

st.title("📊 4. Executive Dashboard")
st.info("الشاشة الرقابية التفاعلية المباشرة لمؤشرات الامتثال والاستدامة الوطنية للمشاريع.")

rate = st.session_state.get("compliance_rate", 42)
is_done = st.session_state.get("step2_completed", False)

c1, c2 = st.columns(2)
with c1:
    with st.container(border=True):
        st.metric("🔵 Engineering Compliance", f"{rate}%")
        # رسم بياني متجاوب
        fig = go.Figure(go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], y=[10, 20, 30, 35, 42, rate], mode='lines+markers', line=dict(color='#2563EB')))
        fig.update_layout(margin=dict(l=5,r=5,t=5,b=5), height=100, xaxis_visible=False, yaxis_visible=False, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

with c2:
    with st.container(border=True):
        st.subheader("📋 مسار تقدم رخصة البناء الإلكترونية")
        st.write("🟢 **Step 1:** Site Analysis & Zoning — **Completed**")
        if is_done:
            st.write("🟢 **Step 2:** Soil Inspection & Foundations — **Completed**")
            st.write("🟠 **Step 3:** Structural Load Calculations — **Unlocked**")
        else:
            st.write("🟠 **Step 2:** Soil Inspection & Foundations — **In Progress**")
            st.write("🔒 **Step 3:** Structural Load Calculations — **Locked**")
