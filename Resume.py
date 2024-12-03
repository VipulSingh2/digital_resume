import streamlit as st

st.set_page_config("digital_resume",page_icon="📃",layout="centered")
col1,col2 = st.columns([3,1])
with col1:
    st.subheader("Name")
    st.title("Vipul Singh")
with col2:
    # st.image("new.png")
st.divider()
col1,col2,col3,col4 = st.columns([1.4,2,1,1])

with col1:
    st.write("📞 +91-8769521995")
with col2:
    st.write("✉️ vipulsingh592005@gmail.com")
  
with col3:
    st.markdown('<a href="https://www.openai.com" target="_blank">Vipul-Singh</a>', unsafe_allow_html=True)
with col4:
    st.markdown("VipulSingh2")
st.divider()
st.header("📚Education")
col1,col2 = st.columns([3,1])
with col1:
    st.write("Modern Institute of Technology & Research Center")
    st.write("B.Tech - Artificial Intelligence and Data Science")
    st.write("Ajit Public School,Tijara, Alwar, Rajasthan")
    st.write("Engineers Point Sr. Sec School,Khairthal, Alwar, Rajasthan")
    
with col2:
    st.write("Graducation Year 2024")
    st.write("CGPA - 8.23")
    st.write("2018")
    st.write("2020")
st.divider()
