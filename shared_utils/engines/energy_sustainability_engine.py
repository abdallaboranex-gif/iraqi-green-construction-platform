# shared_utils/engines/energy_sustainability_engine.py
from shared_utils.iraqi_code_constants import DESIGN_TEMP_SUMMER

def calculate_energy_roi(building_area, insulation_type, amp_needed):
    """
    محرك حساب الوفر المالي والعائد من الاستثمار بناءً على تعرفة المولدات الأهلية في العراق
    """
    # تسعيرة الأمبير التقريبية للمولد الأهلي صيفاً في بغداد (بالدينار العراقي)
    AMPERE_TARIFF_IQD = 15000 
    
    # تحديد معامل كفاءة العزل الحراري (U-Value تقريبي)
    # الطابوق الجمهوري العادي أقل كفاءة من الثرمستون أو الطابوق المعزول
    if insulation_type == "طابوق عادي بدون عزل":
        u_value = 2.4
        cooling_reduction = 0.0  # لا يوجد توفير
    elif insulation_type == "ثرمستون (صديق للبيئة)":
        u_value = 0.8
        cooling_reduction = 0.25 # يوفر 25% من أحمال التكييف صيفاً
    else: # عزل حراري متكامل (بولسترين/صوف صخري)
        u_value = 0.3
        cooling_reduction = 0.45 # يوفر 45% من أحمال التكييف صيفاً

    # حساب التكلفة السنوية التقديرية للمولد الأهلي بدون عزل (لأشهر الصيف الخمسة الحارة)
    current_annual_generator_cost = amp_needed * AMPERE_TARIFF_IQD * 5
    
    # حساب الوفر في عدد الأمبيرات المطلوبة للتكييف صيفاً بعد العزل
    amperage_saved = round(amp_needed * cooling_reduction)
    new_amp_needed = amp_needed - amperage_saved
    
    # التكلفة السنوية الجديدة والوفر المالي بالدينار العراقي
    new_annual_generator_cost = new_amp_needed * AMPERE_TARIFF_IQD * 5
    annual_savings_iqd = current_annual_generator_cost - new_annual_generator_cost
    
    # حساب تكلفة تركيب العزل التقريبية وفترة استرداد رأس المال (Payback Period) بالسنوات
    insulation_installation_cost = building_area * 12000 # 12 ألف دينار للمتر المربع كمعدل
    
    if annual_savings_iqd > 0:
        payback_years = round(insulation_installation_cost / annual_savings_iqd, 1)
    else:
        payback_years = 0.0

    return {
        "u_value": u_value,
        "amperage_saved": amperage_saved,
        "new_amp_needed": new_amp_needed,
        "annual_savings_iqd": annual_savings_iqd,
        "payback_years": payback_years,
        "design_temp": DESIGN_TEMP_SUMMER
    }
