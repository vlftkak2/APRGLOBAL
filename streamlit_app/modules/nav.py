import streamlit as st
from streamlit_lottie import st_lottie
import requests

def sidebar():
    with st.sidebar:
        url = requests.get("https://lottie.host/9795a487-ba5c-4619-9151-68f77125a58c/amvixSOIik.json") 
        url_json = dict() 
        url_json = url.json() 
        st_lottie(url_json, 
        # change the direction of our animation 
        reverse=True, 
        # height and width of animation 
        height=200,   
        width=250, 
        # speed of animation 
        speed=1,   
        # means the animation will run forever like a gif, and not as a still image 
        loop=True,   
        # quality of elements used in the animation, other values are "low" and "medium" 
        quality='high', 
        # THis is just to uniquely identify the animation 
        key='Tree')

        st.header('메뉴')
        st.page_link('pages/globalPage.py', label='해외물류운영팀 모니터링', icon='🔥')
        
        
