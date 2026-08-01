# components/gate5/gate5_billing_engine.py
import streamlit as st
import random

def calculate_sovereign_fees():
    """المحرك المالي لـ غيت 5 - حساب رسوم التدقيق وإصدار وصولات القبض المأتمتة"""
    
    # 🧠 قراءة مساحة الأرض الحية المخزنة بالجلسة العامة للعقار
    land_w = st.session_state.get("land_width", 0.0)
    land_l = st.session_state.get("land_length", 0.0)
    user_area = land_w * land_l if (land_w > 0 and land_l > 0) else 200.0
    
    # 📊 معادلة الجباية الرسمية المقرة: 500 دينار عراقي لكل متر مربع لتدقيق مدونات التربة والاستدامة
    base_audit_fee = user_area * 500
    stamp_fee = 25000  # رسم طابع نقابي ثابت لمعاملات البناء الأخضر
    total_fee = base_audit_fee + stamp_fee
    
    # توليد رقم صك مشفر وعشوائي لوصول القبض الإلكتروني الحكومي
    receipt_id = f"IRQ-PAY-{random.randint(100000, 999999)}"
    
    # مصفوفة الباقات والاشتراكات السنوية للمكاتب الاستشارية
    subscription_plans = {
        "باقة المكتب الاستشاري المعتمد": {"price": "350,000 د.ع / سنوياً", "perks": "تدقيق غير محدود للمخططات الإنشائية + دعم فني"},
        "باقة الشركات والمجمعات الاستثمارية الكبرى": {"price": "1,200,000 د.ع / سنوياً", "perks": "ربط مأتمت عبر الـ API السيادي + تقارير ذكاء أعمال"}
    }
    
    return {
        "user_area": user_area, "base_fee": base_audit_fee, "stamp_fee": stamp_fee,
        "total_fee": total_fee, "receipt_id": receipt_id, "plans": subscription_plans
    }
