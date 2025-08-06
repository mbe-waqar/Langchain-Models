from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "this is a test document",
    "this is another test document",
    "Islamabad is the capital of Pakistan."
]

vector = embedding.embed_documents(documents)

print(str(vector))