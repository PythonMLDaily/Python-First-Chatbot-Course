from chatbot_chain import get_chatbot_chain
import sys

chain = get_chatbot_chain()

while True:
    query = input('Prompt (or type "exit" to quit): ')

    if query == "exit":
        print('Exiting')
        sys.exit()

    response = chain({"question": query})

    print("Answer: " + response["answer"])

