import streamlit as st
from chatbot_chain import get_chatbot_chain

chain = get_chatbot_chain()

bot_logo = 'https://pbs.twimg.com/profile_images/1739538983112048640/4NzIg1h6_400x400.jpg'

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "bot",
                                     "content": "Hello, how can I help?"}]

for message in st.session_state.messages:
    if message["role"] == 'bot':
        with st.chat_message(message["role"], avatar=bot_logo):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if query := st.chat_input("Please ask your question here:"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant", avatar=bot_logo):
        message_placeholder = st.empty()
        result = chain({"question": query})
        message_placeholder.markdown(result['answer'])

    st.session_state.messages.append({"role": "bot", "content": result['answer']})