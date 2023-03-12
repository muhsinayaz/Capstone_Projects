# import module
import streamlit as st
import pandas as pd
import numpy as np
import pickle

import json
import requests  
from streamlit_lottie import st_lottie 



# Page-3

st.set_page_config(
    page_title="My Project App",
    page_icon="😎"
)

html_temp = """
            <div style ="background-color:#1D9C26; opacity: 0.5
            border-style: hidden; border-radius: 25px; 
            padding:13px">
                <h1 style ="color:black; text-align:center; ">
                Let's Examine the Predictions
                </h1>
            </div>
            """
st.markdown(html_temp, unsafe_allow_html = True)


# Animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_data
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Include Lottitater
lottie_pred = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_q2vehgcl.json")

st_lottie(lottie_pred,
          speed=0.6,
          quality="high",
          key="predict")


# user input
user_input_df = st.session_state["user_input"]
# try:

#     st.dataframe(user_input_df)
# except: st.write(user_input_df)

determie_temp = """
            <div style = 
            padding:13px;">
                <h3 style ="color:orange; text-align:center; ">
                Your Selected
                </h3>
            </div>
            """

st.markdown(determie_temp, unsafe_allow_html = True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write("V17 :  ", st.session_state["v17"])
with col2:
    st.write("V14 :  ", st.session_state["v14"])
with col3:
    st.write("V10 :  ", st.session_state["v10"])
with col4:
    st.write("V4 :  ", st.session_state["v4"])
with col5:
    st.write("V26 :  ", st.session_state["v26"])





log_model = pickle.load(open('models/model_Log.pkl', 'rb'))
xgb_model = pickle.load(open('models/model_XGB.pkl', 'rb'))


pred_log = log_model.predict(user_input_df)
pred_log = ['Fraud' if pred_log == 1 else 'Safe']
pred_xgb = xgb_model.predict(user_input_df)
pred_xgb = ['Fraud' if pred_xgb == 1 else 'Safe']



    
st.title('')

#  Model Seçimi
st.markdown("""<h3 style='text-align:left; color:#1D9C26;'>Choose Your Model</h3>
""", unsafe_allow_html=True)

model_selected = st.selectbox('Pick one model and get your prediction', ['Logistic Regression', 'XGBoosting'])


if model_selected == 'Logistic Regression':
    x1 = pred_log
else:
    x1 = pred_xgb


x2 = ['Warning! Suspected Fraud' if x1[0] == 1 else 'Secure Transaction']


if st.button('Predict'):
    if model_selected == 'XGBoosting':
        st.metric('XGBoosting Prediction', value=x2[0])

    else:
        st.metric('Logistic Regression Prediction', value=x2[0])


    if x1[0] == 1:
        st_lottie(load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_qbuxqwzg.json"))
        # st_lottie(lottie_hello, key="coding")

    else:
        st_lottie(load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_tw05dqnq.json"))









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






