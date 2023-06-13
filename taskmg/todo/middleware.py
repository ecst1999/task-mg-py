from .models import Notification

def get_notifications(request):

    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user).all()

        return {
            'notifications': notifications
        }
    return {
        
    }