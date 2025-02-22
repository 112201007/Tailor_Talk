# from langchain import LangChain
from langchain.text_splitter import TextSplitter  # Example based on available modules
# Initialize LangChain
# langchain = LangChain()



from fastapi import FastAPI
import pandas as pd
# from langchain import LangChain

app = FastAPI()

# Load the dataset
df = pd.read_csv('titanic.csv')

# Initialize LangChain
# langchain = LangChain()

def parse_question(question):
    # Use LangChain to parse the question
    # This is a conceptual example; you'll need to implement the actual logic
    # Example: Use LangChain's NLP capabilities to determine intent
    # result = TextSplitter.parse(question)
    result=question
    # Example: Map LangChain's output to intents
    if "percentage" in result:
        return {"intent": "percentage_male"}
    elif "average fare" in result:
        return {"intent": "average_fare"}
    elif "embarked" in result:
        return {"intent": "embarked_counts"}
    else:
        return {"intent": "unknown"}
    
@app.get("/percentage_male")
def percentage_male():
    male_count = df[df['Sex'] == 'male'].shape[0]
    total_count = df.shape[0]
    percentage = (male_count / total_count) * 100
    return {"percentage_male": percentage}

@app.get("/average_fare")
def average_fare():
    average_fare = df['Fare'].mean()
    return {"average_fare": average_fare}

@app.get("/embarked_counts")
def embarked_counts():
    embarked_counts = df['Embarked'].value_counts().to_dict()
    return {"embarked_counts": embarked_counts}

@app.get("/ask")
def ask(question: str):
    parsed_question = parse_question(question)
    intent = parsed_question['intent']
    
    if intent == "percentage_male":
        return percentage_male()
    elif intent == "average_fare":
        return average_fare()
    elif intent == "embarked_counts":
        return embarked_counts()
    else:
        return {"response": "I'm sorry, I can't answer that question yet."}




# from fastapi import FastAPI
# import pandas as pd
# import pandas as pd
# import matplotlib.pyplot as plt
# import streamlit as st
# app = FastAPI()

# # Load the dataset
# df = pd.read_csv('titanic.csv')

# @app.get("/percentage_male")
# def percentage_male():
#     male_count = df[df['Sex'] == 'male'].shape[0]
#     total_count = df.shape[0]
#     percentage = (male_count / total_count) * 100
#     return {"percentage_male": percentage}

# @app.get("/average_fare")
# def average_fare():
#     average_fare = df['Fare'].mean()
#     return {"average_fare": average_fare}

# @app.get("/embarked_counts")
# def embarked_counts():
#     embarked_counts = df['Embarked'].value_counts().to_dict()
#     return {"embarked_counts": embarked_counts}

# # @app.get("/draw_histogram")
# # def draw_histogram():
# #     # embarked_counts = df['Embarked'].value_counts().to_dict()
# #     # return {"embarked_counts": embarked_counts}
# #     df = pd.read_csv('titanic.csv')
# #     plt.hist(df['Age'].dropna(), bins=20, edgecolor='black')
# #     plt.title('Histogram of Passenger Ages')
# #     plt.xlabel('Age')
# #     plt.ylabel('Frequency')
# #     st.pyplot(plt)
# @app.get("/ask")
# def ask(question: str):
#     # Placeholder for question parsing logic
#     # This should be replaced with actual NLP parsing
#     if "percentage of passengers were male" in question:
#         return percentage_male()
#     elif "average ticket fare" in question:
#         return average_fare()
#     elif "passengers embarked from each port" in question:
#         return embarked_counts()
#     elif "histogram of passenger ages" in question:
#         return draw_histogram()
#     else:
#         return {"response": "I'm sorry, I can't answer that question yet."}