from dotenv import load_dotenv
load_dotenv() #loads environment variables from a .env file into the environment, making them accessible in the application.
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure our api key
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

#function to load google gemini model and procide sql queires
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt,question])
    return response.text

#function to retrieve data from the database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    conn.close()
    for row in data:
        print(row)
    return  data
prompt = """
You are an expert in converting English questions to sql query!
The SQL database has the name my_database.db and it has a table named students 
with the following columns: Name, class, section, marks.

For example:
Example - How many entries of records are present?
SQL command - SELECT COUNT(*) FROM students;

Question - What is the average marks of students in class 10th section A?
SQL command - SELECT AVG(marks) FROM students WHERE class='10th' AND section='A';

Also the sql code should not have ''' in beginning or end and sql word in output.
"""

st.set_page_config(page_title="Text to SQL", page_icon=":guardsman:", layout="wide")    
st.header("Gemini App To Retrieve Data From SQL Database")
question = st.text_input("Enter your question here: ",key = "input")                         
submit = st.button("Submit")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,'my_database.db')
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)