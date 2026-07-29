# shared_utils/engines/data_anonymizer.py
import re

def anonymize_owner_data(raw_text):
    """
    محرك ذكي يقوم بإخفاء وتعمية البيانات الشخصية الحساسة للمالك والمهندس
    لحماية الخصوصية قبل رفعها للسحابة المركزية.
    """
    anonymized_text = raw_text
    
    # 1. إخفاء أرقام الهواتف العراقية (مثل آسيا سيل، زين، كورك) وتعويضها بـ [PHONE_HIDDEN]
    phone_pattern = r"(07\d{9})|(\+?9647\d{9})"
    anonymized_text = re.sub(phone_pattern, "[🔒 تم إخفاء رقم الهاتف للخصوصية]", anonymized_text)
    
    # 2. إخفاء الأرقام الوطنية الحساسة كالهوية أو البطاقة الموحدة (12 رقم)
    national_id_pattern = r"\b\d{12}\b"
    anonymized_text = re.sub(national_id_pattern, "[🔒 تم تعمية الرقم الوطني الحساس]", anonymized_text)
    
    return anonymized_text

def get_provincial_green_stats():
    """
    مجمّع البيانات المركزي لإحصاءات البناء الأخضر في المحافظات العراقية لعام 2026
    """
    # بيانات إحصائية تفاعلية تحاكي الواقع الإنشائي الحالي في العراق
    stats_data = {
        "المحافظة": ["بغداد", "البصرة", "نينوى", "النجف الأشرف", "كربلاء المقدسة", "أربيل"],
        "المشاريع المسجلة":,
        "نسبة الالتزام بالعزل (%)":,
        "الوفر الكربوني التراكمي (طن)": [12400, 9800, 3200, 4100, 5600, 11200]
    }
    return stats_data
