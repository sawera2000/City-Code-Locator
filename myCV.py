import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Sawera's CV")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("me.png",width=230)
with col2:
    st.title("Sawera Arshad")
    st.write("Undergraduate Informatio Technology  ")
    st.info("I am Currently Enrolled in BS information Technology and seeking Skills AI , Machine Learning and Robotics from PMU-BBSHRRDB-MUET,Jamshoro")
    st.write("📫", "saweraarshad108@gmail.com")

# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualification")
df=pd.DataFrame({
        "year":      ['2k20 to current','2k19-2k21','2k17-2k18','2k16'],
        "Degree":   ['BS-IT','BA','Intermidiates','Matriculation'],
        "field":    ['Information Technology','Bachelor in Arts','Engineering','Science'],
        "Institution":  ['University Of Sindh(UOS)','GGDC','Worker Intermediate Girls College','City Grammer High School Kotri'],
        "Grads":    ['3.6 CGP', '1st Division(A)',' A Grade' ,'A1'],
        })
st.write(df)


# --- EXPERIENCE ---
st.write('\n')
st.subheader("Experience")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and MS.Office 
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Numpy,Pandas), C/C++, Matlab 
- 📊 Data Visulization: MS Excel, Python

"""
)

# --- Contact Details ---
st.write('\n')
st.subheader("Contact Details")
st.write(
    """
- 📞 0000-0000000
- 📧 saweraarshad108@gmail.com
- 📍  Hyderabd, Pakistan
"""
)

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- Introduction to Machine Learning - Simplilearn
- Graphic Designing - NFTP
- Canva Basics to Advanced Training - LWS Academy
"""
)
#---languages---
st.subheader("Languages")   
st.slider("English  ", 0,100,70)
st.slider("Sindhi  ", 0,100,50)
st.slider("Urdu ", 0,100,80)

# --- Honor And Awards ---
st.write('\n')
st.subheader("Honor And Awards")
st.write(
    """
- Ehsaas Scholarship of Undergraduate Program (2020-2024)
"""
)