from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
import pandas as pd

def save_chat_to_excel(query, response):
    file_name = "chat_history.xlsx"
    
    # Check if file already exists. If not, create a new one with headers.
    if not os.path.exists(file_name):
        df = pd.DataFrame(columns=["query", "response"])
        df.to_excel(file_name, index=False, engine='openpyxl')
    
    # Read the existing file
    df = pd.read_excel(file_name, engine='openpyxl')
    
    # Append new chat record
    new_record = {"query": query, "response": response}
    df = df.append(new_record, ignore_index=True)
    
    # Save the updated dataframe
    df.to_excel(file_name, index=False, engine='openpyxl')

os.environ["OPENAI_API_KEY"] = XYZ  # Replace with environment variable or other secret management tool
loader = CSVLoader(file_path='builderdatacsv.csv')
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])
chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

# Repeatedly ask questions until "exit" is entered
while True:
    query = input("Ask a question (or type 'exit' to end): ")
    if query.lower().strip() == "exit":
        break

    response = chain({"question": query})

    # Save the chat record to Excel
    save_chat_to_excel(query, response['result'])

    print(response['result'])
