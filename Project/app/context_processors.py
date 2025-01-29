from .models import Client

def client_processor(request):
    client = None
    if request.user.is_authenticated:
        client = Client.objects.filter(user=request.user).first()
    return {'client': client}
