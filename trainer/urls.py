from django.urls import path
from .views import comment_view, user_view, home_view

urlpatterns = [
    path('user/', user_view),
    path('comment/', comment_view),
    path('', home_view)
]
