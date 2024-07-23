# myproject/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения для Django настройки модуля
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')

# Создайте экземпляр Celery
app = Celery('admin')

# Используйте строку конфигурации из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживайте задачи в ваших приложениях Django
app.autodiscover_tasks()
