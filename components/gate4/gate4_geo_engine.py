# components/gate4/gate4_geo_engine.py
import streamlit as st

def calculate_national_telemetry():
    """المحرك الجغرافي والاقتصادي لـ غيت 4 - معالجة بث العدادات الوطنية ورصد تضخم المواد"""
    
    # 📡 التقاط بث البيانات الحية القادم فوراً من البوابة الثالثة الإحصائية
    telemetry_data = st.session_state.get("g4_streamed_telemetry", {})
    
    # حساب المجاميع الوطنية التراكمية بناءً على المعاملات المقبولة حياً
    total_houses = sum(v["total"] for v in telemetry_data.values()) if telemetry_data else 3784
    passed_cnt = sum(v["passed"] for v in telemetry_data.values()) if telemetry_data else 2739
    
    # ⚡ معادلة استشرافية: كل بيت مطابق لمدونة العزل يوفر حوالي 0.005 ميجاوات (5 kW) من ذروة الأحمال الصيفية
    total_mw_saved = passed_cnt * 0.005
    
    # 🧱 حساب المقنن التراكمي الإجمالي الفعلي لمواد البناء بالمشروعات المستوفية
    total_cement_tons = passed_cnt * 45  # معدل افتراضي 45 طن سمنت للبيت القياسي
    total_steel_tons = passed_cnt * 12   # معدل افتراضي 12 طن حديد تسليح للبيت القياسي
    
    # 📈 قاعدة بيانات استشرافية لرصد تضخم أسعار المواد في الأسواق العراقية حالياً (مقارنة بالعام الماضي)
    inflation_db = {
        "السمنت المقاوم العراقي (طن)": {"current": "135,000 د.ع", "change": "+8% (تضخم طفيف)"},
        "حديد التسليح السيادي (طن)": {"current": "980,000 د.ع", "change": "+14% (حرج/ارتفاع عالمي)"},
        "الطابوق الجف قيم الفاخر (ألف)": {"current": "160,000 د.ع", "change": "-2% (مستقر)"}
    }
    
    return {
        "total_houses": total_houses,
        "mw_saved": total_mw_saved,
        "cement": total_cement_tons,
        "steel": total_steel_tons,
        "inflation": inflation_db,
        "db": telemetry_data
    }
