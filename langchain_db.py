import time

from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
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


while True:
    # Check for new entries in 'questions' collection
    new_questions = list(questions_collection.find({"processed": {"$ne": True}}))
    
    for entry in new_questions:
        query = entry['text']
        
        # If you want to provide the entire chat history as context
        context = ". ".join([item[0] + ". " + item[1] for item in chat_history])
        full_query = context + ". " + query if context else query
        
        response = chain({"question": full_query})

        # Save user's query and model's response in chat_history
        chat_history.append((query, response['result']))
        
        # Send the response back to 'botresponses' collection
        botresponses_collection.insert_one({"question_id": entry["_id"], "response_text": response['result']})
        
        # Mark the question as processed
        questions_collection.update_one({"_id": entry["_id"]}, {"$set": {"processed": True}})

    time.sleep(3)  # Sleep for 10 seconds before checking again



# from langchain.document_loaders import CSVLoader
# from langchain.indexes import VectorstoreIndexCreator
# from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
# import os
# import pymongo
# import datetime
# import time

# # Set the OpenAI API key
# os.environ["OPENAI_API_KEY"] = 'open_AI_api'

# # Load the documents
# loader = CSVLoader(file_path='context7.csv')

# # Create an index using the loaded documents
# index_creator = VectorstoreIndexCreator()
# docsearch = index_creator.from_loaders([loader])

# chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

# # Create a connection to the MongoDB server
# client = pymongo.MongoClient("mongodb+srv://vrchatAdmin:il4FA64i1Mbeo8Ay@cluster0.r5gre5i.mongodb.net")

# # Select your database
# db = client["salesbot"]

# # Select the collections
# questions_collection = db["questions"]
# responses_collection = db["responses"]

# # Initialize the last_processed_id with the latest document's ID when starting the script
# latest_documents_on_start = list(questions_collection.find().sort([('_id', pymongo.DESCENDING)]).limit(1))
# last_processed_id = latest_documents_on_start[0]['_id'] if len(latest_documents_on_start) > 0 else None

# print("checking for questions...")

# while True:
#     # Get the latest document added to the questions collection
#     latest_documents = list(questions_collection.find().sort([('_id', pymongo.DESCENDING)]).limit(1))
    
#     if len(latest_documents) > 0:
#         latest_document = latest_documents[0]
        
#         # Check if this document's ID is different from the last one we processed
#         if latest_document['_id'] != last_processed_id:
#             query = latest_document["question"] 
            
#             # Process the query using the chain object
#             response_data = chain({"question": query})
#             response_text = response_data['result']
#             print(response_text)
            
#             # Upload the response to the MongoDB 'responses' collection
#             document = {
#                 "question": query,
#                 "answer": response_text,
#                 "timestamp": datetime.datetime.now()  # Adding a timestamp for record-keeping
#             }
#             responses_collection.insert_one(document)
            
#             # Update the last_processed_id to the ID of this document
#             last_processed_id = latest_document['_id']
    
#     # Sleep for 0.3 seconds to prevent spamming the database with requests
#     time.sleep(0.3)



# # from langchain.document_loaders import CSVLoader
# # from langchain.indexes import VectorstoreIndexCreator
# # from langchain.chains import RetrievalQA
# # from langchain.llms import OpenAI
# # import os
# # import joblib
# # import pymongo
# # import datetime
# # import time

# # os.environ["OPENAI_API_KEY"] = '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'
# # # Load the documents
# # loader = CSVLoader(file_path='context7.csv')

# # # Create an index using the loaded documents
# # index_creator = VectorstoreIndexCreator()
# # docsearch = index_creator.from_loaders([loader])

# # chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")
# # ########
# # # Create a connection to the MongoDB server
# # client = pymongo.MongoClient("mongodb+srv://vrchatAdmin:il4FA64i1Mbeo8Ay@cluster0.r5gre5i.mongodb.net")

# # # Select your database
# # db = client["salesbot"]

