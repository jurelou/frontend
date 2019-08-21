#!/usr/bin/env python3

from app.api import factory

app = factory.flask

frontend_app = factory.frontend_app

if __name__ == '__main__':
	app.run()