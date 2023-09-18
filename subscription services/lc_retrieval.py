# pip install -q langchain openai chromadb
# pip install tiktoken

from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = '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' # Replace with your API key, but remember to keep it secret.

# Load the documents
loader = CSVLoader(file_path='context2.csv')

# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

# Set up the retrieval chain. Use the chain_type "retrieval" to indicate retrieval behavior.
chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="retrieval", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

chat_history = []

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
