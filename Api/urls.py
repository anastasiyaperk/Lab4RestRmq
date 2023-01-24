from django.urls import path

from Api.views import EchoView, UploadView, TopView

urlpatterns = [
    path('echo/', EchoView.as_view()),
    path('upload/', UploadView.as_view()),
    path('top/', TopView.as_view()),
]
