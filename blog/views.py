from django.http import HttpResponse


def anasayfa(request):
    return HttpResponse("MErhaba")


def gitle(request):
    import subprocess
    process = subprocess.Popen(["cd /home/muslu/django/pythontc", "git", "pull", "origin", "master"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return HttpResponse(output)
