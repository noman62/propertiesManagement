from django.http import HttpResponse


def home(request):
    response_text = (
        "Welcome to my Django application!\n"
        "Please enter the endpoint after the actual URL, e.g., /admin/"
    )
    return HttpResponse(response_text)
