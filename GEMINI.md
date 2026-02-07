# Project Overview

This project is "The Wall," a lightweight and anonymous digital wall where users can post positive messages. The idea is inspired by the tourist destination of Thoddoo, Maldives, as a place for people to share positive vibes and things on their minds.

## Core Principles

*   **Anonymity:** This is the number one priority. The application will not store any personally identifiable information. No user accounts, no IP logging.
*   **Lightweight:** The application should be fast and efficient, with a minimal footprint.
*   **Positive Vibe:** The design and moderation will encourage positive and respectful messages.

## Technology Stack

*   **Frontend:** SvelteKit (TypeScript)
*   **Backend:** FastAPI (Python)
*   **Database:** SQLite

## Architecture

The project will be a monolith containing both the frontend and backend.

*   `frontend/`: Contains the SvelteKit application for the user interface.
*   `backend/`: Contains the FastAPI application for the API and database interactions.

---

# Building and Running

## Frontend (SvelteKit)

To run the frontend for development:

```bash
cd frontend
npm install
npm run dev
```

To build the frontend for production:

```bash
cd frontend
npm run build
```

## Backend (FastAPI)

To run the backend for development:

```bash
cd backend
# It is recommended to use a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

# Development Conventions

*   **Code Style:** We will use the default formatters for Svelte/TypeScript and Python (Prettier and Black).
*   **API:** The backend will provide a RESTful API. All endpoints should be documented using FastAPI's automatic OpenAPI documentation.
*   **Testing:** We will add unit tests for the backend API to ensure reliability.
