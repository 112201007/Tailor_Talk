import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("Titanic Dataset Chatbot")

# Input for user question
question = st.text_input("Ask a question about the Titanic dataset:")

if question:
    if "histogram of passenger ages" in question.lower():

        df = pd.read_csv('titanic.csv')

        plt.hist(df['Age'].dropna(), bins=20, edgecolor='black')

        plt.title('Histogram of Passenger Ages')

        plt.xlabel('Age')

        plt.ylabel('Frequency')

        st.pyplot(plt)
    else:
        try:
            response = requests.get(f"http://localhost:8000/ask?question={question}")
            if response.status_code == 200:
                response_data = response.json()
                # Extract and display the specific value based on the question
                if "percentage_male" in response_data:
                    st.write(f"Percentage of male passengers: {response_data['percentage_male']:.2f}%")
                elif "average_fare" in response_data:
                    st.write(f"Average ticket fare: ${response_data['average_fare']:.2f}")
                elif "embarked_counts" in response_data:
                    st.write("Passengers embarked from each port:")
                    for port, count in response_data['embarked_counts'].items():
                        st.write(f"{port}: {count}")
                else:
                    st.write("Unexpected response format:", response_data)
            else:
                st.write(f"Error: Received status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.write(f"Error: Unable to connect to the server. {e}")

  
# Button to show histogram of passenger ages
if st.button("Show histogram of passenger ages"):
    df = pd.read_csv('titanic.csv')
    plt.hist(df['Age'].dropna(), bins=20, edgecolor='black')
    plt.title('Histogram of Passenger Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    st.pyplot(plt)