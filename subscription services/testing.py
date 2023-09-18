### Testing continuously
import faiss
from sentence_transformers import SentenceTransformer
import json

# Load the conversation from the JSON file
with open('conversation_data.json', 'r') as file:
    loaded_conversation = json.load(file)

# Extract the responses list
responses = [item["response"] for item in loaded_conversation]

# Load FAISS index
loaded_index = faiss.read_index('faiss_index.idx')

# Load SentenceTransformer model
loaded_model = SentenceTransformer('sentence_transformer_model/')

def get_response(new_question, model, index, responses):
    # Convert new question to embedding
    new_question_embedding = model.encode([new_question])
    
    # Use FAISS to get the top 1 most similar question's index
    _, indices = index.search(new_question_embedding, 1)
    
    # Return the corresponding response
    return responses[indices[0][0]]

# Interactive terminal loop
while True:
    # Ask for a question from the user
    user_question = input("Please enter your question (or type 'exit' to stop): ")

    # Check if the user wants to exit
    if user_question.lower() == 'exit':
        print("Goodbye!")
        break

    # Get and print the response
    response = get_response(user_question, loaded_model, loaded_index, responses)
    print(f"{response}\n")