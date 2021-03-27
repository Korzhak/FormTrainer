from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home_view(request):
    return render(request, "home.html", {})

@csrf_exempt
def user_view(request):
    if request.method == "POST":
        print(request.POST)

    elif request.method == "GET":
        print(request.GET)

    else:
        print("Mistake")
    return render(request, "trainer/user.html", {})


@csrf_exempt
def comment_view(request):
    if request.method == "POST":
        print(request.POST)

    elif request.method == "GET":
        print(request.GET)

    else:
        print("Mistake")
    return render(request, "trainer/comment.html", {})
