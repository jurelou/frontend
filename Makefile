PYTHON=python3
CELERY_LOGLEVEL=--loglevel=info

all: 
	$(PYTHON) run.py

frontend_app:
	celery -A run.frontend_app worker $(CELERY_LOGLEVEL)
