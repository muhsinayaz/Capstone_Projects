# import module

import streamlit as st
import pandas as pd
import numpy as np
import pickle

import base64
from PIL import Image
# import json
# import requests  
# from streamlit_lottie import st_lottie 


st.set_page_config(
    page_title="My Project App",
    page_icon="😎"
)
user_upload = None


st.title("")
determie_temp = """
            <div style = 
            padding:13px;">
                <h3 style ="color:orange; text-align:center; ">
                Upload the data to predict.
                </h3>
            </div>
            """

st.markdown(determie_temp, unsafe_allow_html = True)

# Upload File
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    user_upload = pd.read_csv(uploaded_file)
    st.dataframe(user_upload, use_container_width=True)

# models
log_model = pickle.load(open('models/model_Log.pkl', 'rb'))
xgb_model = pickle.load(open('models/model_XGB.pkl', 'rb'))


#  Model Seçimi
st.markdown("""<h2 style='text-align:center; color:#1D9C26;'>Choose Your Model</h2>
""", unsafe_allow_html=True)

model_selected = st.selectbox('Pick one model and get your prediction', ['Logistic Regression', 'XGBoosting'])

result = []
if user_upload is not None:

    if st.button('Predict'):

        if model_selected == 'Logistic Regression':
            result = log_model.predict(user_upload)
        if model_selected == 'XGBoosting':
            result = xgb_model.predict(user_upload)

        # Download Data    
        @st.cache_data 
        def convert_df(df, result):
            df = user_upload.copy()
            df["Class"] = result
            return df.to_csv().encode('utf-8')

        csv = convert_df(user_upload, result)

        st.write(":violet[If you want to download the results.]")
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='result_with_label.csv',
            mime='text/csv',
        )
st.title("")
determie_temp = """
            <div style = 
            padding:13px;">
                <h3 style ="color:orange; text-align:center; ">
                Result
                </h3>
            </div>
            """

st.markdown(determie_temp, unsafe_allow_html = True)
st.write(result)





# Footer
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


# # Background image

# def sidebar_bg(side_bg):

#    side_bg_ext = 'png'

#    st.markdown(
#       f"""
#       <style>
#       [data-testid="stSidebar"] > div:first-child {{
#           background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
#       }}
#       </style>
#       """,
#       unsafe_allow_html=True,
#       )
   
# def page_bg():
#     '''
#     A function to unpack an image from url and set as bg.
#     Returns
#     -------
#     The background.
#     '''
        
# st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url("https://media.istockphoto.com/id/183240639/photo/blue-\
#               colored-defocused-pattern.jpg?s=612x612&w=0&k=20&c=fdQnEgY2Qi79WLT3dKCd0fo9i808u2Lv8aOE-zTExRw=");
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# page_bg()
# sidebar_bg("images/business-tech.jpg")
