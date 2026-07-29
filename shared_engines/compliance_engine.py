# shared_engines/compliance_engine.py
import json
import os

def load_iraqi_code_rules():
    """
    دالة مركزية آمنة لقراءة الدستور الرقمي من ملف الـ JSON
    """
    file_path = "iraqi_code_rules.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def verify_structural_and_soil(extracted_bearing_capacity):
    """
    محرك تدقيق فحص التربة والأسس بمطابقة أرقام المختبر مع محددات الكود العراقي
    """
    rules = load_iraqi_code_rules()
    geo_rules = rules.get("geotechnical_standards", {})
    min_allowed = geo_rules.get("min_bearing_capacity_kpa", 50.0)
    safety_factor = geo_rules.get("standard_safety_factor", 3.0)
    
    if extracted_bearing_capacity >= min_allowed:
        return {
            "status": True,
            "bearing_capacity": extracted_bearing_capacity,
            "safety_factor": safety_factor,
            "message": f"Verified: Extracted capacity ({extracted_bearing_capacity} kPa) complies with Iraqi Code minimum ({min_allowed} kPa)."
        }
    else:
        return {
            "status": False,
            "bearing_capacity": extracted_bearing_capacity,
            "message": f"Rejected: Extracted capacity ({extracted_bearing_capacity} kPa) is dangerous and below Iraqi Code minimum ({min_allowed} kPa)."
        }
