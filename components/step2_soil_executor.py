# components/step2_soil_executor.py
import streamlit as st

def run_soil_compliance_audit(L, lang, user_area, building_floors, selected_gov, lot_num_val, sector_num_val):
    """تشغيل التدقيق الكودي الفوري لتقرير فحص التربة والمطابقة مع ملف الإكسل وتوليد الـ PDF"""
    
    # سحب المدخلات المخزنة بأمان من ملف خطوة التربة المنفصل
    inputs = st.session_state.get("temp_soil_inputs", {})
    bearing_cap = inputs.get("bearing", 0)
    actual_bh_depth = inputs.get("depth", 0)
    report_status = inputs.get("status", "")
    gypsum = inputs.get("gypsum", 0.0)
    is_heavy_structure = inputs.get("is_heavy", False)
    water_table = inputs.get("water_table", 20.0)
    water_chem_status = inputs.get("water_chem", "مطابق وضمن الحدود الآمنة")

    # زر تشغيل الفحص والتحقق الرقمي السداسي المربوط بملف الإكسل
    if st.button(L['run_audit'], type="primary", use_container_width=True):
        if bearing_cap == 0 or actual_bh_depth == 0 or report_status == "":
            st.error("⚠️ يرجى إدخال كافة نتائج الفحوصات المختبرية وعمق الحفر والاعتمادية أولاً.")
        else:
            try:
                from shared_engines.compliance_engine import IraqiDynamicComplianceEngine
                excel_engine = IraqiDynamicComplianceEngine(excel_filename="soil_testing.xlsx")
                
                payload = {
                    "governorate": selected_gov, "total_land_area_m2": user_area, "soil_bearing_capacity": bearing_cap,
                    "soil_report_status": report_status, "actual_gypsum_percentage": gypsum, "is_heavy_structure": is_heavy_structure,
                    "actual_borehole_depth_meters": actual_bh_depth, "lot_num": lot_num_val, "sector_num": sector_num_val,
                    "building_floors": building_floors, "water_table_meters": water_table, "water_chemical_status": water_chem_status
                }
                
                soil_result = excel_engine.validate_soil_report(payload)
                st.markdown(L['soil_report_header'])
                
                if soil_result["status"] == "PASSED":
                    st.success(soil_result["summary"])
                    st.session_state["compliance_rate"], st.session_state["step2_status"] = 68, "Completed"
                    st.rerun()
                else:
                    st.error(soil_result["summary"])
                    pdf_path = excel_engine.generate_pdf_report(payload, soil_result, "Soil_Compliance_Failures.pdf")
                    with open(pdf_path, "rb") as f:
                        st.download_button(label="📥 تحميل تقرير المخالفات والرفض الرسمي (PDF)", data=f, file_name="Soil_Compliance_Failures.pdf", mime="application/pdf", use_container_width=True)
                    
                    for idx, failure in enumerate(soil_result["failures"], 1):
                        st.markdown(f"""
                        <div class='compliance-card'>
                            ### ⚠️ المخالفة {idx}: **{failure['title']}**<br>
                            <small style='color:#DC2626; font-weight:bold;'>{failure['severity']}</small><br>
                            💬 <b>للمواطن:</b> {failure['citizen_exp']}<br>
                            🔧 <b>للمهندس:</b> {failure['engineer_exp']}<br>
                            ✅ <b>طريقة الإصلاح:</b> {failure['resolution']}<br>
                            🚨 <b>العقوبة البلدية:</b> {failure['legal_penalty']}
                        </div>
                        """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"حدث خطأ في معالجة البيانات: {str(e)}")
