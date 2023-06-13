from .models import Notification

def get_notifications(request):
    notifications = Notification.objects.filter(user = request.user).all()

    if notifications.__len__ == 0:
        return {
            'notifications': ''
        }

    return {
        'notifications': notifications
    }
    