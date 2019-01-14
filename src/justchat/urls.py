from django.contrib import admin
from django.urls import path, include

from chat.views import index

urlpatterns = [
    path('chat/', include('chat.urls', namespace='chat')),
    path('admin/', admin.site.urls),
]
