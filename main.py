import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="MSDS_NBA_GROUP_34",
    page_icon="🏀",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)


nba = requests.get(
    "https://lottie.host/03ecab61-f3ac-4ee0-b841-bf5de65dcb7a/2ZBvzRuFKx.json"
)
url_json = dict()

if nba.status_code == 200:
    url_json = nba.json()
else:
    print("Error in the URL")

st_lottie(url_json)


st.image("intro.png")
