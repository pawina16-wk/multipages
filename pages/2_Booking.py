import streamlit as st
from datetime import date

st.title("📝 จองเรือ")

st.markdown("กรุณากรอกข้อมูลเพื่อทำการจองเรือ")

# ฟอร์มจองเรือ
with st.form("booking_form"):
    name = st.text_input("ชื่อ-นามสกุล")
    people = st.number_input("จำนวนผู้โดยสาร", min_value=1, max_value=20, step=1)
    destination = st.selectbox("ปลายทาง", ["เกาะพีพี", "เกาะสิมิลัน", "เกาะลันตา", "เกาะไข่"])
    trip_date = st.date_input("วันที่เดินทาง", min_value=date.today())
    time = st.selectbox("รอบเวลาเดินทาง", ["เช้า (08:00)", "บ่าย (13:00)"])
    note = st.text_area("หมายเหตุเพิ่มเติม")
    submitted = st.form_submit_button("✅ ยืนยันการจอง")

if submitted:
    st.success(f"✅ ขอบคุณ {name} ระบบได้บันทึกการจองไปยัง {destination} เรียบร้อยแล้ว!")
    st.info(f"🕒 เดินทางวันที่ {trip_date} รอบ {time}")
