from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "number": 1000
    }
    return render(request, 'home/index.html', context)

def mavue(request):
    return HttpResponse("C'est la page deux")


def api(request):
        return JsonResponse ({"data":"Jane Doe", "proba":1000})
 