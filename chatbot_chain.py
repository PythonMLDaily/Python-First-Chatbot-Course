import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def get_chatbot_chain():
    os.environ["OPENAI_API_KEY"] = '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'

    loader = CSVLoader(file_path="faq.csv")
    documents = loader.load()

    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())

    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(),
                                                  retriever=vectorstore.as_retriever(),
                                                  memory=memory)
    return chain
