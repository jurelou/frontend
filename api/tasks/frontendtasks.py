from api import factory

front = factory.frontend_broker
back = factory.engine_broker

def toto():
	print("Sending task to engine")
	back.send_task("opulence.engine.run.add")
	pass