from .views import ContactView
from django.urls import path

urlpatterns = [
    path('v1/contact/insert', ContactView.as_view(), name = 'insert_person_to_contact')
]
