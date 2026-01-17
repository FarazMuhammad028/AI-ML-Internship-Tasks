# Task 4 – Context-Aware RAG Chatbot

## Objective
Build a context-aware conversational chatbot using **Retrieval-Augmented Generation (RAG)** with LangChain. The chatbot can:
- Remember previous conversation history
- Retrieve relevant information from external documents
- Generate accurate, grounded answers
- Be deployed interactively using Streamlit (optional)

---

## Dataset
- Any custom text corpus can be used (e.g., Wikipedia pages, manuals, notes)
- Example file: `sample.txt` in the same folder as the notebook
- The chatbot splits documents into chunks for better retrieval

---

## Methodology / Approach

1. **Document Loading**
   - Load text documents using `TextLoader` from `langchain_community`
   - Handle encoding safely to prevent errors (`utf-8` with fallback)

2. **Document Chunking**
   - Use `RecursiveCharacterTextSplitter` to split documents into manageable chunks
   - Chunk size: 500 characters with 50-character overlap

3. **Embeddings & Vector Store**
   - Generate embeddings for chunks using `HuggingFaceEmbeddings`
   - Store embeddings in **FAISS vector database** for fast retrieval

4. **RAG Chatbot**
   - Build a **ConversationalRetrievalChain** with memory
   - Use `HuggingFacePipeline` as the LLM
   - Retrieves relevant chunks from vector store and combines with chat history

5. **Testing**
   - Ask queries like `"What is the document about?"` to test chatbot responses

---

## Results
- The chatbot is **context-aware** and provides answers grounded in the uploaded documents
- Conversational memory allows **follow-up questions**
- Works on **any custom corpus** provided in `.txt` format
