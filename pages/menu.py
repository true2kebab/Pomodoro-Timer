import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "intro"

st.markdown('''<style>
        h1{text-align: center !important;
            font-size: 124px !important;
            font-weight: 1000 !important;}
        .stApp {
        background: linear-gradient(90deg, #FF007F, #00F0FF, #8A2BE2) !important;
                    }
           .stButton button{background-color: red !important;
                  transition:0.2s !important;
                  color:white !important;
                  padding:50px !important;
                  border-radius:50px !important;
                  text-align: center !important;
                  font-weight: 500 !important;
                  font-size: 5px !important;
                    }

                .stPageLink p{
                                    font-size: 38px !important;
                                    font-weight: bold;
                                    color: red !important;
                                    overflow: visible !important;
                                    white-space: nowrap !important;
                                    }
                .stPageLink [data-testid="stIconBlock"],
                            .stPageLink span,
                            .stPageLink div {
                                font-size: 32px !important; 
                                line-height: 1 !important;
                                overflow: visible !important;
                                white-space: nowrap !important;
                                }
           .stButton button:hover{background-color: green !important;}       
               </style>    ''', unsafe_allow_html=True)
st.title("The menu")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/pomodoro.py", label="Open Pomodoro Timer", icon="⏱️")
with col4:
    st.page_link("pages/history.py", label="View History", icon="⏳")

col1, col2, col3 = st.columns(3)
with col2:
    st.page_link("intropage.py", label="Back to Intro Page", icon="🏠")

