from django.urls import path
from .views import SpeechRecognitionView

urlpatterns = [
    path('recognize/', SpeechRecognitionView.as_view(), name='recognize'),
]