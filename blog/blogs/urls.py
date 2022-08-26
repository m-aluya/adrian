from django.urls import path

from . import views
urlpatterns = [
    path('<slug:slug>/',views.details,name='post_details'),
]