import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# Load All Files

with open('model_logistic.pkl', 'rb') as file_model:
  model_logistic = pickle.load(file_model)

def run():
    st.title('Job Placement Prediction')
    # Membuat form
    with st.form(key='form_parameters'):
        gender =st.selectbox('Gender', ('Male','Female'), index=1, help='Gender of the candidate.')
        ssc_percentage =st.number_input('SSC Percentage', min_value=0, max_value=100, value=25, step =1, help= 'Senior secondary exams percentage (10th Grade).')
        ssc_board = st.selectbox('SSC Board', ('Other','Central'), index=1, help= 'Board of education for ssc exams.')
        hsc_percentage = st.number_input('HSC Percentage', min_value=0, max_value=100, value=25, step =1, help= 'Higher secondary exams percentage (12th Grade).')
        hsc_board = st.selectbox('HSC Board', ('Other','Central'), index=1, help= 'Board of education for hsc exams.')
        hsc_subject = st.selectbox('HSC Subject', ('Commerce','Science','Arts'), index=1, help= 'Subject of study for hsc.')
        degree_percentage = st.number_input('Degree Percentage', min_value=0, max_value=100, value=25, step =1, help= 'Percentage of marks in undergrad degree.')
        undergrad_degree = st.selectbox('Undergrad Degree', ('Sci&Tech','Comm&Mgmt','Others'), index=1, help= 'Undergrad degree majors.')
        work_experience = st.selectbox('Work Experience', ('Yes','No'), index=1, help= 'Past work experience.')
        emp_test_percentage = st.number_input('Test Percentage', min_value=0, max_value=100, value=25, step =1, help= 'Aptitude test percentage.')
        specialisation = st.selectbox('Specialisation', ('Mkt&HR','Mkt&Fin'), index=1, help= 'Postgrad degree majors - (MBA specialization).')
        mba_percent = st.number_input('MBA Percent',min_value=0, max_value=100, value=25, step =1, help= 'Percentage of marks in MBA degree.')

        

        submitted = st.form_submit_button('Predict')

    data_inf = {
    'gender': gender,
    'ssc_percentage': ssc_percentage, 
    'ssc_board': ssc_board, 
    'hsc_percentage': hsc_percentage, 
    'hsc_board': hsc_board, 
    'hsc_subject': hsc_subject, 
    'degree_percentage': degree_percentage,
    'undergrad_degree': undergrad_degree, 
    'work_experience': work_experience, 
    'emp_test_percentage': emp_test_percentage, 
    'specialisation': specialisation,
    'mba_percent': mba_percent
    }

    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:       
        y_pred_inf = model_logistic.predict(data_inf)
        y_pred_inf = str(y_pred_inf)
        st.write('## Status :', y_pred_inf.split("'")[1])

      
if __name__ == '__main__':
    run()