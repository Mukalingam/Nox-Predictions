import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import Model, load_model
import base64

st.set_page_config(
    page_title="Nox Predictions",
    page_icon="🌍",
)

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("tmp3.jpeg")    

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://storage.googleapis.com/micada-dev-public/test/image1.jpg");
background-size: 160%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

def load():
  model=load_model("nox_predictictions.h5")
  return model
with st.spinner('Model is being loaded..'):
  model=load()

st.title("NOx level Prediction of Combined Cycle Power Plant ")

amd_temp = st.number_input('Ambient Temperature, in degrees Celsius')
st.write('The given Ambient Temperature is ', amd_temp)

amd_pre = st.number_input('Ambient Pressure, in millibars')
st.write('The given Ambient Pressure is ', amd_pre)

amd_hum = st.number_input('Ambient Humidity, as a percentage')
st.write('The given Ambient Humidity is ', amd_hum)

dif_pre = st.number_input('Air Filter Difference Pressure, difference of pressure in the air filter, in millibars')
st.write('The given Air Filter Difference Pressure is ', dif_pre)

ex_pre = st.number_input('Gas Turbine Exhaust Pressure, pressure of the combustion chamber exhaust gases, in in millibar')
st.write('The given Gas Turbine Exhaust Pressure is ', ex_pre)

tb_tem = st.number_input('Turbine Inlet Temperature, temperature of the combustion chamber exhaust gases as they enter the turbine unit, in degrees Celsius')
st.write('The given Turbine Inlet Temperature is ', tb_tem)

tb_tem_af = st.number_input('Turbine After Temperature, temperature of the combustion chamber exhaust gases as they exit the turbine unit, in degrees Celsius')
st.write('The given Turbine After Temperature is ', tb_tem_af)

com_dic = st.number_input('Compressor Discharge Pressure, pressure of the gases expelled by the compressor, in millibars')
st.write('The given Compressor Discharge Pressure is ', com_dic)

tb_en = st.number_input('Turbine Energy Yield, total energy yielded by the turbine in an hour, in Megawatts per hour')
st.write('The given Turbine Energy Yield is ', tb_en)

co_em = st.number_input('The CO emission value in percent')
st.write('The given CO emission is ', co_em)

X_Testing = np.array([[amd_temp, amd_pre, amd_hum, dif_pre, ex_pre, tb_tem, tb_tem_af, com_dic, tb_en, co_em]])
#X_Testing = np.array([[17, 1013, 77, 3, 25, 1081, 546, 133, 12,22.1]])
if st.button('Predict'):
  value = 0
  predictions = model.predict(X_Testing)
  value = predictions[:,0]
  pre = value.item()
  res = round(pre, 2)
  st.write('The Predicted Nox value in milligrams per cubic meter is',res)

