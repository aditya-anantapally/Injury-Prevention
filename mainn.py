import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyCyAgxDUoNbr2Ww8tCdfs5esYs8eeeHSDE")
model=genai.GenerativeModel("gemini-2.5-flash")
# Inject light-blue background for the Streamlit app
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
Age=st.number_input("Enter athlete age: ", min_value=1, max_value=100, step=1)
Gender=st.selectbox("Select athlete gender: ", ["Male", "Female", "Other"])
Weight=st.number_input("Enter athlete weight (in lbs): ", min_value=1,      max_value=1000, step=1) 
Height=st.number_input("Enter athlete height (in inches): ", min_value=1, max_value=120, step=1)
Sport=st.text_input("Enter athlete sport: ")
Position=st.text_input("Enter athlete position: ")  
Experience_Level=st.selectbox("Select athlete experience level: ", ["Beginner", "Intermediate", "Advanced", "Professional"])
Training_Intensity_Level=st.selectbox("Select athlete training intensity level: ", ["Low", "Moderate", "High", "Extreme"])
Previous_Injuries=st.text_area("Enter athlete previous injuries and how long since the injury happened: ")
Recent_Injuries=st.text_area("Enter athlete current injuries: ")
Current_Training_Frequency=st.text_input("Enter athlete current training frequency (e.g., 2 days/week on tuesdays and thursdays): ")
Games_Per_Week=st.number_input("Enter athlete games per week on average: ", min_value=0, max_value=14, step=1)
Average_Minutes_Played_Per_Game=st.number_input("Enter athlete average minutes played per game: ", min_value=0, max_value=240, step=1)
Dietary_Habits=st.text_area("Enter athlete dietary habits: ")
Other_Notes=st.text_area("Enter athlete other notes: ")
prompt=f"""You are an experienced sports scientist and injury prevention specialist.Dont add unnessecary text about yourself.
Analyze the following athlete profile and estimate their injury risk level .
Use evidence-based reasoning related to biomechanics, training load, sport-specific in jury patterns, and history of previous injuries.
Then, explain why the athlete has that risk level and give 3–5 actionable recommendations to reduce injury risk as well as a recovery plan to help any current injuries heal by giving a schedule for each day of the week to maximize the healing process.Use mainly things that can be done by a average youth soccer player(no crazy expensive equipment, dont change the current practices they have since coaches will not change their practice session. do mainly things outside of practice. and remeber lots of users are in school so they have a limited  time )                  
Athlete Data:     
Name: {name}    
Age: {Age}    
Gender: {Gender}    
Weight: {Weight}   
Height: {Height}    
Sport: {Sport}   
Position: {Position}
Experience Level: {Experience_Level}
Training Intensity Level: {Training_Intensity_Level}
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
"""

st.write("Is all this info correct? If so, please proceed to get your injury risk analysis and recommendations.")
if st.button("Get Injury Risk Analysis and Recommendations"):
    st.write("### Injury Risk Analysis and Recommendations")
    with st.spinner("Processing your data..."):
        response=model.generate_content(prompt)   
    st.write(response.text)






# Nutrition prompt enhancement:
# Ask AI to include a 7-day meal-by-meal diet plan with breakfast, lunch, dinner,
# snacks, hydration, ingredients, step-by-step recipes, estimated macros,
# average US grocery prices per meal, and total daily food cost tailored to athlete.
