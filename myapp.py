import streamlit as st
import requests

st.title("Chatbot with OnPrem Hosted LLM")

url = "http://127.0.0.1:11434/api/chat"
context = ""
if "messages" not in st.session_state:
    st.session_state.messages = []
    context = ""
    prompt = ""
        

#show the message as Bot
message = st.chat_message("ai")
message.write("welcome to Hello World from AI!")

# Show the message as Human

message_human = st.chat_message("human")
message_human.write("I'm Human!")

# Take the input prompt

prompt = st.chat_input("Please write something")
payload = {
    "model": "llama3.2:latest",
    "messages": [
        {
            "role": "user",
            "content": f"Previous History is following : {st.session_state.messages} and new prompt is following :{prompt}. Make sure you do not display json like structure as it is, in the answer."
        }
    ],
    "stream": False
}

if prompt != None:
    st.session_state.messages.append({"role":"human", "content":f"{prompt}"})
    for message in st.session_state.messages:
        if message["content"] != None:
            st.chat_message(message["role"]).markdown(message["content"]) 

if prompt != None:
    response = requests.post(url, json=payload)
    answer = response.json()["message"]["content"]
#    st.session_state.messages.append({"role":"human", "content":f"{prompt}"})
    st.session_state.messages.append({"role":"ai", "content":f"{answer}"})
    if answer != None:
        st.chat_message('ai').markdown(answer) 

# for message in st.session_state.messages:
#     if message["content"] != None and message["content"] != prompt :
#         st.chat_message(message["role"]).markdown(message["content"]) 
