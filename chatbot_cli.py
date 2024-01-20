import sys
from chatbot_chain import get_chatbot_chain

chain = get_chatbot_chain()
while True:
    try:
        query = input('Prompt (or type "exit" to quit): ')

        if query == "exit":
            print('Exiting')
            sys.exit()

        response = chain({"question": query})

        print("Answer: " + response["answer"])
    except Exception as e:
        print(f"Error: {e}")