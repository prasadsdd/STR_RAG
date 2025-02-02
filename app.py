
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


from flask import Flask, request, render_template, redirect, url_for
import os
from modules.data_loader import process_pdf
from modules.chunking import split_text
from modules.embeddings import generate_embeddings
from modules.vector_store import get_vector_store
from modules.llm import get_llm_response
import tempfile

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

from modules.embeddings import generate_embeddings

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file and allowed_file(file.filename):
        # Save the uploaded file to the 'uploads' folder
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # Process the PDF and create embeddings
        docs = process_pdf(filename)
        
        # Generate the embedding model
        embedding_model = generate_embeddings()

        # Pass the embedding model to get_vector_store
        vectorstore = get_vector_store(docs, embedding_model)
        
        return render_template('index.html', message="File uploaded and processed successfully!")
    
    return render_template('index.html', message="Invalid file type. Only PDF files are allowed.")


@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    if query:
        # Retrieve stored FAISS index and get response from the LLM
        response = get_llm_response(query)
        return render_template('index.html', answer=response)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

