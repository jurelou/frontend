PYTHON=python3
CELERY_LOGLEVEL=--loglevel=info

all: 
	$(PYTHON) run.py

frontend_worker:
	celery -A run.frontend_worker worker $(CELERY_LOGLEVEL)
