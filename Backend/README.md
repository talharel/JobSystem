celery -A celery_worker worker --concurrency=2 --loglevel=debug --without-mingle --without-gossip --without-heartbeat -P eventlet


uvicorn main:app --host 127.0.0.1 --port 8000