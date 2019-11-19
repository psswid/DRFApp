from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_order_email(order, order_items):
    user = order.owner
    html = get_template("templates/order.html")
    txt = get_template("templates/order.txt")
    content = Context({"user": user, "order": order, "order_items": order_items})
    subject, from_email, to = (
        "Order #" + str(order.pk) + " ready",
        "order@local.loc",
        user.email,
    )
    text_content = txt.render(content)
    html_content = html.render(content)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
