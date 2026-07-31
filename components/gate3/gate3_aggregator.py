# components/gate3/gate3_aggregator.py
import streamlit as st
import pandas as pd

def run_statistical_aggregator(lang):
    """المحرك المركزي لتسجيل القياسات التراكمية وبثها لذاكرة البوابة الرابعة الجغرافية"""
    
    # 🧠 قراءة مدخلات المعاملة الحية الحالية المخزنة في الجلسة العامة للمنصة
    current_gov = st.session_state.get("selected_gov", "Baghdad")
    current_width = st.session_state.get("land_width", 0.0)
    current_length = st.session_state.get("land_length", 0.0)
    current_area = current_width * current_length
    step2_stat = st.session_state.get("step2_status", "In Progress")
    
    # 📝 مصفوفة وقاعدة البيانات الإحصائية التاريخية لبلديات العراق
    analytics_db = {
        "Baghdad": {"name": "بغداد", "total": 1428, "passed": 1150, "failed": 278, "energy_save": "31%"},
        "Salah_Al_Din": {"name": "صلاح الدين", "total": 384, "passed": 242, "failed": 142, "energy_save": "35%"},
        "Najaf": {"name": "النجف الأشرف", "total": 512, "passed": 390, "failed": 122, "energy_save": "28%"},
        "Anbar": {"name": "الأنبار", "total": 296, "passed": 210, "failed": 86, "energy_save": "29%"},
        "Nineveh": {"name": "نينوى", "total": 415, "passed": 310, "failed": 105, "energy_save": "30%"},
        "Basra": {"name": "البصرة", "total": 620, "passed": 450, "failed": 170, "energy_save": "26%"},
        "Muthanna": {"name": "المثنى", "total": 145, "passed": 95, "failed": 50, "energy_save": "34%"}
    }
    
    # 📡 حقن داتا المعاملة الموقعية الحالية فورياً داخل سجل المحافظة المحددة
    if current_gov in analytics_db and current_area > 0:
        analytics_db[current_gov]["total"] += 1
        if step2_stat == "Completed":
            analytics_db[current_gov]["passed"] += 1
        else:
            analytics_db[current_gov]["failed"] += 1
            
    # قذف وبث الداتا الكاملة والمحدثة حياً إلى قناة الذاكرة العامة للبوابة الرابعة
    st.session_state["g4_streamed_telemetry"] = analytics_db
    return analytics_db
