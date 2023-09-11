# pip install -q langchain openai chromadb
# pip install tiktoken

from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
import joblib

os.environ["OPENAI_API_KEY"] = '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'
# Load the documents
loader = CSVLoader(file_path='context.csv')

# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

chat_history = []

# Start with the bot's opening line
opening_line = "Hello, I'm Jacob from AryanTech Company. I'm calling you regarding our service to assist you in securing a job. Are you looking for any job opportunities right now?"
chat_history.append(opening_line)
print(opening_line)

while True:
    # Ask user for a query
    query = input("Please enter your query (or type 'exit' to end): ")

    # Exit loop if user types 'exit'
    if query.lower() == 'exit':
        break
    
    # If you want to provide the entire chat history as context
    context = ". ".join(chat_history)
    full_query = context + ". " + query if context else query

    response = chain({"question": full_query})

    # Save user's query and model's response to chat_history
    chat_history.append(query)
    chat_history.append(response['result'])

    print(response['result'])

# If you wish to save the chat history to a file
with open('chat_history.txt', 'w') as f:
    for chat in chat_history:
        f.write("%s\n" % chat)
# ________________________________________________
# chat_history = []

# while True:
#     # Ask user for a query
#     query = input("Please enter your query (or type 'exit' to end): ")

#     # Exit loop if user types 'exit'
#     if query.lower() == 'exit':
#         break
    
#     # If you want to provide the entire chat history as context
#     context = ". ".join(chat_history)
#     full_query = context + ". " + query if context else query

#     response = chain({"question": full_query})

#     # Save user's query and model's response to chat_history
#     chat_history.append(query)
#     chat_history.append(response['result'])

#     print(response['result'])

# # If you wish to save the chat history to a file
# with open('chat_history.txt', 'w') as f:
#     for chat in chat_history:
#         f.write("%s\n" % chat)

# _______________________________________________________________________________
# #query = "what is your name"
# query = "what payment options are available?"
# response = chain({"question": query})
# print(response['result'])


# #query = "What is the name of your company?"
# query = "How do I submit my cv?"
# response = chain({"question": query})
# print(response['result'])

# #query = "what services do you offer?"
# query = "When can I get started with your services?"
# response = chain({"question": query})
# print(response['result'])

# #query = "how does cv analysis work?"
# query = "What makes your service different than others?"
# response = chain({"question": query})
# print(response['result'])


