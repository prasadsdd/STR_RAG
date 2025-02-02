from langchain.vectorstores import FAISS  # Import FAISS

def get_vector_store(docs, embedding_model):
    try:
        # Attempt to load an existing FAISS index
        vectorstore_faiss = FAISS.load_local("faiss_local", embedding_model, allow_dangerous_deserialization=True)
        print("Loaded existing FAISS index")
    except Exception as e:
        print(f"Error loading FAISS index: {e}")
        # If not found, create a new FAISS index
        vectorstore_faiss = FAISS.from_documents(docs, embedding_model)
        print("Created new FAISS index")

    vectorstore_faiss.add_documents(docs)
    vectorstore_faiss.save_local("faiss_local")
    return vectorstore_faiss



