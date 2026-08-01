# components/gate6/gate6_safety_engine.py
import streamlit as st

def process_site_safety_audit(safety_items, has_violation_photo):
    """المحرك الميداني لـ غيت 6 - تدقيق قائمة السلامة الموقعية وإصدار الغرامات الفورية"""
    
    # حساب عدد البنود غير المستوفاة في الموقع
    uncompliant_count = list(safety_items.values()).count(False)
    
    # تحديد حالة الموقع والغرامة المالية البلدية بموجب مدونة السلامة العراقية
    if uncompliant_count >= 2 or has_violation_photo:
        status = "FAILED"
        summary = "🚨 الموقع غير آمن! تم رصد مخالفات ميدانية حرجة تهدد سلامة العمال والمارة."
        # فرض غرامة مالية فورية (مثال: 500,000 دينار عراقي)
        fine_amount = "500,000 د.ع"
        penalty_txt = "⚠️ عقوبة بلدية: إيقاف العمل الفوري في موقع البناء وتجميد رخصة إجازة البناء رقمياً حتى تصحيح وضع السلامة ودفع الغرامة."
    else:
        status = "PASSED"
        summary = "🟢 الموقع مستوفٍ ومطابق تماماً لاشتراطات مدونة السلامة الموقعية والأمان المهني."
        fine_amount = "0 د.ع"
        penalty_txt = "✅ لا توجد عقوبات. الموقع مرخص لمتابعة أعمال الصب والإنشاء."
        
    return {
        "status": status,
        "summary": summary,
        "uncompliant_count": uncompliant_count,
        "fine": fine_amount,
        "penalty": penalty_txt
    }
