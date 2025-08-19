import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import SimpleSequentialChain, SequentialChain
import os
from dotenv import load_dotenv
import langchain_helper as helper
load_dotenv()

st.title("Restaurant Name Generator")
st.sidebar.header("Cuisine Picker")



cuisine = st.sidebar.selectbox("Select a cuisine", ["Indian", "Italian", "Chinese", "Mexican", "Thai"])
if cuisine:
    response = helper.get_restaurant_name_and_menu(cuisine)
    st.write("Restaurant Name:", response["Restaurant_Name"])
    st.write("Menu:", response["Menu"])

