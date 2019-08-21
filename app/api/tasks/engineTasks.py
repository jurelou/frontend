from app.api import factory
from app.common.tasks import sync_call

engine_app = factory.engine_app
timeout = 5
def list_collectors():
	a  = sync_call(engine_app, "engine.engine_app", "ping", timeout)
	return a