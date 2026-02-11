import streamlit as st
import requests
import uuid

st.set_page_config(page_title="ADK Assistant", page_icon="🤖")

st.title("🤖 Multi-Agent ADK Assistant")

# Session State for UUID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Session State for Messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask the agents something..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call API
    with st.chat_message("assistant"):
        with st.spinner("Agents are researching and analyzing..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={
                        "message": prompt,
                        "session_id": st.session_state.session_id
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("response", "No response received.")
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Connection Error: {str(e)}")
