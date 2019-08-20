#!/usr/bin/env python3

from api import factory

app = factory.flask

if __name__ == '__main__':
	app.run()