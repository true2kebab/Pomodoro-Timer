import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "intro"

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
                .stPageLink p{
                    font-size: 38px !important;
                    font-weight: bold;
                    color: red !important;
                                }
    .stPageLink [data-testid="stIconBlock"],
    .stPageLink span,
    .stPageLink div {
        font-size: 32px !important; 
        line-height: 1 !important;
    }
               </style>    """, unsafe_allow_html=True)
st.subheader(" ")
st.title("The start of your productivity session")
st.header("  ")
st.header("  ")
left, center, right = st.columns([1, 2, 1])
with center:
    st.page_link("pages/menu.py", label="Go to Menu Page", icon="📋")