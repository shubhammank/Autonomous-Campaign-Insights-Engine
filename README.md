# Campaign Insights & Anomaly Detection

## Overview
This is a production-ready GenAI + RAG + LangGraph project.  
It includes:
- Full LangGraph Orchestration
- RAG Pipeline (Chunking, Embedding, Retrieval)
- FastAPI Microservice
- Docker Deployment
- Multi-Agent LLM Workflows

## Architecture
```mermaid
flowchart TD
    UI --> API
    API --> LangGraph
    LangGraph --> Agents
    Agents --> RAG
    RAG --> VectorDB
```

## Installation
```
pip install -r requirements.txt
uvicorn src.api.server:app --reload
```

## Run with Docker
```
docker build -t campaign_insights .
docker run -p 8080:8080 campaign_insights
```

## Folder Structure
```
src/
  api/
  agents/
  rag/
  workflows/
```

## Orchestration
LangGraph is used to manage multi-agent workflows, error handling and memory.

## RAG
Includes:
- Chunker
- Embedder (Sentence Transformers)
- Retriever (ChromaDB)
