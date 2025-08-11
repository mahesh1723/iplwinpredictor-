#importing the necessary libraries
import streamlit as st
import pickle as pkl
import pandas as pd

#having a wide page layout
st.set_page_config(layout = "wide")

#title of the page
st.title("IPL Win Predictor")


#import data an model from the pickle
teams = pkl.load(open('team1.pkl','rb'))
cities = pkl.load(open('city1.pkl','rb'))
model = pkl.load(open('model.pkl','rb'))


#first row and columns
col1, col2, col3 = st.columns(3)
with col1:
    batting_team = st.selectbox('Select the Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the Bowling Team', sorted(teams))
with col1:
    selected_city = st.selectbox('Select the host city', sorted(cities))

target = st.number_input('Target Score', min_value=0, max_value=720, step=1)

col4, col5, col6 = st.columns(3)
with col4:
    score = st.number_input('Score', min_value =0 ,max_value=720, step=1)
with col5:
    overs = st.number_input('Overs Completed', min_value=0, max_value=20, step =1)
with col6:
    wickets= st.number_input('Wicket Fell', min_value=0, max_value=10, step=1)

if st.button('Predict Probabilities'):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[selected_cit y], 
        'Score':[score],
        'wickets':[wickets],
       'Remaining_Balls':[balls_left],
        'target_left':[runs_left],
        'crr':[crr],
        'rrr':[rrr],
    })
    result = model.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + " - " + str(round(win * 100)) + "%")

    st.header(bowling_team + " - " + str(round(loss * 100)) + "%")





