PYTHON=python3
CELERY_LOGLEVEL=--loglevel=info
HOST=$(shell hostname)
all: 
	$(PYTHON) run.py

frontend_app:
	celery -A run.frontend_app worker $(CELERY_LOGLEVEL) -n $(HOST)-frontend_app
