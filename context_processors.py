from users.models import UserProfile, Message, Associate
from django.contrib.auth.models import User


def user_menu(request):
    new_messages = Message.objects.filter(toUser=request.user.pk).filter(isSeen=False).count()
    associate_requests = Associate.objects.filter(requested = request.user.pk).filter(dateAccepted = None).filter(dateRemoved = None).count()

    notifications = new_messages + associate_requests

    c = {
            'new_messages': new_messages,
            'notifications': notifications,
            'associate_requests': associate_requests,
            }
    return c

