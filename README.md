# 🚀 FastAPI AI Backend Template

A production-ready FastAPI backend template for building AI-powered applications using Clean Architecture.

This repository provides a reusable project structure that separates business logic from infrastructure and allows you to rapidly build AI solutions such as Retrieval-Augmented Generation (RAG) systems, AI agents, document processing platforms, chatbots, and AI automation workflows.

---

## 🚀 Create a New Project

This repository is a GitHub Template.

To start a new AI backend:

1. Click **Use this template**.
2. Create a new repository.
3. Clone the new repository.
4. Update `.env`, project name, and README.
5. Start building your AI solution.

The template already includes:
- Clean Architecture
- FastAPI
- JWT Authentication
- MongoDB
- Repository Pattern
- Exception Handling
- AI-ready folder structure

---

# Features

- Clean Architecture
- FastAPI
- JWT Authentication
- MongoDB Support
- Vector Database Integration
- AI Agent Ready
- LangChain Compatible
- Global Exception Handling
- Dependency Separation
- Async Repository Pattern
- Modular Services
- Production Friendly

---

# Project Structure

```
app/
│
├── api/
│   ├── dependencies/
│   └── v1/
│       └── routes/
│
├── application/
│   ├── auth/
│   ├── chat/
│   ├── documents/
│   ├── rag/
│   ├── agents/
│   └── ...
│
├── infrastructure/
│   ├── database/
│   ├── auth/
│   ├── llm/
│   ├── vectorstore/
│   ├── storage/
│   └── ...
│
├── core/
│
├── schemas/
│
└── main.py
```

---

# Architecture

```
HTTP Request

        │

        ▼

API Layer

        │

        ▼

Application Layer

        │

        ▼

Infrastructure Layer

        │

        ▼

External Services
```

---

# Folder Responsibilities

## API Layer

Responsible for:

- Receiving HTTP requests
- Request validation
- Creating Commands
- Calling Application Services
- Returning HTTP responses

Business logic should **never** be written here.

---

## Application Layer

Responsible for:

- Use Cases
- Business workflows
- Service orchestration
- Calling repositories
- Raising business exceptions

---


## Infrastructure Layer

Contains implementations for:

- MongoDB
- Vector Databases
- JWT
- Password Hashing
- Storage Providers
- LLM Providers
- Embedding Models

---

## Core

Contains shared application utilities:

- Configuration
- Exception Classes
- Exception Handlers
- Middleware
- Security

---

# Design Principles

The project follows:

- Clean Architecture
- Repository Pattern
- Dependency Inversion Principle
- Single Responsibility Principle
- Separation of Concerns

---

# Request Flow

```
Client

    │

    ▼

API Route

    │

    ▼

Command DTO

    │

    ▼

Application Service

    │

    ▼

Repository Interface

    │

    ▼

Repository Implementation

    │

    ▼

MongoDB / Vector DB / LLM
```

---

# Exception Flow

```
Infrastructure

        │

        ▼

Application Exception

        │

        ▼

Global Exception Handler

        │

        ▼

JSON Response
```

---

# Suitable Projects

This template is suitable for:

- AI Chatbots
- Retrieval-Augmented Generation (RAG)
- AI Agents
- Knowledge Base Systems
- Document Intelligence
- Internal Enterprise AI
- Customer Support AI
- Hospital AI Platforms
- HR AI Assistants
- AI Automation
- Workflow Automation
- Semantic Search
- Vector Search Applications

---

# Tech Stack

- FastAPI
- MongoDB
- JWT Authentication
- LangChain
- Qdrant / Pinecone
- OpenAI / Anthropic
- Python AsyncIO

---

# Future Improvements

- Dependency Injection Container
- Unit Testing
- Docker Support
- Kubernetes Deployment
- CI/CD Pipelines
- Background Workers
- Redis
- Celery
- Monitoring
- Structured Logging

---

# License

MIT License
