import json

from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner!")


def save_log(request):
    if request.method == 'POST':
        json_req = json.loads(request.body)
        return HttpResponse(json_req.get("log", "not found"))
