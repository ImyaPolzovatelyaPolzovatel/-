from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Сообщение',
        'Сообщение',
        'django_test@inbox.ru',
        [user_email],
        fail_silently=False,
    )