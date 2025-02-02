import boto3
from langchain.embeddings import BedrockEmbeddings
import os

def generate_embeddings():
    # Fetch the region from environment variables
    region_name = os.getenv('region_name')  # Fetch region from the .env file

    if not region_name:
        raise ValueError("AWS region is not set. Please check your .env file.")

    # Create an AWS client
    client = boto3.client(
        service_name="bedrock-runtime",
        region_name=region_name,  # Use the correct region name
        aws_access_key_id=os.getenv("aws_access_key_id"),
        aws_secret_access_key=os.getenv("aws_secret_access_key"),
    )

    embedding_model = BedrockEmbeddings(model_id="amazon.titan-embed-image-v1", client=client)
    return embedding_model






