import streamlit as st

st.markdown('''<style>
        h1 { text-align: center !important;
             font-size: 124px !important; font-weight: 1000 !important; }
        .stApp { background: linear-gradient(180deg, #FF007F, #00F0FF, #8A2BE2) !important; }
        h2 { color: blue !important; }
        
        .stPageLink p{
                                            font-size: 38px !important;
                                            font-weight: bold;
                                            color: red !important;}

        .stPageLink [data-testid="stIconBlock"],
                    .stPageLink span,
                    .stPageLink div {
                        font-size: 32px !important; 
                        line-height: 1 !important;
                        }
        </style>''', unsafe_allow_html=True)

st.title("The History and How to use the Pomodoro Technique")
st.header("Origin and Experimentation")
st.text('''Initial Struggle: As a college student facing mounting academic pressure, Cirillo found himself overwhelmed, unfocused, and prone to severe burnout.
The 2-Minute Test: He made a small pact with himself: challenge his focus for just two consecutive minutes using a mechanical, tomato-shaped kitchen timer—pomodoro being the Italian word for tomato.
Finding the Sweet Spot: After successfully maintaining focus for tiny intervals, he experimented with longer durations. He deduced that shorter intervals (like 10 minutes) were too brief to accomplish meaningful tasks, while hour-long blocks caused fatigue.''')
st.header("how to Use the Pomodoro Technique")
st.text('''1. Choose a Task: Select a task you want to work on.
2. Set a Timer: Set a timer for 25 minutes (one Pomodoro).
3. Work: Focus on the task until the timer rings.
4. Take a Break: Rest for 5 minutes after each Pomodoro.
5. Repeat: Continue the cycle, taking a longer break after four Pomodoros.''')

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/menu.py", label="Go to Menu Page", icon="📋")
