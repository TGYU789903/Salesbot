# Required Libraries
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

# Set up the OpenAI API Key
os.environ["OPENAI_API_KEY"] = 'YOUR_OPENAI_API_KEY'  # replace with your actual key, and remember not to share this!

# Load the documents
loader = CSVLoader(file_path='path_to_your_csv.csv')

# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

# Set up the chain for retrieval
chain = RetrievalQA.from_chain_type(
    llm=OpenAI(), 
    chain_type="retrieval",  # Use "retrieval" to indicate we want to retrieve a response rather than generate one
    retriever=docsearch.vectorstore.as_retriever(),
    input_key="question"
)

# Query
query = "Tell me about services provided."
response = chain({"question": query})
print(response['result'])
