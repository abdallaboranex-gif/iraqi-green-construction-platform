# shared_utils/engines/market_analytics_engine.py

def get_green_marketplace_products():
    """
    مخزن المنتجات والمواد الإنشائية الخضراء المستدامة المتوفرة في السوق العراقي لعام 2026
    """
    products = dict()
    
    # المنتج الأول: الثرمستون المعزول
    products["Thermostone"] = {
        "name": "ثرمستون عالي الكثافة (خفيف ومعزول)",
        "price_iqd": 110000,
        "unit": "متر مكعب",
        "eco_benefit": "يوفر حتى 25% من استهلاك التكييف صيفاً"
    }
    
    # المنتج الثاني: الزجاج المزدوج
    products["DoubleGlazing"] = {
        "name": "زجاج مزدوج محقون بغاز الأرجون (Double Glazing)",
        "price_iqd": 45000,
        "unit": "متر مربع",
        "eco_benefit": "يمنع نفاذ حرارة الصيف والضوضاء الخارجية"
    }
    
    # المنتج الثالث: منظومة طاقة شمسية
    products["SolarSystem"] = {
        "name": "منظومة طاقة شمسية هجينة (Hybrid 5kW)",
        "price_iqd": 3500000,
        "unit": "منظومة متكاملة",
        "eco_benefit": "تغنيك عن سحب الأمبيرات العالي من المولد الأهلي"
    }
    
    return products
