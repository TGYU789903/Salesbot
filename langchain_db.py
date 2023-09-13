import os
from pymongo import MongoClient
import soundfile as sf
import sounddevice as sd

from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import joblib

os.environ["OPENAI_API_KEY"] = 'open_AI_api'

# Load the documents
loader = CSVLoader(file_path='context7.csv')

# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

chat_history = []

# Start with the bot's opening line
opening_line = "Hello, I'm Jacob from AryanTech Company. I'm calling you regarding our service to assist you in securing a job. Are you looking for any job opportunities right now?"
print(opening_line)

# Connect to MongoDB
client = MongoClient("mongodb+srv://vrchatAdmin:il4FA64i1Mbeo8Ay@cluster0.r5gre5i.mongodb.net")
db = client['salesbot']
collection = db['botresponses']

def play_audio_from_db(response):
    # Search for the response in the MongoDB collection
    entry = collection.find_one({"response": response})
    
    # If the response is found, play the associated audio file
    if entry:
        object_id = str(entry['_id'])
        audio_filename = f"elevenlabs_audio_files/{object_id}.mp3"
        if os.path.exists(audio_filename):
            data, samplerate = sf.read(audio_filename)
            sd.play(data, samplerate)
            sd.wait()  # This keeps the play_audio_from_db function running until the audio is finished

while True:
    # Ask user for a query
    query = input("Please enter your query (or type 'exit' to end): ")

    # Exit loop if user types 'exit'
    if query.lower() == 'exit':
        break

    # If you want to provide the entire chat history as context
    context = ". ".join([entry[0] + ". " + entry[1] for entry in chat_history])
    full_query = context + ". " + query if context else query

    response = chain({"question": full_query})

    # Save user's query and model's response as a tuple in chat_history
    chat_history.append((query, response['result']))

    print(response['result'])

    play_audio_from_db(response['result'])

def save_chat_to_txt(filename, chat_history):
    with open(filename, 'w') as file:
        for entry in chat_history:
            user_query, bot_response = entry
            file.write(f"User: {user_query}\nBot: {bot_response}\n\n")

# Save the chat history to a .txt file
save_chat_to_txt('chat_history.txt', chat_history)
