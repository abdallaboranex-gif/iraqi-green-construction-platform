# components/sidebar_metrics.py
import streamlit as st

def render_metric_card(title, percentage, color, icon, lang):
    """بناء الحلقات الدائرية الذكية للتقدم الإنشائي المتوافقة بصرياً مع اتجاه الواجهة"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    progress_txt = "نسبة التقدم الإجمالية" if lang == "AR" else "Overall Progress"
    
    return f"""
    <div dir="{direction}" style="background-color: white; padding: 12px; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05); text-align: {align};">
        <div>
            <div style="font-weight: bold; font-size: 0.9rem; color: #1F2937; margin-bottom: 3px;">{icon} {title}</div>
            <div style="font-size: 0.75rem; color: #6B7280;">{progress_txt}</div>
        </div>
        <div style="position: relative; width: 55px; height: 55px; border-radius: 50%; background: conic-gradient({color} {percentage * 3.6}deg, #E5E7EB 0deg); display: flex; align-items: center; justify-content: center;">
            <div style="position: absolute; width: 41px; height: 41px; border-radius: 50%; background-color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.85rem; color: #1F2937; font-family: sans-serif;">
                {percentage}%
            </div>
        </div>
    </div>
    """

def render_sidebar_analytics(L, lang):
    """رسم لوحة التحليلات الحية والطقس والمؤشرات السيادية للجانب الأيمن"""
    direction = "rtl" if lang == "AR" else "ltr"
    align_text = "right" if lang == "AR" else "left"
    align_opposite = "left" if lang == "AR" else "right"
    
    st.markdown(f"<h5 style='color: #1F2937; text-align: {align_text};'>📊 {L['dashboard_title']}</h5>", unsafe_allow_html=True)
    
    # 1. كروت الحلقات الدائرية المتوازية للتقدم والمطابقة الإنشائية
    st.markdown(render_metric_card(L['eng_comp'], st.session_state["compliance_rate"], "#2563EB", "🌐", lang), unsafe_allow_html=True)
    
    struct_p = 100 if st.session_state["step2_status"] == "Completed" else 0
    struct_title = "السلامة الإنشائية والأسس" if lang == "AR" else "Structural Integrity"
    st.markdown(render_metric_card(struct_title, struct_p, "#10B981", "🟢", lang), unsafe_allow_html=True)
    
    # 2. كرت الأثر البيئي ومؤشر انبعاثات الكربون الأخضر (Green Score)
    st.markdown(f"""
    <div dir="{direction}" style="background-color: white; padding: 12px; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); text-align: {align_text};">
        <div style="font-weight: bold; font-size: 0.9rem; color: #1F2937; margin-bottom: 8px;">{L['sustainability_title']}</div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 0.75rem; color: #6B7280;">{L['green_score']}</div>
                <h2 style="margin: 0; color: #10B981; font-size: 1.8rem; font-family: sans-serif;">61</h2>
            </div>
            <div style="text-align: {align_opposite};">
                <div style="font-size: 0.7rem; color: #6B7280;">{L['co2_reduction']}</div>
                <div style="color: #10B981; font-weight: bold; font-size: 1rem;">{L['co2_val']}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3. 🌤️ كرت جغرافية طقس ومناخ العراق الحي والمرتبط برطوبة الأسس والصب الخرساني
    st.markdown(f"""
    <div dir="{direction}" style="background-color: #EFF6FF; padding: 12px; border-radius: 12px; border: 1px solid #BFDBFE; margin-bottom: 12px; text-align: {align_text};">
        <div style="font-weight: bold; font-size: 0.9rem; color: #1E40AF; margin-bottom: 5px;">🌤️ طقس وجو العراق الحي (مباشر)</div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 0.75rem; color: #1E3A8A;">درجة الحرارة الحالية في بغداد</div>
                <h3 style="margin: 0; color: #1E40AF; font-size: 1.6rem; font-family: sans-serif;">44°C</h3>
            </div>
            <div style="text-align: {align_opposite}; font-size: 0.75rem; color: #1E3A8A; leading: 14px;">
                <b>الرطوبة:</b> 18%<br>
                <b>حالة الجو:</b> صافٍ ومشمس ☀️<br>
                <span style="color:#D97706; font-weight:bold;">⚠️ تنبيه: تجنب صب الخرسانة ظهراً</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4. 📈 كرت المؤشرات التفاعلية الحية للمنصة (Platform Telemetry)
    st.markdown(f"""
    <div dir="{direction}" style="background-color: white; padding: 12px; border-radius: 12px; border: 1px solid #E5E7EB; margin-bottom: 12px; text-align: {align_text}; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 0.9rem; color: #1F2937; margin-bottom: 6px;">👥 المؤشرات الرقمية للمنصة الآن</div>
        <div style="font-size: 0.8rem; color: #4B5563; margin-bottom: 4px;"><b>المهندسين والمكاتب النشطة حالياً:</b> <span style="color:#2563EB; font-weight:bold; font-family:sans-serif;">1,428 مـهندس</span></div>
        <div style="font-size: 0.8rem; color: #4B5563;"><b>المعاملات تحت التدقيق الآن:</b> <span style="color:#2563EB; font-weight:bold; font-family:sans-serif;">384 معاملة رخصة</span></div>
    </div>
    """, unsafe_allow_html=True)

    # 5. 📅 كرت تفاصيل الميزانيات التخمينية والمشاريع تحت الإنشاء
    st.markdown(f"""
    <div dir="{direction}" style="background-color: white; padding: 12px; border-radius: 12px; border: 1px solid #E5E7EB; text-align: {align_text}; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <div style="font-weight: bold; font-size: 0.9rem; color: #1F2937; margin-bottom: 8px;">{L['timeline_title']}</div>
        <div style="font-size: 0.8rem; color: #4B5563; margin-bottom: 5px; font-family: sans-serif;"><b>{L['duration_lbl']}</b> {L['duration_val']}</div>
        <div style="font-size: 0.8rem; color: #4B5563; font-family: sans-serif;"><b>{L['budget_lbl']}</b> {L['budget_val']}</div>
        <div style="margin-top: 8px; font-size: 0.75rem; color: #6B7280; border-top: 1px dashed #E5E7EB; padding-top: 5px;">
            <b>المشاريع المرصودة تحت الإنشاء:</b> 12 مشروع سيادي في بغداد
        </div>
    </div>
    """, unsafe_allow_html=True)
