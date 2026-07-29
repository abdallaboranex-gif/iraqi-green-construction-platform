# shared_utils/rbac_rules.py

def verify_engineer_with_syndicate(membership_id):
    """
    محرك تفاعلي يحاكي التحقق الرقمي من هوية المهندس وعضويته في نقابة المهندسين العراقية
    """
    # عينات تجريبية لأرقام هويات النقابة المسجلة برمجياً
    valid_ids = dict()
    valid_ids["12345"] = "Baghdad"
    valid_ids["67890"] = "Basra"
    valid_ids["55555"] = "Nineveh"
    
    clean_id = str(membership_id).strip()
    
    if clean_id in valid_ids:
        province = valid_ids[clean_id]
        return {
            "verified": True,
            "province": province,
            "message": f"تم التحقق بنجاح! رقم العضوية {clean_id} نشط ومسجل في فرع {province}."
        }
    else:
        return {
            "verified": False,
            "province": None,
            "message": f"فشل التحقق! رقم العضوية {clean_id} غير مدرج في سجلات النقابة الرقمية."
        }

def get_role_permissions(role_name):
    """
    تحديد صلاحيات الاستخدام داخل المنصة بناءً على الرتبة الهندسية المعتمدة
    """
    permissions = dict()
    if role_name == "Project Manager":
        permissions["upload_docs"] = True
        permissions["run_calculators"] = True
        permissions["view_analytics"] = True
    elif role_name == "Auditor / Consultant":
        permissions["upload_docs"] = False
        permissions["run_calculators"] = True
        permissions["view_analytics"] = True
    else: # Guest / Investor
        permissions["upload_docs"] = False
        permissions["run_calculators"] = False
        permissions["view_analytics"] = True
        
    return permissions
