# pages/6_Site_Safety.py
import streamlit as st
import plotly.graph_objects as go

st.title("🦺 6. Site Safety & Environmental Inspector")
st.info("واجهة التفتيش الموقعي الذكي لمراقبة السلامة المهنية وإعادة تدوير النفايات الإنشائية المتوافقة مع محددات البيئة العراقية.")

col_checklist, col_waste = st.columns(2)

with col_checklist:
    with st.container(border=True):
        st.subheader("📋 القائمة التفتيشية للسلامة الموقعية (Safety Checklist)")
        st.caption("الحد الأدنى لالتزام المقاول بموقع العمل وفق مدونة السلامة المهنية:")
        
        # بنود فحص تفاعلية للمفتش الموقعي
        helmet_check = st.checkbox("خوذ حماية الرأس وسترات الأمان العاكسة لجميع العمال والمشرفين")
        scaffold_check = st.checkbox("تأمين السقالات والرافعات الإنشائية وفحص أحزمة الأمان للمرتفعات")
        heat_check = st.checkbox("توفير مظلات استراحة ونقاط مياه شرب باردة (بسبب حرارة الصيف 50°C)")
        fire_check = st.checkbox("وجود مطافئ الحريق وصناديق الإسعافات الأولية وتأمين الأسلاك الكهربائية")
        
        # حساب نسبة الالتزام الموقعي
        total_items = 4
        checked_items = sum([helmet_check, scaffold_check, heat_check, fire_check])
        safety_score = int((checked_items / total_items) * 100)
        
        st.markdown("---")
        st.metric(label="📊 مؤشر السلامة المهنية الفوري للموقع (Safety Score)", value=f"{safety_score}%")
        
        if safety_score == 100:
            st.success("🍏 الموقع مستوفي لشروط مدونة السلامة الموقعية وجاهز لمتابعة العمل.")
        elif safety_score >= 50:
            st.warning("⚠️ الموقع يحتوي على ثغرات سلامة؛ يرجى استكمال النواقص لتفادي الغرامات.")
        else:
            st.error("🚨 الموقع خطر جداً ومخالف! يجب إيقاف الأعمال الإنشائية فوراً لحين تأمين العمال.")

with col_waste:
    with st.container(border=True):
        st.subheader("🏗️ تقدير حجم تدوير الأنقاض والمخلفات البيئية")
        st.caption("حساب العائد البيئي للمقاول والدولة من إعادة تدوير مخلفات الهدم والبناء:")
        
        concrete_waste = st.number_input("أدخل حجم مخلفات الخرسانة والأنقاض المتوقعة بالموقع (طن):", min_value=1, max_value=10000, value=50)
        
        # نسبة إعادة تدوير قياسية 75% لتحويل الأنقاض إلى سبيس معتمد
        recycle_rate = 0.75
        recycled_amount = round(concrete_waste * recycle_rate, 1)
        
        # توفير 8,000 دينار عراقي عن كل طن يتم تدويره محلياً كبديل لشراء السبيس الجديد
        saved_money = int(recycled_amount * 8000)
        
        # رسم بياني دائري لتوزيع المخلفات
        fig_pie = go.Figure(go.Pie(
            labels=['أجزاء يعاد تدويرها (سبيس)', 'أنقاض غير قابلة للتدوير'],
            values=[recycled_amount, round(concrete_waste - recycled_amount, 1)],
            hole=.4,
            marker_colors=['#10B981', '#64748B']
        ))
        fig_pie.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),
            height=140,
            showlegend=False
        )
        st.plotly_chart(fig_pie, use_container_width=True, config={'displayModeBar': False})
        
        st.markdown("---")
        st.write(f"♻️ الكمية القابلة لإعادة التدوير واستخدامها هندسياً: **{recycled_amount} طن**")
        st.success(f"💰 الوفر المالي البيئي المقدر للمقاول: **{saved_money:,} دينار عراقي**")
