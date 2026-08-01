import streamlit as st

st.set_page_config(page_icon="⏱️", page_title="PomApp")
st.markdown("""
                <style>
                h1{
            color: black !important;
            font-size: 124px !important;
            text-align: center !important;
            font-weight: 1000 !important;
                    }
            .stApp {
        background: linear-gradient(45deg, #FF007F, #00F0FF, #8A2BE2) !important;
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
               </style>    """, unsafe_allow_html=True)
st.subheader(" ")
st.title("The start of your productivity session")
st.header("  ")
st.header("  ")
left, center, right = st.columns([1, 2, 1])
