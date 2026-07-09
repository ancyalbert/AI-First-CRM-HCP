# AI-First CRM – HCP Module

## Project Overview

This project is an AI-First Customer Relationship Management (CRM) system for Healthcare Professionals (HCPs). It enables medical representatives to log interactions using either a structured form or a conversational AI chat interface.

The application uses LangGraph for AI agent orchestration and Groq's Gemma2-9B-IT model to process interaction requests and execute CRM-related tools.

---

## Features

* Structured HCP Interaction Form
* Conversational AI Chat Interface
* LangGraph AI Agent
* Five AI Tools

  * Log Interaction
  * Edit Interaction
  * Search HCP
  * Interaction Summary
  * Next Best Action
* FastAPI REST Backend
* React + Redux Frontend
* MySQL Database Integration
* Groq LLM Integration (Gemma2-9B-IT)

---

## Technology Stack

### Frontend

* React
* Redux Toolkit
* Axios
* React Router

### Backend

* Python
* FastAPI
* LangGraph
* LangChain
* Groq API

### Database

* MySQL
* SQLAlchemy

---

## Project Structure

```text
AI-First-CRM-HCP
│
├── backend
│   ├── ai_agent
│   ├── database
│   ├── models
│   ├── routes
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## LangGraph AI Tools

### 1. Log Interaction

Logs HCP interactions using structured or conversational input.

### 2. Edit Interaction

Updates previously logged interaction details.

### 3. Search HCP

Searches Healthcare Professional information.

### 4. Interaction Summary

Generates a concise summary of interaction details.

### 5. Next Best Action

Suggests the recommended follow-up action for the sales representative.

---

## How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## AI Model

* Groq
* gemma2-9b-it

---

## Assignment Requirements Covered

* React Frontend
* Redux State Management
* FastAPI Backend
* LangGraph AI Agent
* Groq LLM
* MySQL Database
* Form-based Interaction Logging
* Chat-based Interaction Logging
* Five LangGraph Tools

---

## Author

Ancy Albert
