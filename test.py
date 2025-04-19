import streamlit as st
st.header("Wrist Watch Detection")
st.subheader("by Fahad Nasir Mughal")
st.markdown("Fahad")
st.title("Personal Information Form")


st.code("""
name = 'Fahad'
age = 22
""", language='python') 


name = st.text_input("Enter your name")
father_name = st.text_input("Enter your father's name")
age = st.number_input("Enter your age")
salary = st.number_input("Enter your salary",  format="%.2f")

if st.button('Submit'):
    st.write(f"Name: {name}, Father's Name: {father_name}, Age: {age}, Salary: ${salary}")




st.file_uploader("choose the image:",type=['jpeg','jpg','svg'])

st.image(img, caption="Uploaded Image", use_column_width=True)




st.radio('gender',"age")
st.code("""import streamlit as st
st.header("Wrist Watch Detection")
st.subheader("by Fahad Nasir Mughal")
st.markdown("Fahad")
st.title("Personal Information Form")

name = st.text_input("Enter your name")
father_name = st.text_input("Enter your father's name")
age = st.number_input("Enter your age")
salary = st.number_input("Enter your salary",  format="%.2f")

if st.button('Submit'):
    st.write(f"Name: {name}, Father's Name: {father_name}, Age: {age}, Salary: ${salary}")
""",language='python')

import pandas as pd
data = {
    'Name': ['fahad', 'ali', 'ahmed', 'khizar'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df=pd.DataFrame(data)
st.write(df)
st.dataframe(df)
st.table(df)
st.line_chart(df)

data=pd.read_csv(r"c:\Users\C1-PC17\Downloads\assign3_train.csv")

st.line_chart(data[['x1', 'x2']])