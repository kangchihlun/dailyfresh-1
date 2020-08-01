from .celery_app import app as celery_app
__all__ = ("celery_app",)


# 自定義模板操作符(還不是為了css模板的關係，轉小寫)
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def lower(value):
    return value.lower()