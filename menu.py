import streamlit as st


st.markdown{'''<style>
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
           .stButton button:hover{background-color: green !important;}       
               </style>    """, unsafe_allow_html=True'''}
st.title("The menu")
st.button("History of pomodoro")
st.button("Pomodoro")
st.button("Tutorial on how to use it")
