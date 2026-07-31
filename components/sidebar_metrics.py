# components/sidebar_metrics.py
import streamlit as st

def render_metric_card(title, percentage, color, icon, lang):
    """دالة بناء الحلقات الدائرية الذكية بنظام HTML متوافق مع اتجاه اللغة"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    progress_txt = "نسبة التقدم الإجمالية" if lang == "AR" else "Overall Progress"
    
    return f"""
    <div dir="{direction}" style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05); text-align: {align};">
        <div>
            <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937; margin-bottom: 5px;">{icon} {title}</div>
            <div style="font-size: 0.8rem; color: #6B7280;">{progress_txt}</div>
        </div>
        <div style="position: relative; width: 60px; height: 60px; border-radius: 50%; background: conic-gradient({color} {percentage * 3.6}deg, #E5E7EB 0deg); display: flex; align-items: center; justify-content: center;">
            <div style="position: absolute; width: 46px; height: 46px; border-radius: 50%; background-color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95rem; color: #1F2937; font-family: sans-serif;">
                {percentage}%
            </div>
        </div>
    </div>
    """

def render_sidebar_analytics(L, lang):
    """رسم كامل كروت قطاع التحليلات والمؤشرات للجانب الأيمن"""
    st.markdown(f"<h4>{L['dashboard_title']}</h4>", unsafe_allow_html=True)
    
    # 1. كرت المطابقة الهندسية العامة (يقرأ من الذاكرة الحية)
    st.markdown(render_metric_card(L['eng_comp'], st.session_state["compliance_rate"], "#2563EB", "🌐", lang), unsafe_allow_html=True)
    
    # 2. كرت السلامة الإنشائية والأسس (يتحول إلى 100% تلقائياً عند اكتمال فحص التربة)
    struct_p = 100 if st.session_state["step2_status"] == "Completed" else 0
    struct_title = "السلامة الإنشائية والأسس" if lang == "AR" else "Structural Integrity"
    st.markdown(render_metric_card(struct_title, struct_p, "#10B981", "🟢", lang), unsafe_allow_html=True)
    
    # 3. كرت كفاءة وعزل الطاقة
    energy_title = "كفاءة وعزل الطاقة" if lang == "AR" else "Energy Optimization"
    st.markdown(render_metric_card(energy_title, 0, "#D97706", "⚡", lang), unsafe_allow_html=True)
    
    # 4. كرت الأثر البيئي والاستدامة (Green Score)
    direction = "rtl" if lang == "AR" else "ltr"
    align_text = "left" if lang == "AR" else "right"
    
    st.markdown(f"""
    <div dir="{direction}" style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937; margin-bottom: 12px;">{L['sustainability_title']}</div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 0.8rem; color: #6B7280;">{L['green_score']}</div>
                <h1 style="margin: 0; color: #10B981; font-size: 2.2rem; font-family: sans-serif;">61</h1>
            </div>
            <div style="text-align: {align_text};">
                <div style="font-size: 0.75rem; color: #6B7280;">{L['co2_reduction']}</div>
                <div style="color: #10B981; font-weight: bold; font-size: 1.1rem;">{L['co2_val']}</div>
            </div>
        </div>
    </div>
    
    # 5. كرت الجدول الزمني وتوزيع ميزانية الرخص
    <div dir="{direction}" style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 0.95rem; color: #1F2937; margin-bottom: 10px;">{L['timeline_title']}</div>
        <div style="font-size: 0.82rem; color: #4B5563; margin-bottom: 6px; font-family: sans-serif;"><b>{L['duration_lbl']}</b> {L['duration_val']}</div>
        <div style="font-size: 0.82rem; color: #4B5563; font-family: sans-serif;"><b>{L['budget_lbl']}</b> {L['budget_val']}</div>
    </div>
    """, unsafe_allow_html=True)
