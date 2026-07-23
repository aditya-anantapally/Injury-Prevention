import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-2.5-flash")
st.markdown(
    """
    <style>
    /* Light blue background */
    .stApp, .reportview-container, body {
        background-color: #add8e6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Welcome to the  Injury Recovery/Prevention App ")
name= st.text_input("Enter athlete name: ") 
st.write( "Hi " + name, " Please fill in the details below. The more detail the better!")
st.markdown("Demographics and Biometrics")
col1, col2=st.columns(2)
with col1:
    Age=st.number_input("Enter athlete age: ", min_value=1, max_value=100, step=1)
    Weight=st.number_input("Enter athlete weight (in lbs): ", min_value=1, max_value=1000, step=1)
with col2:
    Gender=st.selectbox("Select athlete gender: ", ["Male", "Female", "Other"]) 
    Height=st.number_input("Enter athlete height (in inches): ", min_value=1, max_value=120, step=1)
st.write("---")
st.markdown("Sport Profile")
Sport_Category=st.radio("Choose category: ", ["Traditional team/Individual sport", "Martial arts/Combat sports"],
horizontal = True
)
Sport_Name=st.text_input("Enter athlete sport: ")
if Sport_Category == "Traditional team/Individual sport":
    User_Level=st.selectbox("Select user level: ", ["Recreational", "Club", "High School", "Collegiate", "Professional"])
    Position=st.text_input("Enter athlete position if applicable: ")
else:
    User_Level=st.text_input("Enter belt color/rank if applicable: ") 
Intensity_Level=st.selectbox("Select athlete intensity level: ", ["Low", "Moderate", "High", "Extreme"])
st.write("---")
st.markdown("Health and Training History")
Previous_Injuries=st.text_area("Enter athlete previous injuries and how long since the injury happened: ")
Recent_Injuries=st.text_area("Enter athlete current injuries: ")
Current_Training_Frequency=st.text_input("Enter athlete current training frequency and duration (e.g., 2 days/week on tuesdays and thursdays for 3 hours): ")
col3, col4=st.columns(2)
with col3:
    Games_Per_Week=st.number_input("Enter athlete games per week on average if applicable: ", min_value=0, max_value=14, step=1)
with col4:
    Average_Minutes_Played_Per_Game=st.number_input("Enter athlete average minutes played per game if applicable: ", min_value=0, max_value=240, step=1)
Dietary_Habits=st.text_area("Enter athlete dietary habits: ")
Other_Notes=st.text_area("Enter athlete other notes: ")

st.write("Is all this info correct? If so, please proceed to get your injury risk analysis and recommendations.")
if st.button("Get Injury Risk Analysis and Recommendations"):
    if Sport_Category == "Traditional team/Individual sport":
        final_rank_string= f"Competition Level: {User_Level} Position: {Position}"
    else: 
        final_rank_string= f"Belt Color/Rank: {User_Level}"
prompt=f"""You are an experienced sports scientist and injury prevention specialist.Dont add unnessecary text about yourself.
Analyze the following athlete profile and estimate their injury risk level based on the type of sport they play and their level is defined as '{final_rank_string}'.
Use evidence-based reasoning related to biomechanics, training load, sport-specific injury patterns, and history of previous injuries.
Then, explain why the athlete has that risk level and give 3–5 actionable recommendations to reduce injury risk as well as a recovery plan to help any current injuries heal by giving a schedule for each day of the week to maximize the healing process.Use mainly things that can be done by a average athlete (no crazy expensive equipment, dont change the current practices they have since coaches will not change their practice session. do mainly things outside of practice. and remeber lots of users are in school so they have a limited  time ). Also try to come up with good meal plans based on different budgets to help with any deficiencies.                  
Athlete Data:     
Name: {name}    
Age: {Age}    
Gender: {Gender}    
Weight: {Weight}   
Height: {Height}
Sport Category: {Sport_Category}
Intensity Level: {Intensity_Level}
Sport: {Sport_Name}  ({final_rank_string})
Intensity Level: {Intensity_Level}
Previous Injuries: {Previous_Injuries}
Recent Injuries: {Recent_Injuries}
Current Training Frequency: {Current_Training_Frequency}
Games Per Week: {Games_Per_Week}
Average Minutes Played Per Game: {Average_Minutes_Played_Per_Game}
Dietary Habits: {Dietary_Habits}
Other Notes: {Other_Notes}
Output Format:
Injury Risk Level: (give a risk estimate)
Risk Factors Identified: (list specific reasons)   
Recommendations to Reduce Injury Risk:
Recovery Plan: (Provide a day-by-day schedule for healing)
Meal Plan: (Include a 7-day meal-by-meal diet plan with breakfast, lunch, dinner, snacks, hydration, ingredients, step-by-step recipes, estimated macros, average US grocery prices per meal, and total daily food cost tailored to athlete.)
"""
st.write("### Injury Risk Analysis and Recommendations")
    with st.spinner("Processing your data..."):
        response=model.generate_content(prompt)   
    st.write(response.text)





