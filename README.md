# RAG-based PDF Query System

This project demonstrates an end-to-end RAG-based (Retrieval Augmented Generation) PDF query system using AWS Bedrock and FAISS.

## Features
- Upload PDFs and extract text from them
- Split text into chunks
- Generate embeddings and store them in FAISS
- Query the embeddings with a question to get responses

## Setup
1. Clone the repository.
2. Create a `.env` file and add your AWS credentials and model IDs.
3. Install the dependencies: `pip install -r requirements.txt`.
4. Run the Flask app: `python app.py`.

## API Endpoints
- `POST /upload`: Upload a PDF for processing.
- `GET /query`: Query the PDF with a question.

## Project Structure
- `app.py`: Main Flask application
- `modules/`: Contains business logic like data loading, chunking, and querying
- `uploads/`: Stores uploaded PDFs

