import os
import configparser
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def get_chatbot_chain():
     # Load OpenAI API key from a configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')
    os.environ["OPENAI_API_KEY"] = config.get('Credentials', 'OPENAI_API_KEY')

    loader = CSVLoader(file_path="faq.csv")
        
    try:
        documents = loader.load()
    except Exception as e:
        print(f"Error loading documents: {e}")

    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(),
                                                  retriever=vectorstore.as_retriever(),
                                                  memory=memory)
    return chain


