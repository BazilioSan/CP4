"""
URL configuration for newsletter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from newsletter.apps import NewsletterConfig
from newsletter.views import (MainPage,
                              RecipientListView,
                              RecipientCreateView,
                              RecipientDetailView,
                              RecipientUpdateView,
                              RecipientDeleteView,
                              MessageListView,
                              MessageCreateView,
                              MessageDetailView,
                              MessageUpdateView,
                              MessageDeleteView,
                              )


app_name = NewsletterConfig.name

urlpatterns = [
path('', MainPage.as_view(), name='main_page'),
    path('newsletter/recipient_list/', RecipientListView.as_view(), name='recipient_list'),
    path('newsletter/recipient_create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('newsletter/recipient_delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('newsletter/recipient_update/<int:pk>/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('newsletter/recipient_detail/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
    path('newsletter/message_list/', MessageListView.as_view(), name='message_list'),
    path('newsletter/message_create/', MessageCreateView.as_view(), name='message_create'),
    path('newsletter/message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('newsletter/message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('newsletter/message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]
