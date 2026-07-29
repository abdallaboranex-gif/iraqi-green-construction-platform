# shared_utils/engines/data_anonymizer.py
import re

def anonymize_owner_data(raw_text):
    """
    محرك ذكي يقوم بإخفاء وتعمية البيانات الشخصية الحساسة للمالك والمهندس
    """
    anonymized_text = raw_text
    
    # حجب الهواتف العراقية
    phone_pattern = r"(07\d{9})|(\+?9647\d{9})"
    anonymized_text = re.sub(phone_pattern, "[🔒 تم إخفاء رقم الهاتف للخصوصية]", anonymized_text)
    
    # حجب الأرقام الوطنية
    national_id_pattern = r"\b\d{12}\b"
    anonymized_text = re.sub(national_id_pattern, "[🔒 تم تعمية الرقم الوطني الحساس]", anonymized_text)
    
    return anonymized_text

def get_provincial_green_stats():
    """
    مجمّع البيانات المركزي لإحصاءات البناء الأخضر في المحافظات العراقية لعام 2026
    """
    # تم صياغة البيانات هنا على شكل نصوص وقيم مباشرة لتفادي أي تشوه أثناء النقل
    stats_data = dict()
    stats_data["المحافظة"] = ["Baghdad", "Basra", "Nineveh", "Najaf", "Karbala", "Erbil"]
    stats_data["المشاريع المسجلة"] = [150, 85, 45, 60, 70, 95]
    stats_data["نسبة الالتزام بالعزل (%)"] = [65, 40, 35, 55, 60, 75]
    stats_data["الوفر الكربوني التراكمي (طن)"] = [450, 210, 115, 180, 230, 310]
    
    return stats_data
