# shared_engines/compliance_engine.py
import json
import os

def load_iraqi_code_rules():
    """
    قراءة الدستور الرقمي الشامل من ملف الـ JSON المحدث
    """
    file_path = "iraqi_code_rules.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def verify_comprehensive_compliance(governorate_zone, soil_key, extracted_bearing_capacity, planned_height):
    """
    محرك التدقيق الآلي الشامل لمطابقة فحص التربة والمحددات البلدية للمحافظة
    """
    rules = load_iraqi_code_rules()
    geotech = rules.get("code_301_geotechnical", {})
    soil_profiles = geotech.get("soil_types", {})
    
    # 1. جلب محددات التربة الخاصة بالمنطقة من الدستور الرقمي
    selected_soil = soil_profiles.get(soil_key, {})
    if not selected_soil:
        return {"status": False, "message": "Unknown soil profile selected."}
        
    min_allowed_kpa = selected_soil.get("min_bearing_capacity_kpa", 50.0)
    recommended_foundation = selected_soil.get("recommended_foundation", "Raft")
    safety_factor = geotech.get("general_safety_factors", {}).get("shallow_foundations", 3.0)
    
    # 2. جلب المحددات البلدية للارتفاع
    municipal = rules.get("municipal_regulations", {})
    max_height_allowed = municipal.get("max_building_height_meters", 12.0)
    
    # 3. إجراء عملية الفحص الهندسي والبلدي المزدوج
    soil_check = extracted_bearing_capacity >= min_allowed_kpa
    height_check = planned_height <= max_height_allowed
    
    if soil_check and height_check:
        return {
            "status": True,
            "message": f"Verified in {governorate_zone}! Soil capacity ({extracted_bearing_capacity} kPa) matches local limits. Planned height ({planned_height}m) is within municipal limits. Recommended Foundation: {recommended_foundation}."
        }
    else:
        error_msg = "Compliance Failed: "
        if not soil_check:
            error_msg += f"Soil bearing capacity is below the required {min_allowed_kpa} kPa for this zone. "
        if not height_check:
            error_msg += f"Planned height exceeds the municipal maximum of {max_height_allowed} meters. "
        return {
            "status": False,
            "message": error_msg
        }
