import boto3  # Import boto3
from langchain.llms import Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

def get_llm_response(query):
    # Get the LLM model
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name="YOUR_REGION_NAME",  # Ensure this is correctly set or fetched from the environment
        aws_access_key_id="YOUR_AWS_ACCESS_KEY_ID",  # Ensure correct keys are used
        aws_secret_access_key="YOUR_AWS_SECRET_ACCESS_KEY",
    )
    llm = Bedrock(model_id="meta.llama3-70b-instruct-v1:0", client=client)

    prompt_template = """
    Human: Use the following pieces of context to provide a 
    concise answer to the question at the end but use at least summarize with 
    250 words with detailed explanations. If you don't know the answer, 
    just say that you don't know, don't try to make up an answer.
    <context>{context}</context>
    Question: {question}
    Assistant:"""

    # Retrieve the FAISS vector store
    faiss_index = FAISS.load_local("faiss_local", embedding_model, allow_dangerous_deserialization=True)
    
    # Define the prompt
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=faiss_index.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    response = qa_chain({"query": query})
    return response['result']



