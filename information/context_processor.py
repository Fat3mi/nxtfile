from .models import AboutUs

def show_info(request):
    info=AboutUs.objects.last()
    return {'info':info}