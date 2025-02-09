import streamlit as st

Credits = [16, 18, 23, 24, 22, 0, 0, 0]
total_credits = sum(Credits)

st.title('CGPA Calculator')

num_courses = st.number_input('Number of Sems', min_value=1, step=1, value=5)

if st.checkbox('Add Custom Credits'):
    st.write('Credits for each semester added by default is what is followed in GEC Computer curriculum. You can add your own credits below:')
    st.subheader('Enter your Custom Credits below:')
    creds = []
    for i in range(num_courses):
        credit = st.number_input(f'Sem {i+1}', min_value=0, step=1, value=Credits[i])
        creds.append(credit)
    Credits = creds
    total_credits = sum(Credits)

st.subheader('Enter your SGPA below:')

grades = []
for i in range(num_courses):
    grade = st.number_input(f'Sem {i+1}', min_value=0.0, max_value=10.0, step=0.1)
    grades.append(grade)

total_grade = sum([a*b for a,b in zip(grades, Credits)])
cgpa = total_grade/total_credits

st.subheader(f'Your CGPA is: {cgpa:.2f}')

gdrive_link = "https://drive.google.com/file/d/1JyIgnGSZpeBphGtcoDdaj8eXnVvROFb8/view?usp=drivesdk"
st.markdown(f"[View CGPA Calculation Guide]({gdrive_link})")
