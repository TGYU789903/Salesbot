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

def ask_and_get_response(chain, query, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            response = chain({"question": query})
            return response
        except RateLimitError:
            retries += 1
            if retries < max_retries:
                print(f"RateLimitError encountered. Retrying in 8.0 seconds. Attempt {retries}/{max_retries}")
                time.sleep(8.0)  # Wait for 8 seconds before retrying
            else:
                print(f"Max retries reached. Exiting after {max_retries} attempts.")
                raise  # Re-raise the exception after max retries
  

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

    response = ask_and_get_response(chain, query)

    # Save the chat record to Excel
    save_chat_to_excel(query, response['result'])

    print(response['result'])
