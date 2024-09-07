# Project Description
An intelligent job search management application.

## Technologies
- React
- FastAPI
- PostgreSQL
- Playwright
- Docker
- GitHub Actions
- WebSockets
- Celery


## Table of Contents

- [Getting Started](#getting-started)

## Getting Started

### Clone the Repository

### Setup Environment Variables
Copy the example `.env.example` file and rename it to `.env`.
Update the values in the `.env`.


### Backend Setup
```sh
cd Backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 127.0.0.1 --port 8000
```


### Frontend Setup
```sh
cd Frontend
npm install
npm run dev
```

### RabbitMQ setup
```sh
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```


### Celery Setup
```sh
cd backend
celery -A celery_worker worker --concurrency=2 --loglevel=debug --without-mingle --without-gossip --without-heartbeat -P eventlet
```







