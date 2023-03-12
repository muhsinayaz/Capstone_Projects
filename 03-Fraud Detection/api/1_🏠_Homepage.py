# import module
import streamlit as st
import pandas as pd
import numpy as np
import pickle
# import imblearn

from PIL import Image
import json
import requests  
from streamlit_lottie import st_lottie 
# import base64


st.set_page_config(
    page_title="My Project App",
    page_icon="😎"
)
# Animation
@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Main Page
html_temp = """
            <div style ="background-color:#1D9C26; 
            border-style: hidden; border-radius: 25px; 
            padding:13px">
                <h1 style ="color:black; text-align:center; ">
                Streamlit Fraud Detection
                </h1>
            </div>
            """
st.markdown(html_temp, unsafe_allow_html = True)


# İmages of Entered

lottie_fraud = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_llckxtas.json")

st_lottie(lottie_fraud, key="fraud",
          height=480, width=720)

# Sidebar Info
determie_temp = """
            <div style = 
            padding:13px;">
                <h3 style ="color:orange; text-align:center; ">
                About the data we use.
                </h3>
            </div>
            """

st.markdown(determie_temp, unsafe_allow_html = True)
st.write("")
st.markdown(""":green[***The datasets contains transactions made by credit cards in September 2013 by european cardholders.***]\n
:green[***This dataset presents transactions that occurred in two days, where it has **492 frauds** out of **284,807** transactions.***] \n
:green[***The dataset is **highly unbalanced**, the positive class (frauds) account for 0.172% of all transactions.***]""")


# Display Dataset
@st.cache_data
def read_csv(path):
    return pd.read_csv('data/Sample-Data-10rows.csv')
df = read_csv("data/Sample-Data-10rows.csv")
st.write(df)












hide_st_style = """
            <style>
footer {
	visibility: hidden;
	}
header {
    visibility: hidden;
    }
# #MainMenu {
#     visibility: hidden;
#     }

footer:after {
	content:'Developed with ❤️ by Muhsin'; 
	visibility: visible;
	display: block;
	position: relative;
	# background-color: green;
	padding: 15px;
	top: 2px;
}
            </style>
    
            """
st.markdown(hide_st_style, unsafe_allow_html=True)




