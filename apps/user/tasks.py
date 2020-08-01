from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery_tasks import celery_app
from django.conf import settings




@celery_app.task()
def send_register_active_email(to_email, username, token):
    """define task func"""
    print('--------------- celery task called ---------------')
    subject = '天天生鲜欢迎信息'
    message = ''
    html_message = '<h1>%s, 欢迎成为天天生鲜注册会员<h1>' \
                   '请点击下面链接激活账户<br/>' \
                   '<a href="http://127.0.0.1:8000/user/active/%s">' \
                   'http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    send_mail(subject, message=message, from_email=sender, recipient_list=receiver, html_message=html_message)

