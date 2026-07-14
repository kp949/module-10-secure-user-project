"""Module 10 secure FastAPI calculator application."""

import logging

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app import crud
from app.database import Base, engine, get_db
from app.operations import add, divide, multiply, subtract
from app.schemas import CalculationRequest, UserCreate, UserRead


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Module 10 Secure Calculator")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Module 10 Secure Calculator</title></head>
        <body>
            <h1>Module 10 Secure Calculator</h1>
            <p>The API is running. Try /docs to test the user endpoints.</p>
        </body>
    </html>
    """


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, user.username):
        logger.warning("Duplicate username attempted: %s", user.username)
        raise HTTPException(status_code=400, detail="Username already exists")

    if crud.get_user_by_email(db, user.email):
        logger.warning("Duplicate email attempted: %s", user.email)
        raise HTTPException(status_code=400, detail="Email already exists")

    logger.info("Creating user: %s", user.username)
    return crud.create_user(db, user)


@app.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/add")
def add_numbers(request: CalculationRequest):
    return {"result": add(request.a, request.b)}


@app.post("/subtract")
def subtract_numbers(request: CalculationRequest):
    return {"result": subtract(request.a, request.b)}


@app.post("/multiply")
def multiply_numbers(request: CalculationRequest):
    return {"result": multiply(request.a, request.b)}


@app.post("/divide")
def divide_numbers(request: CalculationRequest):
    try:
        result = divide(request.a, request.b)
    except ValueError as error:
        logger.error("Division error: %s", error)
        raise HTTPException(status_code=400, detail=str(error)) from error
    return {"result": result}

