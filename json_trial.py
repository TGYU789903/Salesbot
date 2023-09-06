import json

def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Load the documents
documents = load_json('context.json')


# Create an index using the loaded documents
# This might need modification if the library doesn't support direct list inputs
docsearch = index_creator.from_documents(documents)

# Rest of the code remains unchanged...
