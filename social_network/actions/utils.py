import datetime
from django.utils import timezone
from .models import Actions


def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similiar_actions = Actions.objects.filter(
        user=user,
        verb=verb,
        created__gte=last_minute
    )
    action = Actions(user, verb, target)
    action.save()
