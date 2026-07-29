# shared_engines/energy_engine.py
import json
import os

def load_insulation_rules():
    """
    قراءة محددات العزل الحراري صيفاً من ملف الدستور الرقمي JSON
    """
    file_path = "iraqi_code_rules.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            rules = json.load(f)
            return rules.get("thermal_insulation", {})
    return {}

def calculate_cooling_and_roi(building_area, insulation_material, current_amps):
    """
    محرك هندسي يحسب الوفر المالي والأمبيري بناءً على جودة العزل صيفاً في العراق
    """
    insulation_rules = load_insulation_rules()
    design_temp = insulation_rules.get("design_summer_temp_celsius", 50.0)
    amp_tariff = insulation_rules.get("generator_amp_tariff_iqd", 15000)
    
    # تحديد معامل الكسب الحراري ونسبة التوفير التقديرية بناءً على مادة الجدران
    if insulation_material == "طابوق عادي بدون عزل":
        u_value = 2.4
        saving_ratio = 0.0
    elif insulation_material == "ثرمستون (صديق للبيئة)":
        u_value = 0.8
        saving_ratio = 0.25  # توفير 25% من الأحمال صيفاً
    else:  # عزل حراري متكامل (بولسترين أو صوف صخري)
        u_value = 0.3
        saving_ratio = 0.45  # توفير 45% من الأحمال صيفاً
        
    # حساب الوفر المالي والتكلفة السنوية التقديرية لأشهر الصيف الخمسة الحارة في العراق
    current_annual_cost = current_amps * amp_tariff * 5
    amperage_saved = round(current_amps * saving_ratio)
    new_amps_needed = current_amps - amperage_saved
    new_annual_cost = new_amps_needed * amp_tariff * 5
    
    annual_savings_iqd = current_annual_cost - new_annual_cost
    
    # حساب فترة استرداد رأس مال تركيب العزل بالسنوات (Payback Period)
    installation_cost = building_area * 12000  # معدل 12 ألف دينار للمتر المربع
    
    if annual_savings_iqd > 0:
        payback_years = round(installation_cost / annual_savings_iqd, 1)
    else:
        payback_years = 0.0
        
    return {
        "design_temp": design_temp,
        "u_value": u_value,
        "amperage_saved": amperage_saved,
        "new_amps_needed": new_amps_needed,
        "annual_savings_iqd": annual_savings_iqd,
        "payback_years": payback_years
    }
