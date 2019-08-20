#!/usr/bin/env python3

from app.api import factory

app = factory.flask

frontend_worker = factory.frontend_broker

if __name__ == '__main__':
	app.run()