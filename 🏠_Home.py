import streamlit as st
from streamlit.logger import get_logger
import streamlit.components.v1 as components
import datetime
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
background-image: url("https://storage.googleapis.com/micada-dev-public/test/image2.jpg");
background-size: 100%;
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

thedate = datetime.date.today()
def run():
    #st.image('https://www.neuraldesigner.com/images/power-plant-gas-emissions-image.webp', use_column_width=True)
    # st.set_page_config(page_title="Enter Page", page_icon="💻")
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.write("""
    # Welcome to NOx level Prediction of Combined Cycle Power Plant!
    """) 

    st.markdown(
        """
    This is an Example solved by using the Neural Network Techniques by Predicting the NOx levels in the gases emitted by the 
    Combined Cycle Power Plant.
    
    ### Goal
    The goal of this model is to predict the NOx levels accurately by which precautions will be taken in order to control the Pollution.
    

    """
    )
    #st.write("###### Date: ", thedate)
    #st.markdown('![Visitor count](https://shields-io-visitor-counter.herokuapp.com/badge?page=https://share.streamlit.io/your_deployed_app_link&label=VisitorsCount&labelColor=000000&logo=GitHub&logoColor=FFFFFF&color=1D70B8&style=for-the-badge)')
                                        
                                          
                            

if __name__ == "__main__":
    run()

