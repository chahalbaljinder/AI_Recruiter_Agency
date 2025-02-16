from openai import OpenAI

import numpy as np
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Set up your OpenAI API key
# openai.api_key = "your_openai_api_key"

client = OpenAI()


# Function to create embeddings
# source: https://platform.openai.com/docs/guides/embeddings/
def get_embedding(text, model="text-embedding-3-small"):
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding


# Sample data
documents = [
    "I love programming in Python.",
    "The weather is sunny today.",
    "OpenAI creates powerful AI tools.",
    "I enjoy hiking in the mountains.",
]

# single = get_embedding("cat")
# print(f"===>> {single}")

# # Create embeddings for each document
document_embeddings = [get_embedding(doc) for doc in documents]
# print(document_embeddings)

# Query
query = "I like coding with Javascript."
query_embedding = get_embedding(query)


# Calculate cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


# Find the most similar document
similarities = [
    cosine_similarity(query_embedding, doc_emb) for doc_emb in document_embeddings
]
most_similar_index = np.argmax(similarities)

# Output the most similar document
print(f"Query: {query}")
print(f"Most similar document: {documents[most_similar_index]}")
print(f"Similarity score: {similarities[most_similar_index]:.4f}")
