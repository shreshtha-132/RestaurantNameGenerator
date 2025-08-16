import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import SimpleSequentialChain, SequentialChain
import os
from dotenv import load_dotenv
load_dotenv()

st.title("Restaurant Name Generator")
st.sidebar.header("Cuisine Picker")

def get_restaurant_name_and_menu(cuisine):
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ["GEMINI_API_KEY"])
    name_prompt = PromptTemplate(input_variables=["cuisine"], template="Coin a restaurant name for {cuisine} cuisine.")
    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="Restaurant Name")
    menu_prompt = PromptTemplate(input_variables=["Restaurant Name"], template="Create a menu for {Restaurant Name}. Give it as comma-sepaPrated")
    menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key="Menu")
    chain = SequentialChain(chains=[name_chain, menu_chain], input_variables=["cuisine"], output_variables=["Restaurant Name", "Menu"])
    response = chain.invoke("Indian")
    return response

cuisine = st.sidebar.selectbox("Select a cuisine", ["Indian", "Italian", "Chinese", "Mexican", "Thai"])
if cuisine:
    response = get_restaurant_name_and_menu(cuisine)
    st.write("Restaurant Name:", response["Restaurant Name"])
    st.write("Menu:", response["Menu"])

