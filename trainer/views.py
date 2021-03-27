from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home_view(request):
    return render(request, "home.html", {})

@csrf_exempt
def user_view(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        context["method"] = "POST"
        for value in request.POST:
            context[value] = request.POST[value]

    elif request.method == "GET":
        print(request.GET)
        context["method"] = "GET"
        for value in request.GET:
            context[value] = request.GET[value]

    else:
        print("Mistake")
    return render(request, "trainer/user.html", context)


@csrf_exempt
def comment_view(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        context["method"] = "POST"
        for value in request.POST:
            context[value] = request.POST[value]

    elif request.method == "GET":
        print(request.GET)
        context["method"] = "GET"
        for value in request.GET:
            context[value] = request.GET[value]

    else:
        print("Mistake")
    return render(request, "trainer/comment.html", context)
