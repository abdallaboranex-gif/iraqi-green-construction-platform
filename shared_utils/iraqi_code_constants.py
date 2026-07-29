# shared_utils/iraqi_code_constants.py
# معاملات ومحددات كود البناء العراقي القياسي لعام 2026

# 1. محددات التربة والأسس القياسية (Geotechnical Base Constants)
BEARING_CAPACITY_MIN = 50.0   # الحد الأدنى المقبول لقدرة تحمل التربة (kPa) للأسس الشريطية
BEARING_CAPACITY_MAX = 350.0  # الحد الأعلى القياسي للتربة القوية جداً في العراق
SAFETY_FACTOR_SOIL = 3.0      # معامل الأمان القياسي لحسابات الأسس السطحية

# 2. معاملات الأحمال الإنشائية القياسية (Structural Load Factors)
DEAD_LOAD_FACTOR = 1.4        # معامل الحمل الميت وفق مواصفات الكود العراقي
LIVE_LOAD_FACTOR = 1.7        # معامل الحمل الحي للمباني السكنية والتجارية

# 3. محددات جغرافية ومناخية لمدينة بغداد (Baghdad Environmental Constants)
DESIGN_TEMP_SUMMER = 50.0     # درجة الحرارة القياسية للتصميم الحراري صيفاً (مئوية)
WIND_SPEED_BASE = 40.0        # سرعة الرياح التصميمية الأساسية في وسط العراق (m/s)
