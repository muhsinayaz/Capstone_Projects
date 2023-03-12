# import module

import streamlit as st
import pandas as pd
import numpy as np
import pickle

from PIL import Image
import json
import requests  
from streamlit_lottie import st_lottie 


st.set_page_config(
    page_title="My Project App",
    page_icon="😎"
)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
# Page-2
html_temp = """
            <div style ="background-color:#1D9C26; 
            border-style: hidden; border-radius: 25px; 
            padding:13px">
                <h1 style ="color:black; text-align:center; ">
                Enter values to predict.
                </h1>
            </div>
            """
st.markdown(html_temp, unsafe_allow_html = True)

lottie_coding = load_lottiefile("images/programming-computer.json")

# Include Lottitater
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    # renderer= "canvas", #"svg",
    height=None,
    width=None,
    key=None,
)


if "user_input" not in st.session_state:
    st.session_state["user_input"] = "Giriş Yapılmadı"
if "v17" not in st.session_state:
    st.session_state["v17"] = 0.00
if "v14" not in st.session_state:
    st.session_state["v14"] = 0.00
if "v10" not in st.session_state:
    st.session_state["v10"] = 0.00
if "v4" not in st.session_state:
    st.session_state["v4"] = 0.00
if "v26" not in st.session_state:
    st.session_state["v26"] = 0.00
if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None



def converts():
    st.session_state.v17s = st.session_state.v17n
    st.session_state.v14s = st.session_state.v14n
    st.session_state.v10s = st.session_state.v10n
    st.session_state.v4s = st.session_state.v4n
    st.session_state.v26s = st.session_state.v26n
def convertn():
    st.session_state.v17n = st.session_state.v17s
    st.session_state.v14n = st.session_state.v14s
    st.session_state.v10n = st.session_state.v10s
    st.session_state.v4n = st.session_state.v4s
    st.session_state.v26n = st.session_state.v26s


col1, buff,col2 = st.columns([2,1,2])
st.title("Enter Values")
with col1:
    v17 = st.slider(label="V17-PCA", min_value=-26.00, max_value=10.00, step=0.01,
                    value=st.session_state["v17"], key="v17s", on_change=convertn)
    v14 = st.slider(label="V14-PCA", min_value=-20.00, max_value=11.00, step=0.01,
                    value=st.session_state["v14"], key="v14s", on_change=convertn)
    v10 = st.slider(label="V10-PCA", min_value=-25.00, max_value=24.00, step=0.01,
                    value=st.session_state["v10"], key="v10s", on_change=convertn)
    v4 = st.slider(label="V4-PCA", min_value=-6.00, max_value=17.00, step=0.01,
                   value=st.session_state["v4"], key="v4s", on_change=convertn)
    v26 = st.slider(label="V26-PCA", min_value=-3.00, max_value=4.00, step=0.01,
                    value=st.session_state["v26"], key="v26s", on_change=convertn)
with col2:
    st.title("")
    v17 = st.number_input(label="V17-PCA", min_value=-26.00, max_value=10.00, step=0.01,
                          value=st.session_state["v17"], key="v17n", on_change=converts)
    v14 = st.number_input(label="V14-PCA", min_value=-20.00, max_value=11.00, step=0.01,
                          value=st.session_state["v14"], key="v14n", on_change=converts)
    v10 = st.number_input(label="V10-PCA", min_value=-25.00, max_value=24.00, step=0.01,
                          value=st.session_state["v10"], key="v10n", on_change=converts)
    v4 = st.number_input(label="V4-PCA", min_value=-6.00, max_value=17.00, step=0.01,
                         value=st.session_state["v4"], key="v4n", on_change=converts)
    v26 = st.number_input(label="V26-PCA", min_value=-3.00, max_value=4.00, step=0.01,
                          value=st.session_state["v26"], key="v26n", on_change=converts)


    
new_dict= {'V17': v17, 'V14': v14, 'V10': v10, 'V4': v4,'V26': v26}

features = pd.DataFrame(new_dict, index=[0])

submit = st.button("Submit")

if submit:

    st.session_state["user_input"] = features
    st.session_state.v17 = v17
    st.session_state.v14 = v14 
    st.session_state.v10 = v10
    st.session_state.v4 = v4    
    st.session_state.v26 = v26 
    html_temp = """
            <div style ="background-color:green; padding:10px">
                <h3 style ="color:white; text-align:center; ">
                Kaydedilen değerler.
                </h3>
            </div>
            """
    st.markdown(html_temp, unsafe_allow_html = True)

    st.dataframe(features.T, use_container_width=True)
    
else:
    st.write(st.session_state["user_input"])











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
