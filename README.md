# Space Weather Knowledge Assistant

## Overview
This project implements a chatbot that answers questions related to solar activity and space weather.  
The system combines a local knowledge base with a language model using a Retrieval-Augmented Generation (RAG) approach.
The chatbot retrieves relevant information from documents stored in the project and uses that context to generate responses. If the required information is not found in the knowledge base, the system performs a live web search and summarizes the results.

## Features
- Retrieval-Augmented Generation using local documents
- Vector embeddings and similarity search with FAISS
- Live web search fallback when information is not available in the knowledge base
- Two response modes: concise and detailed
- Display of retrieved document sources used to generate answers
- Streamlit interface with response mode selection and example questions for quick testing.

### Project Structure

```
config/
   config.py

models/
   llm.py
   embeddings.py

utils/
   rag_utils.py
   web_search.py

data/
   space_weather.txt
   solar_flares.txt
   geomagnetic_storms.txt
   isro_space_weather.txt

app.py
requirements.txt
README.md
```

## Data Sources
The knowledge base consists of curated documents related to:
- Space weather
- Solar flares
- Geomagnetic storms
- ISRO solar observation missions

These documents are stored in the `data/` directory and used by the retrieval system.

## Technologies Used
Python  
Streamlit  
LangChain  
Sentence Transformers  
FAISS  
Groq LLM API  
SerpAPI

## Running the Application
Install dependencies:
pip install -r requirements.txt

Set environment variables for API keys:
GROQ_API_KEY=your_key
SERP_API_KEY=your_key

Run the chatbot:
streamlit run app.py

## Example Questions
- What is space weather?
- What is a solar flare?
- What is the Kp index?
- How do geomagnetic storms affect satellites?

## Deployment
The application can be deployed using Streamlit Cloud.

## Author
Developed as part of an AI engineering case study assignment.
