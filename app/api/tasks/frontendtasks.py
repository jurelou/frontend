from app.api import factory

front = factory.frontend_app
engine = factory.engine_app
scan = factory.scan_app

def toto():
	print("Sending task to engine")
	engine.send_task("engine.engine_app.ping")
	scan.send_task("engine.scan_app.add")