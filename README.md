<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>

<body>

  <h1>🧠 RAG-Based Question Answering System</h1>

  <p>
    A production-ready Retrieval-Augmented Generation (RAG) system that enables intelligent question answering over custom PDF documents using Large Language Models and vector search.
  </p>

  <hr>

  <h2>📌 Overview</h2>
  <p>
    This project implements a Retrieval-Augmented Generation (RAG) pipeline that combines semantic search with LLMs to generate accurate, context-aware answers from uploaded documents.
    Users can upload PDFs and ask natural language questions.
  </p>

  <hr>

  <h2>🏗️ Architecture</h2>
  <p>
    PDF Documents → Text Extraction → Chunking → Embeddings → Vector Database (ChromaDB) → Similarity Search → LLM → Final Answer
  </p>

  <hr>

  <h2>⚙️ Tech Stack</h2>
  <ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>LangChain</li>
    <li>ChromaDB</li>
    <li>SentenceTransformers / OpenAI Embeddings</li>
    <li>Groq / OpenAI LLM</li>
  </ul>

  <hr>

  <h2>📁 Project Structure</h2>

  <pre>
rag-question-answering-system/

├── app.py
├── requirements.txt
├── .env
├── .gitignore

├── data/
│   ├── uploaded PDFs
    └──vectorstore/
      └── ChromaDB storage

├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── qa_chain.py

└── README.md
  </pre>

  <hr>

  <h2>🚀 Features</h2>
  <ul>
    <li>Upload multiple PDF documents</li>
    <li>Automatic text extraction</li>
    <li>Smart chunking strategy</li>
    <li>Semantic search using embeddings</li>
    <li>LLM-powered contextual answers</li>
    <li>Fast retrieval with ChromaDB</li>
    <li>Secure API key management using .env</li>
  </ul>

  <hr>

  <h2>🧪 How It Works</h2>
  <ol>
    <li>PDF files are uploaded</li>
    <li>Text is extracted and split into chunks</li>
    <li>Chunks are converted into embeddings</li>
    <li>Embeddings stored in ChromaDB</li>
    <li>User asks a question</li>
    <li>Relevant chunks retrieved via similarity search</li>
    <li>LLM generates final answer using context</li>
  </ol>

  <hr>

  <h2>🛠️ Installation</h2>

  <h3>1. Clone Repository</h3>
  <pre>git clone https://github.com/your-username/rag-system.git
cd rag-system</pre>

  <h3>2. Create Virtual Environment</h3>
  <pre>python -m venv venv
venv\Scripts\activate</pre>

  <h3>3. Install Dependencies</h3>
  <pre>pip install -r requirements.txt</pre>

  <h3>4. Setup Environment Variables</h3>
  <pre>GROQ_API_KEY=your_api_key_here</pre>

  <h3>5. Run Application</h3>
  <pre>streamlit run app.py</pre>

  <hr>

  <h2>🔐 Security</h2>
  <ul>
    <li>API keys stored in .env</li>
    <li>.env excluded via .gitignore</li>
    <li>No sensitive data pushed to GitHub</li>
  </ul>

  <hr>

  <h2>📈 Future Improvements</h2>
  <ul>
    <li>Support for DOCX and TXT files</li>
    <li>Cloud deployment (AWS / Streamlit Cloud / HuggingFace)</li>
    <li>Chat memory feature</li>
    <li>Multi-modal RAG (text + images)</li>
    <li>Evaluation metrics for answer quality</li>
  </ul>

  <hr>

  <h2>👩‍💻 Author</h2>
  <p>
    Arpita Gupta<br>
    Interested in AI, ML, and Backend Systems
  </p>

  <hr>

</body>
</html>
