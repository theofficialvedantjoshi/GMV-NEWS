import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie;
from streamlit_lottie import st_lottie_spinner
st.set_page_config("GMV NEWS LIVE", "✈")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_url = "https://assets3.lottiefiles.com/private_files/lf30_tto68aem.json"
lottie_json = load_lottieurl(lottie_url)
st_lottie(lottie_json,height=200,width=200)

def janes():
    placeholder = st.empty()
    placeholder.empty()
st.header("GMV NEWS")

st.write("")
"This project features the GMV News application, which displays the latest news, with the heading and content, from different websites by just the click of the button. It helps the user to avoid the hassle of reading online news/ newspapers to update themselves with the daily news because our application makes this process more time friendly."
st.write("")

st.button("JANES",on_click=janes)
st.text("")


st.button("LOCKHEED MARTIN",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("GLOBAL DEFENSE ",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("DEFENSE NEWS",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("XYZ",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")

st.button("ABC",kwargs={'clicked_button_ix': 3, 'n_buttons': 4})
st.text("")