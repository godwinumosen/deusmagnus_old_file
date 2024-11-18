from celery import shared_task
from .models import TeamMemberBirthday
from .views import send_birthday_reminder
from django.utils import timezone

@shared_task
def check_birthdays_task():
    today = timezone.now().date()
    birthday_people = TeamMemberBirthday.objects.filter(birthday=today)

    for person in birthday_people:
        send_birthday_reminder(person)
