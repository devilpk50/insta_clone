from django.urls import path
from chat.views import user_chat

app_name = 'chat'

urlpatterns = [
    path("chat/<str:username>/", user_chat, name="user_chat"),
]
