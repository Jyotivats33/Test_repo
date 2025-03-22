from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
text = "This is a test document."
query_result = embeddings.embed_query(text)
query_result[:3]

