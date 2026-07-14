# Module 10 Secure FastAPI User Project

This is my Module 10 FastAPI project. It adds a secure user model to the calculator application using SQLAlchemy, Pydantic validation, password hashing, database tests, Docker, and GitHub Actions.

## Features

- FastAPI web application
- SQLAlchemy User model
- Unique username and email fields
- Passwords stored as hashes, not plain text
- Pydantic schemas for creating and reading users
- User API endpoints
- Calculator API endpoints from the earlier project
- Unit tests for password hashing, validation, and calculator functions
- Integration tests with a real database
- Dockerfile and Docker Compose setup
- GitHub Actions workflow for testing, Docker build, image scan, and Docker Hub push

## Project Files

- `main.py` has the FastAPI routes.
- `app/models.py` has the SQLAlchemy User model.
- `app/schemas.py` has the Pydantic schemas.
- `app/security.py` has password hashing and password verification.
- `app/crud.py` has database helper functions.
- `app/database.py` has the database connection setup.
- `tests/unit` has unit tests.
- `tests/integration` has API and database integration tests.
- `.github/workflows/ci-cd.yml` runs the CI/CD pipeline.
- `Dockerfile` builds the application image.
- `docker-compose.yml` runs FastAPI, PostgreSQL, and pgAdmin.

## Run Locally

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the application:

```powershell
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

## Run Tests Locally

```powershell
pytest
```

## Run With Docker Compose

```powershell
docker compose up --build
```

FastAPI:

```text
http://localhost:8000
```

pgAdmin:

```text
http://localhost:5050
```

pgAdmin login:

```text
Email: admin@example.com
Password: admin
```

PostgreSQL connection in pgAdmin:

```text
Host: db
Port: 5432
Username: postgres
Password: postgres
Database: fastapi_db
```

## API Endpoints

Health check:

```text
GET /health
```

Create user:

```text
POST /users
```

Example body:

```json
{
  "username": "alice",
  "email": "alice@example.com",
  "password": "Password123"
}
```

Read user:

```text
GET /users/{user_id}
```

Calculator:

```text
POST /add
POST /subtract
POST /multiply
POST /divide
```

Calculator body:

```json
{
  "a": 10,
  "b": 5
}
```

## Docker Hub

Docker Hub repository:

```text
https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/module10-fastapi-secure-users
```

Replace `YOUR_DOCKERHUB_USERNAME` with your real Docker Hub username after you create the repository.

## GitHub Actions Secrets

To let GitHub Actions push to Docker Hub, add these repository secrets in GitHub:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

The token should be a Docker Hub access token, not your regular password.

CI/CD is configured to run tests, build the Docker image, scan it, and push it to Docker Hub after a successful push to GitHub.

## Submission Screenshots

For Canvas, include:

- GitHub repository link
- Screenshot of successful GitHub Actions run
- Screenshot of Docker Hub showing the pushed image
- Reflection document

