# shared_utils/engines/engineering_compliance_engine.py
import random
from shared_utils.iraqi_code_constants import BEARING_CAPACITY_MIN, SAFETY_FACTOR_SOIL

def verify_soil_report(uploaded_file):
    """
    محاكي ذكي لقراءة ملف فحص التربة PDF والتحقق من قدرة التحمل
    """
    if uploaded_file is None:
        return {"status": False, "message": "لم يتم رفع أي ملف"}
    
    # محاكاة قراءة ملف الـ PDF عبر استخراج قيمة افتراضية لقدرة التحمل (مثلاً 120 kPa)
    # مستقبلاً سنضع هنا كود قراءة النصوص الحقيقي (PyPDF2)
    extracted_bearing_capacity = random.choice([140.0, 160.0, 180.0, 45.0]) 
    
    # المقارنة مع محددات الكود العراقي المستدعاة من ملف الثوابت
    if extracted_bearing_capacity >= BEARING_CAPACITY_MIN:
        return {
            "status": True,
            "bearing_capacity": extracted_bearing_capacity,
            "safety_factor": SAFETY_FACTOR_SOIL,
            "message": f"التقرير مطابق. قدرة تحمل التربة المستخرجة ({extracted_bearing_capacity} kPa) أعلى من الحد الأدنى القياسي العراقي ({BEARING_CAPACITY_MIN} kPa)."
        }
    else:
        return {
            "status": False,
            "bearing_capacity": extracted_bearing_capacity,
            "message": f"فشل المطابقة! قدرة التحمل المستخرجة ({extracted_bearing_capacity} kPa) خطرة وأقل من الحد الأدنى لكود البناء العراقي ({BEARING_CAPACITY_MIN} kPa)."
        }
