from django.test import TestCase
import pytest
from celery.result import EagerResult
from .tasks import get_users_count
# Create your tests here.
