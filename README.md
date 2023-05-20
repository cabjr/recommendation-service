# Vowpal Wabbit Microservice with FastAPI
![Python](https://img.shields.io/badge/python-v3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.65.2-109989?style=flat&logo=fastapi)
![Vowpal Wabbit](https://img.shields.io/badge/VowpalWabbit-8.11.0-ff69b4?style=flat&logo=vowpalwabbit)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.20-orange)
![Docker](https://img.shields.io/badge/Docker-3.3.1-blue?style=flat&logo=docker)

This project creates a microservice for generic item recommendations using Vowpal Wabbit and FastAPI. The service exposes two endpoints, one for training and one for prediction. All events are logged and persisted to an SQLite database.

## Project Structure

/vw_recommendation
/app
init.py
main.py
models.py
vw_model.py
database.py
logger.py
/logs
Dockerfile
requirements.txt


## Setup Instructions

1. Clone the repository:

```
git clone https://github.com/cabjr/recommendation-service
```


2. Navigate to the project directory:

```
cd recommendation-service
```


3. Install the dependencies:


```
pip install -r requirements.txt
```

4. Run the server:

```
uvicorn app.main:app --reload
```

The application will be accessible at `localhost:8000`.

## API Documentation

FastAPI automatically generates a Swagger UI documentation for all the endpoints. After running the server, the API documentation is accessible at `localhost:8000/docs`.

## Logging

All the events are logged into a file inside the `/logs` directory. 

## Database

The application uses SQLite for data persistence, and all events (like training and prediction) are stored in the database. SQLAlchemy is used as the ORM for handling database operations.
