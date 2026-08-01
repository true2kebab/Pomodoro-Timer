import streamlit as st
import time  
from streamlit_autorefresh import st_autorefresh


st.set_page_config(page_title="Pomodoro Timer", page_icon="⏱️")

st.markdown('''<style>
    h1 {
        text-align: center !important;
        font-size: 124px !important;
        font-weight: 1000 !important;
    }
    .stApp {
        background: linear-gradient(90deg, #FF007F, #00F0FF, #8A2BE2) !important;
    }
    .stButton button {
        background-color: red !important;
        transition: 0.2s !important;
        color: white !important;
        padding: 20px 30px !important;
        border-radius: 50px !important;
        text-align: center !important;
        font-weight: 500 !important;
        font-size: 16px !important;
    }
    .stButton button:hover {
        background-color: green !important;
    }
</style>''', unsafe_allow_html=True)

if "timer_running" not in st.session_state:
    st.session_state.timer_running = False
if "remaining_seconds" not in st.session_state:
    st.session_state.remaining_seconds = 0
if "message" not in st.session_state:
    st.session_state.message = ""
if "end_time" not in st.session_state:
    st.session_state.end_time = 0

st.title("Pomodoro Timer")
st.write("Set your work and break lengths, then press Start.")

st.slider("Pomodoro session length (minutes)", 1, 60, 25, key="timer_slider")
st.slider("Break session length (minutes)", 1, 60, 5, key="break_slider")

col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start"):
        if not st.session_state.timer_running:
            st.session_state.timer_running = True
            st.session_state.end_time = time.time() + st.session_state.timer_slider * 60
            st.session_state.message = ""

with col2:
    if st.button("🔄 Reset"):
        st.session_state.timer_running = False
        st.session_state.remaining_seconds = 0
        st.session_state.end_time = 0
        st.session_state.message = "Timer reset."

if st.session_state.timer_running:
    remaining = int(st.session_state.end_time - time.time())

    if remaining > 0:
        st.session_state.remaining_seconds = remaining
        minutes, seconds = divmod(remaining, 60)
        st.subheader(f"⏳ Focus time: {minutes:02d}:{seconds:02d}")
        st_autorefresh(interval=1000, limit=0, key="timer_refresh")
    else:
        st.session_state.timer_running = False
        st.session_state.remaining_seconds = 0
        st.subheader("🎉 YAYYAYAYA BREAK TIME")
        st.balloons()
else:
    if st.session_state.remaining_seconds > 0:
        minutes, seconds = divmod(st.session_state.remaining_seconds, 60)
        st.subheader(f"⏹️ Stopped: {minutes:02d}:{seconds:02d}")
    else:
        st.subheader("Ready to start your Pomodoro session.")

if st.session_state.message:
    st.success(st.session_state.message)

if st.button("📋 Back to Menu"):
    st.switch_page("menu")
    st.stop()
