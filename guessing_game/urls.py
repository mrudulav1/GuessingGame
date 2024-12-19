from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/', include('guessing_game.urls')),  # Link to the guessing_game app
]
