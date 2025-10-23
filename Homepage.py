import streamlit as st

st.set_page_config(page_title="🚤 Boat Booking App")

st.title("🚤 Boat Booking System")
st.write("จองเรือเที่ยวเกาะง่าย ๆ ได้ในไม่กี่คลิก!")

st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", use_container_width=True)

st.sidebar.success("เลือกหน้าเมนูด้านบน 👆")
st.markdown("### 🔹 เมนู")
st.markdown("- หน้าแรก (Home)\n- จองเรือ (Booking)\n- ติดต่อเรา (Contact)")
