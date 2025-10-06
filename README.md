# Gut Health Chatbot

![LLMChatbot](https://github.com/Abhiojiki/Gut_HealthChatbot/blob/main/LLMResponse.png)

## Overview
This project is designed to create a chatbot focused on gut health. It uses a pipeline to discover article URLs from sitemaps, extract and preprocess article content, chunk the text, generate embeddings, and build a FAISS vector index for efficient retrieval.

## Features
- Sitemap discovery and article extraction.
- Content cleaning and preprocessing.
- Chunking for LLM compatibility.
- Embedding generation using SentenceTransformer.
- FAISS vector index for fast retrieval.

## Repository Structure
- `Testing/`: Contains scripts for sitemap discovery, article extraction, and preprocessing.
- `combinedsitemap.csv`: Consolidated list of article URLs.
- `gut_health_articles_clean.jsonl`: Cleaned article content.
- `gut_health_article_chunks.jsonl`: Chunked text entries.
- `gut_health_faiss_index/`: FAISS vector index for retrieval.
- `llm/llm_bot.ipynb`: Notebook for preprocessing, embedding generation, and index creation.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Abhiojiki/Gut_HealthChatbot.git
   cd Gut_HealthChatbot
   ```

2. Set up the virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the sitemap discovery script:
   ```bash
   python Testing/test.py
   ```
   This will generate `combinedsitemap.csv` with article URLs.

4. Extract and preprocess articles:
   ```bash
   python Testing/extract_articles.py
   ```
   This will create `gut_health_articles_clean.jsonl`.

5. Chunk articles and create embeddings:
   ```bash
   jupyter notebook llm/llm_bot.ipynb
   ```
   Follow the steps in the notebook to generate `gut_health_faiss_index`.

## Important Notes
- **Index Creation Time**: Building the FAISS index can take significant time depending on the number of articles and chunks. Alternatively, you can download a prebuilt index for retrieval.
- **Prebuilt Index**: If you prefer not to build the index, download it from [link-to-index] and place it in the `gut_health_faiss_index/` directory.

## Usage
1. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```

2. Run the chatbot:
   ```bash
   python main.py
   ```

## License
This project is licensed under the MIT License.
