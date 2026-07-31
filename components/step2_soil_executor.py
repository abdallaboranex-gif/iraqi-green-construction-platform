# components/step2_soil_executor.py
import streamlit as st

def run_soil_compliance_audit(L, lang, user_area, building_floors, selected_gov, lot_num_val, sector_num_val):
    """تشغيل التدقيق الكودي الفوري والربط الصحيح بالأسماء الحاكمة لجدول إكسل التربة"""
    
    # سحب المدخلات المخزنة بأمان من ذاكرة الجلسة
    inputs = st.session_state.get("temp_soil_inputs", {})
    
    # تصحيح وتأمين المطابقة البرمجية المباشرة لأسماء حقول الإكسل الحاكمة بالخلفية
    bearing_cap = inputs.get("bearing", 0)
    actual_bh_depth = inputs.get("depth", 0)
    report_status = inputs.get("status", "")
    gypsum = inputs.get("gypsum", 0.0)
    is_heavy_structure = inputs.get("is_heavy", False)
    water_table = inputs.get("water_table", 20.0)
    water_chem_status = inputs.get("water_chem", "مطابق وضمن الحدود الآمنة")

    # زر تشغيل الفحص والمطابقة
    if st.button(L['run_audit'], type="primary", use_container_width=True):
        if bearing_cap == 0 or actual_bh_depth == 0 or report_status == "":
            st.error("⚠️ يرجى إدخال كافة نتائج الفحوصات المختبرية وعمق الحفر والاعتمادية أولاً.")
        else:
            try:
                from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
                excel_engine = IraqiDynamicComplianceEngine(excel_filename="soil_testing.xlsx")
                
                # ربط حزمة المعطيات (Payload) بالأسماء المطابقة تماماً لكود الفحص البرمجي ومفاتيح الإكسل
                payload = {
                    "governorate": selected_gov,
                    "total_land_area_m2": user_area,
                    "soil_bearing_capacity": bearing_cap,  # التسمية الصحيحة المقررة في المحرك والإكسل
                    "soil_report_status": report_status, 
                    "actual_gypsum_percentage": gypsum,    # التسمية الجيوكيميائية المطابقة
                    "is_heavy_structure": is_heavy_structure,
                    "actual_borehole_depth_meters": actual_bh_depth,
                    "lot_num": lot_num_val,
                    "sector_num": sector_num_val,
                    "building_floors": building_floors,
                    "water_table_meters": water_table,
                    "water_chemical_status": water_chem_status
                }
                
                soil_result = excel_engine.validate_soil_report(payload)
                st.markdown(L['soil_report_header'])
                
                if soil_result["status"] == "PASSED":
                    st.success(soil_result["summary"])
                    st.session_state["compliance_rate"], st.session_state["step2_status"] = 68, "Completed"
                    st.rerun()
                else:
                    st.error(soil_result["summary"])
                    # توليد وتحميل تقرير المخالفات الرسمي (PDF)
                    pdf_path = excel_engine.generate_pdf_report(payload, soil_result, "Soil_Compliance_Failures.pdf")
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="📥 تحميل تقرير المخالفات والرفض الرسمي (PDF)", data=f, file_name="Soil_Compliance_Failures.pdf", mime="application/pdf", use_container_width=True)
                    
                    # طباعة الحاويات والرسائل السداسية العربية المستدعاة حياً من قلب الإكسل شيت
                    for idx, failure in enumerate(soil_result["failures"], 1):
                        st.markdown(f"""
                        <div class='compliance-card'>
                            <h3 style='margin:0; color:#DC2626;'>⚠️ المخالفة {idx}: {failure['title']}</h3>
                            <div style='background-color:#FEF2F2; padding:6px; border-right:4px solid #DC2626; margin:8px 0; font-weight:bold; font-size:0.85rem; color:#991B1B;'>{failure['severity']}</div>
                            <p style='margin:4px 0; font-size:0.88rem;'>💬 <b>شرح للمواطن:</b> {failure['citizen_exp']}</p>
                            <p style='margin:4px 0; font-size:0.88rem;'>🔧 <b>توجيه للمهندس:</b> {failure['engineer_exp']}</p>
                            <p style='margin:4px 0; font-size:0.88rem; color:#16A34A;'>✅ <b>مسار الإصلاح الفني:</b> {failure['resolution']}</p>
                            <p style='margin:4px 0; font-size:0.88rem; background-color:#FEE2E2; padding:6px; border-radius:4px; color:#991B1B;'>🚨 <b>الأثر والعقوبة البلدية:</b> {failure['legal_penalty']}</p>
                        </div>
                        """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"حدث خطأ في معالجة ومطابقة البيانات: {str(e)}")
