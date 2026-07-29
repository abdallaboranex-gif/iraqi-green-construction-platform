# pages/4_Executive_Dashboard.py
import streamlit as st
import plotly.graph_objects as go

st.title("📊 4. Executive Dashboard")
st.info("الشاشة الرقابية التفاعلية المباشرة لمؤشرات الامتثال الحوكمي والاستدامة الوطنية لجمهورية العراق لعام 2026.")

# قراءة المتغيرات التفاعلية لحظياً من الذاكرة المؤقتة المعزولة والآمنة
compliance_rate = st.session_state.get("compliance_rate", 42)
step2_done = st.session_state.get("step2_completed", False)

# تجميع مصفوفة المخطط الخطي بناءً على قفزة التحديث الرقمية
chart_timeline = [
    st.session_state.get("val1", 10),
    st.session_state.get("val2", 20),
    st.session_state.get("val3", 30),
    st.session_state.get("val4", 35),
    st.session_state.get("val5", 42),
    st.session_state.get("val6", 42)
]

# تقسيم الشاشة التفاعلية إلى لوحتين رئيسيتين (المؤشرات البيانية / مسار التدقيق)
col_metrics, col_pipeline = st.columns(2)

with col_metrics:
    with st.container(border=True):
        st.subheader("🔵 Engineering Compliance Index")
        st.metric(label="معدل الامتثال الكلي للمشروع الحالي", value=f"{compliance_rate}%")
        
        # رسم بياني تفاعلي متجاوب يوضح قفزة التقدم لحظياً
        fig_line = go.Figure(go.Scatter(
            x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
            y=chart_timeline, 
            mode='lines+markers', 
            line=dict(color='#2563EB', width=3)
        ))
        fig_line.update_layout(
            margin=dict(l=10, r=10, t=10, b=10), 
            height=140, 
            xaxis_visible=False, 
            yaxis_visible=False, 
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_line, use_container_width=True, config={'displayModeBar': False})

with col_pipeline:
    with st.container(border=True):
        st.subheader("📋 مسار تقدم رخصة البناء الإلكترونية الموحدة")
        
        # محاكي تتابعي ذكي يتغير لحظياً بناءً على فحص البوابة الأولى
        st.markdown("🟢 **Step 1: Site Analysis & Setbacks** — Completed on 15 May • by Eng. Abdulla")
        
        if step2_done:
            st.markdown("🟢 **Step 2: Geotechnical & Soil Inspection** — Verified via Central Compliance Engine")
            st.markdown("🟠 **Step 3: Structural Load Calculations** — 🔓 Unlocked & Ready for Design")
        else:
            st.markdown("🟠 **Step 2: Geotechnical & Soil Inspection** — ⏳ In Progress (Awaiting Soil PDF Verification)")
            st.markdown("🔒 **Step 3: Structural Load Calculations** — Locked by Municipal Protocols")
            
        st.markdown("🔒 **Step 4: Hydro-Sanitary & Plumbing Regulations** — Locked")
        st.markdown("🔒 **Step 5: Electrical Systems & Phase Balance** — Locked")
