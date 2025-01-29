# AI Agent CRUD Application

FastAPI-based AI Agent CRUD Application with PostgreSQL and React.

This project is a full-stack AI-powered application that allows users to Create, Read, Update, and Delete (CRUD) AI agents while integrating OpenAI GPT for intelligent interactions.



## Features

- FastAPI Backend with CRUD operations
- AI-Powered Responses using OpenAI's GPT and DeepSeek
- PostgreSQL Database integration with SQLAlchemy
- React & TypeScript Frontend
- RESTful API with Swagger Docs (/docs)
- JWT Authentication (Optional, for future expansion)

## Tech Stack

### Backend

- FastAPI (PYthon 3.10 +)
- SQLAlchemy (Database ORM)
- PostgreSQL (Database)
- Uvicorn (ASGI Server)
- Pydantic (Data validation)
- OpenAI API (AI-powered responses)
- DeepSeek

### Frontend

- React (Typescript)
- Axios (API requests)
- React Router (Navigation)
- Tailwind CSS (Styling)

## API Endpoints


Method	  Endpoint	       Description
POST	  /agents/	    Create an AI agent
GET	   /agents/{name}	Retrieve an AI agent
PUT	   /agents/{name}	Update an AI agent
DELETE /agents/{name}	Delete an AI agent
POST	 /ask-ai/	    AI Chatbot Interaction