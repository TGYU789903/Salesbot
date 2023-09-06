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

#query = "what is your name"
query = "what payment options are available?"
response = chain({"question": query})
print(response['result'])


#query = "What is the name of your company?"
query = "How do I submit my cv?"
response = chain({"question": query})
print(response['result'])

#query = "what services do you offer?"
query = "When can I get started with your services?"
response = chain({"question": query})
print(response['result'])

#query = "how does cv analysis work?"
query = "What makes your service different than others?"
response = chain({"question": query})
print(response['result'])


