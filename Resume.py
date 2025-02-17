import streamlit as st

st.set_page_config("digital_resume",page_icon="📃",layout="centered")

# for adding name and image
col1,col2 = st.columns([3,1])
with col1:
    st.subheader("Name")
    st.title("Vipul Singh")
with col2:
    st.image("https://raw.githubusercontent.com/VipulSingh2/digital_resume/main/vipulimage.jpg")
st.divider()

# for adding personal details like mobile no ,githb,email
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
st.header(":orange[📚Education]")
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

# for adding technical skills 
st.header(":orange[⚒️Technical Skills]")
col1,col2 = st.columns([0.5,1])
with col1:
    st.write("• _Language_ :")
    st.write("• _Developer Tools_ :")
    st.write("• _Data Analysis Tools_ :")
    st.write("• _Data Visualization_ :")
    st.write("• _Other Tools_ :")
with col2:
    st.write("_Python,SQL,C_")
    st.write("_Visual Studio Code,Jupyter Notebook,Pycharm_")
    st.write("_Excel,Power BI,MySQL,Pandas_")
    st.write("_Pandas,Numpy,Matplotlib,Streamlit_")
    st.write("_Github_")
st.divider()
# for adding the internship details
st.header(":orange[📄INTERNSHIP]")
st.write("Accenture North America")
st.write("June 2024 - Agust 2024")
st.divider()

# for adding the certificate in the digital resume
st.header(":orange[🎑 CERTIFICATIONS]")
st.markdown('<a href="https://www.openai.com" target="_blank">Data Analysis Virtual Intenship -Forage</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.openai.com" target="_blank">Smart India Hackathon (SIH-2023)</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.openai.com" target="_blank">Deep Learning Training</a>', unsafe_allow_html=True)
st.markdown('<a href="https://www.openai.com" target="_blank">Python for Data Science</a>', unsafe_allow_html=True)
st.divider()

# for adding the personal projects
st.header(":orange[👩‍💻 PROJECTS]")
st.subheader(":blue[WhatsApp Chat Sentiment Analysis.]")
st.write("Python,Machine Learning")
st.write(""" • _Developed a Python application to analyze sentiment in WhatsApp chat data using machine learning tech
niques_.""")
st.write(""" • _Utilized libraries such as Pandas, Scikit-learn, and NLTK for data preprocessing, feature extraction, and
 sentiment classification_.""")

st.subheader(":blue[Analyzing E-commerce Sales Data]")
st.write("_Power BI_")
st.write(""" •_Conducted a comprehensive analysis of e-commerce sales data using Power BI to identify trends, patterns, and
 actionable insights_.""")
st.write("""• _Created interactive dashboards and reports to visualize key metrics such as sales performance, customer be
havior, and product popularity_.""")
st.divider()

# adding the positions of responsibility by me
st.header(":orange[😎 POSITIONS OF RESPONSIBILITY ]")
st.write("_SIH Mentor, (OPJU,CHATTISGARH)_")
st.divider()

# adding ther personal interests
st.header(":orange[🧩INTERESTS]")
st.write(" • _Programming Problems: Counting combinations or permutations and finding unique characters in strings_.")
