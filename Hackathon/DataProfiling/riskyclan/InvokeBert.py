
from sentence_transformers import SentenceTransformer
# Load a pre-trained BERT-based model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Example sentences
sentences = ["BERT embeddings are powerful.", "Machine learning is amazing!"]

# Generate embeddings
embeddings = model.encode(sentences)

# Print the first sentence's embedding
print(embeddings[0])