# pages/marketplace.py
import streamlit as st
import pandas as pd
from shared_utils.engines.market_analytics_engine import get_green_marketplace_products

st.title("🛒 Green Marketplace - الأسواق العراقية الخضراء")
st.info("دليل أسعار المواد الإنشائية المستدامة المتوفرة محلياً بالدينار العراقي لعام 2026.")

# جلب قاعدة بيانات المواد من المحرك الخلفي
products = get_green_marketplace_products()

# تقسيم الشاشة التفاعلية إلى عمودين
col_list, col_calc = st.columns(2)

with col_list:
    st.subheader("📦 الموارد المعتمدة بيئياً")
    for key, info in products.items():
        with st.container(border=True):
            st.markdown(f"### 🧱 {info['name']}")
            st.markdown(f"💰 **السعر التقديري:** {info['price_iqd']:,} IQD / {info['unit']}")
            st.caption(f"🌱 **التأثير البيئي:** {info['eco_benefit']}")

with col_calc:
    with st.container(border=True):
        st.subheader("🧮 حاسبة التكاليف التقديرية للمشروع")
        
        # اختيار المادة لحساب تكلفتها
        selected_item = st.selectbox(
            "اختر المادة الإنشائية المطلوبة:",
            ["Thermostone (ثرمستون معزول)", "DoubleGlazing (زجاج مزدوج)", "SolarSystem (منظومة طاقة شمسية)"]
        )
        quantity = st.number_input("أدخل الكمية المطلوبة بالتحديد:", min_value=1, value=10)
        
        # احتساب التكاليف البرمجية
        total_cost = 0
        if "Thermostone" in selected_item:
            total_cost = quantity * products["Thermostone"]["price_iqd"]
        elif "DoubleGlazing" in selected_item:
            total_cost = quantity * products["DoubleGlazing"]["price_iqd"]
        else:
            total_cost = quantity * products["SolarSystem"]["price_iqd"]
            
        st.markdown("---")
        st.metric(label="📊 إجمالي التكلفة المتوقعة بالدينار العراقي", value=f"{total_cost:,} IQD")
