from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", chat_views.messages, name="messages"),
    path("messages", chat_views.messages, name="messages"),
    path("messages/<str:room_name>/", chat_views.room, name="room"),
    # login-section
    path(
        "auth/login/",
        LoginView.as_view(template_name="login.html"),
        name="login-user",
    ),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
