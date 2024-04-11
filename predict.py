import streamlit as st
import pickle

st.title('Placement Prediction System')
model = pickle.load(open('model1.pkl', 'rb'))

col1, col2 = st.columns(2)

a = col1.number_input('Enter age', value=18, min_value=18, max_value=100, step=1)
g = col2.radio('Select gender', ['Male', 'Female'])
s = col1.selectbox('Select stream', ['Electronics And Communication', 'Computer Science', 'Information Technology', 'Mechanical', 'Electrical', 'Civil'])  # Use selectbox for stream selection
i = col2.number_input('Enter number of internships', value=0, min_value=0, max_value=10, step=1)
c = col1.number_input('Enter CGPA', min_value=0.0, max_value=10.0, step=0.1)
h = col2.radio('Hostel or not', ['No', 'Yes']) 
b = col1.number_input('Enter number of backlogs', value=0, min_value=0, max_value=10, step=1)

if st.button('Predict'):

    gender_val = 1 if g == 'Male' else 0
    stream_mapping = {
        'Electronics And Communication': 1,
        'Computer Science': 2,
        'Information Technology': 3,
        'Mechanical': 4,
        'Electrical': 5,
        'Civil': 6
    }
    stream_val = stream_mapping[s]

    data = [[a, gender_val, stream_val, i, c, 1 if h == 'Yes' else 0, b]]  
    result = model.predict(data)[0]


    if result == 1:
        st.success("Congratulations! You are predicted to get placed. Work hard to secure a higher package.")
    else:
        st.error("Sorry, you are not predicted to get placed. Focus on improving your skills and gaining more experience.")
