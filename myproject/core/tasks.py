from celery import shared_task

@shared_task
def send_welcome_email(user_email):
    print(f"Sending welcome email to {user_email}")
