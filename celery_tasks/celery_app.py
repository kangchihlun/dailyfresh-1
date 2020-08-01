from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# broker和worker在同一台机子上则需要加上本段代码
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django2_dailyfresh.settings-dev')
app = Celery('Django2_dailyfresh')
app.config_from_object('django.conf:settings', namespace='CELERY') #  使用CELERY_ 作为前缀，在settings中写配置
app.autodiscover_tasks()  # 发现任务文件每个app下的task.py
django.setup()