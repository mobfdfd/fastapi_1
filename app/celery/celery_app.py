from celery import Celery
from app.config import settings

celery = Celery("tasks", broker=settings.RABBITMQ_URL, backend="rpc://")
celery.autodiscover_tasks(['app.celery.tasks'])