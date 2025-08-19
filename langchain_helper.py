
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import SimpleSequentialChain, SequentialChain
import os
from dotenv import load_dotenv
load_dotenv()

def get_restaurant_name_and_menu(cuisine):
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ["GEMINI_API_KEY"])
    name_prompt = PromptTemplate(input_variables=["cuisine"], template="Coin a restaurant name for {cuisine} cuisine.")
    name_chain = LLMChain(llm=llm, prompt=name_prompt, output_key="Restaurant_Name")
    menu_prompt = PromptTemplate(input_variables=["Restaurant_Name"], template="Create a menu for {Restaurant_Name}. Give it as comma-separated")
    menu_chain = LLMChain(llm=llm, prompt=menu_prompt, output_key="Menu")
    chain = SequentialChain(chains=[name_chain, menu_chain], input_variables=["cuisine"], output_variables=["Restaurant_Name", "Menu"],return_all=True)
    response = chain.invoke({"cuisine": cuisine})
    return response