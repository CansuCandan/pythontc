from django.http import HttpResponse


def anasayfa(request):
    return HttpResponse("MErhaba")


def gitle(request):
    import subprocess
    process = subprocess.Popen(["git", "pull", "origin", "master"], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return HttpResponse(output)