# # # Select the collection where you want to insert the document
# # collection = db["questions"]
# # responses_collection = db["botresponses"]
# # ########
# # # Initialize the last_processed_id with the latest document's ID when starting the script
# # latest_documents_on_start = list(collection.find().sort([('_id', pymongo.DESCENDING)]).limit(1))
# # last_processed_id = latest_documents_on_start[0]['_id'] if len(latest_documents_on_start) > 0 else None

# # print("checking for questions...")
# # while True:
# #     # Get the latest document added to the collection
# #     latest_documents = list(collection.find().sort([('_id', pymongo.DESCENDING)]).limit(1))
    
# #     if len(latest_documents) > 0:
# #         latest_document = latest_documents[0]
        
# #         # Check if this document's ID is different from the last one we processed
# #         if latest_document['_id'] != last_processed_id:
# #             query = latest_document["question"]  # Assuming the field is named "message"
            
# #             # Process the query here
# #             response_data = chain({"question": query})
# #             response_text = response_data['result']
# #             print(response_text)
            
# #             # Upload the response to the MongoDB 'responses' collection
# #             document = {
# #                 "question": query,
# #                 "answer": response_text,
# #                 "timestamp": datetime.datetime.now()  # Adding a timestamp for record-keeping
# #             }
# #             responses_collection.insert_one(document)
            
# #             # Update the last_processed_id to the ID of this document
# #             last_processed_id = latest_document['_id']
    
# #     # Sleep for 0.3 seconds
# #     time.sleep(0.3)


# # # import os
# # # from pymongo import MongoClient
# # # import soundfile as sf
# # # import sounddevice as sd

# # # from langchain.document_loaders import CSVLoader
# # # from langchain.indexes import VectorstoreIndexCreator
# # # from langchain.chains import RetrievalQA
# # # from langchain.llms import OpenAI
# # # import joblib

# # # os.environ["OPENAI_API_KEY"] = 'open_AI_api'

# # # # Load the documents
# # # loader = CSVLoader(file_path='context7.csv')

# # # # Create an index using the loaded documents
# # # index_creator = VectorstoreIndexCreator()
# # # docsearch = index_creator.from_loaders([loader])

# # # chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

# # # chat_history = []

# # # # Start with the bot's opening line
# # # opening_line = "Hello, I'm Jacob from AryanTech Company. I'm calling you regarding our service to assist you in securing a job. Are you looking for any job opportunities right now?"
# # # print(opening_line)

# # # # Connect to MongoDB
# # client = MongoClient("mongodb+srv://vrchatAdmin:il4FA64i1Mbeo8Ay@cluster0.r5gre5i.mongodb.net")
# # db = client['salesbot']
# # collection = db['botresponses']

# # def play_audio_from_db(response):
# #     # Search for the response in the MongoDB collection
# #     entry = collection.find_one({"response": response})
    
# #     # If the response is found, play the associated audio file
# #     if entry:
# #         object_id = str(entry['_id'])
# #         audio_filename = f"elevenlabs_audio_files/{object_id}.mp3"
# #         if os.path.exists(audio_filename):
# #             data, samplerate = sf.read(audio_filename)
# #             sd.play(data, samplerate)
# #             sd.wait()  # This keeps the play_audio_from_db function running until the audio is finished

# # while True:
# #     # Ask user for a query
# #     query = input("Please enter your query (or type 'exit' to end): ")

# #     # Exit loop if user types 'exit'
# #     if query.lower() == 'exit':
# #         break

# #     # If you want to provide the entire chat history as context
# #     context = ". ".join([entry[0] + ". " + entry[1] for entry in chat_history])
# #     full_query = context + ". " + query if context else query

# #     response = chain({"question": full_query})

# #     # Save user's query and model's response as a tuple in chat_history
# #     chat_history.append((query, response['result']))

# #     print(response['result'])

# #     play_audio_from_db(response['result'])

# # def save_chat_to_txt(filename, chat_history):
# #     with open(filename, 'w') as file:
# #         for entry in chat_history:
# #             user_query, bot_response = entry
# #             file.write(f"User: {user_query}\nBot: {bot_response}\n\n")

# # # Save the chat history to a .txt file
# # save_chat_to_txt('chat_history.txt', chat_history)
