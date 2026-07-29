# shared_engines/safety_engine.py
import re

def anonymize_citizen_data(raw_text):
    """
    محرك ذكي مخصص لحجب وتعمية البيانات الشخصية الحساسة (الهواتف والأرقام الوطنية)
    لحماية خصوصية المواطنين قبل رفع بيانات بيوتهم إلى السحابة المركزية.
    """
    anonymized_text = raw_text
    
    # 1. حجب أرقام الهواتف العراقية (مثل آسيا سيل، زين، كورك)
    phone_pattern = r"(07\d{9})|(\+?9647\d{9})"
    anonymized_text = re.sub(phone_pattern, "[🔒 PHONE_HIDDEN]", anonymized_text)
    
    # 2. حجب الأرقام الوطنية الحساسة كالبطاقة الموحدة (12 رقم)
    national_id_pattern = r"\b\d{12}\b"
    anonymized_text = re.sub(national_id_pattern, "[🔒 ID_HIDDEN]", anonymized_text)
    
    return anonymized_text

def get_provincial_consumption_stats():
    """
    مجمّع البيانات المركزي لإحصاءات استهلاك الطاقة والبناء الأخضر في المحافظات العراقية لعام 2026
    """
    stats_data = dict()
    stats_data["Governorate"] = ["Baghdad", "Basra", "Nineveh", "Najaf", "Karbala", "Erbil"]
    stats_data["Registered Projects"] = [1420, 850, 620, 510, 480, 790]
    stats_data["Insulation Compliance (%)"] = [68, 55, 42, 60, 65, 72]
    stats_data["CO2 Reduction (Tons/Year)"] = [3400, 1900, 1100, 1250, 1300, 2100]
    
    return stats_data
