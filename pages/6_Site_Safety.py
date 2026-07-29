import streamlit as st

st.title("🦺 6. Site Safety & Environmental Inspector")
st.info("واجهة التفتيش الموقعي الذكي لمراقبة السلامة المهنية وإعادة تدوير النفايات الإنشائية.")

with st.container(border=True):
    st.subheader("🏗️ تقدير حجم النفايات الموقعية وإعادة التدوير")
    concrete_waste = st.number_input("حجم مخلفات الخرسانة والأنقاض المتوقعة في الموقع (طن):", min_value=1, value=25)
    recycle_rate = 0.70 # نسبة إعادة تدوير قياسية 70%
    
    recycled_amount = concrete_waste * recycle_rate
    saved_money = recycled_amount * 8000 # توفير 8 آلاف دينار لكل طن معاد تدويره في العراق
    
    st.markdown("---")
    st.write(f"♻️ الكمية القابلة لإعادة التدوير واستخدامها في السبيس: **{recycled_amount} طن**")
    st.success(f"💰 الوفر المالي البيئي للمشروع: **{saved_money:,} دينار عراقي!**")
