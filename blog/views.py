from django.http import HttpResponse


def anasayfa(request):
    return HttpResponse("Merhaba")
