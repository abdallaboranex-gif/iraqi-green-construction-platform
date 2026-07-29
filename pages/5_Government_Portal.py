# pages/5_Government_Portal.py
import streamlit as st

st.title("🏛️ 5. Government Link & Reports Portal")
st.info("نظام المصادقة الإلكتروني الموحد لربط المديريات العامة للبلديات وأمانة بغداد لإصدار رخص البناء السيادية.")

# قراءة حالة فحص المخططات من الذاكرة المركزية الموحدة للمنصة
step2_completed = st.session_state.get("step2_completed", False)
compliance_rate = st.session_state.get("compliance_rate", 42)

with st.container(border=True):
    st.subheader("📜 تدقيق المعاملة وإصدار التقرير الفني النهائي المختوم")
    st.caption("الجهة التدقيقية المعتمدة: وزارة الإعمار والإسكان والبلديات العامة")
    
    project_id = st.text_input("أدخل رقم المعاملة البلدي الموحد:", value="IQ-BAGHDAD-2026-88")
    officer_notes = st.text_area("ملاحظات اللجنة التدقيقية المشتركة (اختياري):", value="تم فحص ومطابقة الارتدادات البلدية والمحددات البيئية لوسط العاصمة.")
    
    st.markdown("---")
    
    if st.button("🖨️ توليد وإصدار شهادة المطابقة الرسمية", type="primary"):
        if step2_completed:
            st.success(f"✅ **تمت المصادقة الرقمية بنجاح على المعاملة: {project_id}**")
            st.html(f"""
            <div style="background-color:#F0FDF4; border:2px solid #16A34A; padding:20px; border-radius:10px; margin-top:10px; font-family:sans-serif;">
                <h4 style="color:#16A34A; margin:0 0 10px 0; text-align:center;">📜 جمهورية العراق - تقرير مطابقة الكودات الهندسية</h4>
                <p style="margin:5px 0; color:#1E293B;"><b>رقم المعاملة:</b> {project_id}</p>
                <p style="margin:5px 0; color:#1E293B;"><b>معدل الامتثال الكلي:</b> {compliance_rate}%</p>
                <p style="margin:5px 0; color:#1E293B;"><b>حالة القرار الفني:</b> مطابق ومستوفي لكافة مدونات البناء العراقية (م.ع.د).</p>
                <p style="margin:5px 0; color:#1E293B;"><b>التوصية:</b> تُصدر إجازة البناء الإلكترونية فوراً وتسدد الرسوم البلدية.</p>
                <p style="margin:10px 0 0 0; font-size:12px; color:#64748B; text-align:center;">🔒 وثيقة معتمدة ومختومة إلكترونياً ومسجلة في السحابة السيادية المركزية لعام 2026</p>
            </div>
            """)
        else:
            st.warning(f"⚠️ **فشل إصدار التقرير للمعاملة: {project_id}**")
            st.html(f"""
            <div style="background-color:#FFFBEB; border:2px solid #D97706; padding:20px; border-radius:10px; margin-top:10px; font-family:sans-serif;">
                <h4 style="color:#D97706; margin:0 0 10px 0; text-align:center;">🛑 تقرير تعليق المعاملة الإنشائية الإدارية</h4>
                <p style="margin:5px 0; color:#1E293B;"><b>حالة القرار الفني:</b> غير مطابق للمواصفات الحالية.</p>
                <p style="margin:5px 0; color:#1E293B;"><b>سبب الرفض والتعليق الأولوي:</b> لم يتم إكمال فحص التربة والأسس أو أن الأرقام المدخلة تخالف محددات مدونة ميكانيك التربة (م.ع.د 301).</p>
                <p style="margin:5px 0; color:#1E293B;"><b>الإجراء المطلوب:</b> يرجى مراجعة البوابة الأولى ورفع تقرير مختبر تربة معتمد يطابق محددات المنطقة الإنشائية.</p>
            </div>
            """)
