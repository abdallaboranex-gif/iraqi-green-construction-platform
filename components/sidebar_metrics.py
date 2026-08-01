import streamlit as st

def render_metric_card(title, percentage, color, icon, lang):
    """بناء الحلقات الدائرية المتوافقة بصرياً مع اتجاه وألوان الواجهة المطلوبة"""
    direction = "rtl" if lang == "AR" else "ltr"
    align = "right" if lang == "AR" else "left"
    progress_txt = "نسبة التقدم الإجمالية" if lang == "AR" else "Overall Progress"
    
    return f"""
    <div dir="{direction}" style="background-color: white; padding: 14px; border-radius: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02), 0 2px 4px -1px rgba(0,0,0,0.02); text-align: {align}; min-height: 105px;">
        <div>
            <div style="font-weight: 700; font-size: 0.88rem; color: #1E293B; margin-bottom: 4px;">{icon} {title}</div>
            <div style="font-size: 0.75rem; color: #64748B;">{progress_txt}</div>
        </div>
        <div style="position: relative; width: 52px; height: 52px; border-radius: 50%; background: conic-gradient({color} {percentage * 3.6}deg, #F1F5F9 0deg); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
            <div style="position: absolute; width: 38px; height: 38px; border-radius: 50%; background-color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.8rem; color: #0F172A; font-family: sans-serif;">
                {percentage}%
            </div>
        </div>
    </div>
    """

def render_sidebar_analytics(L, lang):
    """تحويل الجانب الأيمن إلى شبكة متطورة من عمودين ومؤشرات مطابقة للتصميم"""
    direction = "rtl" if lang == "AR" else "ltr"
    align_text = "right" if lang == "AR" else "left"
    align_opposite = "left" if lang == "AR" else "right"
    
    # تقسيم الواجهة إلى عمودين داخليين لتوزيع الكروت الـ 6 كمصفوفة متوازنة
    sub_col1, sub_col2 = st.columns(2, gap="small")
    
    with sub_col1:
        # 1️⃣ كرت الامتثال الهندسي
        st.markdown(render_metric_card(L['eng_comp'], st.session_state["compliance_rate"], "#3B82F6", "🔵", lang), unsafe_allow_html=True)
        
        # 3️⃣ كرت تحسين الطاقة
        st.markdown(f"""
        <div dir="{direction}" style="background-color: white; padding: 14px; border-radius: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); text-align: {align_text}; min-height: 105px;">
            <div style="font-weight: 700; font-size: 0.88rem; color: #1E293B; margin-bottom: 2px;">⚡ {"تحسين استهلاك الطاقة" if lang == "AR" else "Energy Optimization"}</div>
            <div style="display: flex; justify-content: space-between; align-items: baseline;">
                <div>
                    <div style="font-size: 0.72rem; color: #64748B;">{"التوفير المتوقع" if lang == "AR" else "Estimated Savings"}</div>
                    <div style="color: #10B981; font-weight: 700; font-size: 1.1rem; font-family: sans-serif;">27%</div>
                </div>
                <div style="color: #A7F3D0; font-size: 1.2rem; font-family: sans-serif;">📈</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 5️⃣ كرت إدارة التكاليف والميزانية
        st.markdown(f"""
        <div dir="{direction}" style="background-color: white; padding: 14px; border-radius: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); text-align: {align_text}; min-height: 105px;">
            <div style="font-weight: 700; font-size: 0.88rem; color: #1E293B; margin-bottom: 2px;">💳 {L['budget_lbl'] if lang == 'AR' else 'Cost Management'}</div>
            <div style="font-size: 0.72rem; color: #64748B; font-family: sans-serif;"><b>{L['budget_val']}</b></div>
            <div style="width: 100%; background-color: #F1F5F9; border-radius: 4px; height: 6px; margin-top: 8px;">
                <div style="width: 18%; background-color: #8B5CF6; height: 6px; border-radius: 4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with sub_col2:
        # 2️⃣ كرت السلامة الإنشائية والأسس
        struct_p = 100 if st.session_state["step2_status"] == "Completed" else 0
        struct_title = "السلامة الإنشائية" if lang == "AR" else "Structural Integrity"
        st.markdown(render_metric_card(struct_title, struct_p, "#10B981", "🟢", lang), unsafe_allow_html=True)
        
        # 4️⃣ كرت استدامة البيئة ونقاط الكربون
        st.markdown(f"""
        <div dir="{direction}" style="background-color: white; padding: 14px; border-radius: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); text-align: {align_text}; min-height: 105px;">
            <div style="font-weight: 700; font-size: 0.88rem; color: #1E293B; margin-bottom: 2px;">🌱 {L['sustainability_title']}</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 0.72rem; color: #64748B;">{L['green_score']}</div>
                    <div style="color: #10B981; font-weight: 700; font-size: 1.2rem; font-family: sans-serif;">61</div>
                </div>
                <div style="text-align: {align_opposite};">
                    <div style="font-size: 0.68rem; color: #64748B;">CO₂ / Year</div>
                    <div style="color: #475569; font-weight: 600; font-size: 0.75rem;">{L['co2_val']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 6️⃣ كرت الجدول الزمني للمشروع
        st.markdown(f"""
        <div dir="{direction}" style="background-color: white; padding: 14px; border-radius: 16px; border: 1px solid #E2E8F0; margin-bottom: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); text-align: {align_text}; min-height: 105px;">
            <div style="font-weight: 700; font-size: 0.88rem; color: #1E293B; margin-bottom: 2px;">📅 {L['timeline_title']}</div>
            <div style="font-size: 0.72rem; color: #64748B; font-family: sans-serif;"><b>{L['duration_lbl']}:</b> 42 / 300 Days</div>
            <div style="width: 100%; background-color: #F1F5F9; border-radius: 4px; height: 6px; margin-top: 8px;">
                <div style="width: 14%; background-color: #0EA5E9; height: 6px; border-radius: 4px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 🌤️ الطقس والتنبيهات الموقعية الهندسية أسفل الشبكة مباشرة
    st.markdown(f"""
    <div dir="{direction}" style="background-color: #EFF6FF; padding: 12px; border-radius: 14px; border: 1px solid #BFDBFE; margin-top: 4px; text-align: {align_text}; box-shadow: 0 2px 4px rgba(0,0,0,0.01);">
        <div style="font-weight: 700; font-size: 0.85rem; color: #1E40AF; margin-bottom: 4px;">🌤️ مؤشرات مناخ طقس العراق الحي</div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h4 style="margin: 0; color: #1E40AF; font-size: 1.3rem; font-family: sans-serif;">44°C</h4>
            </div>
            <div style="text-align: {align_opposite}; font-size: 0.72rem; color: #1E3A8A; line-height: 14px;">
                <b>رطوبة الأسس:</b> 18% | <b>الجو:</b> مشمس ☀️<br>
                <span style="color:#D97706; font-weight:700;">⚠️ إشعار فني: تجنب صب الخرسانة ظهراً</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
