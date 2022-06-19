from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_contact', create_contact, name='create_contact'),
    path('view_contact', view_contact, name='view_contact'),
    path('edit_contact/<int:pk>', edit_contact, name='edit_contact'),
    path('contact_delete/<int:pk>', contact_delete, name='contact_delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
