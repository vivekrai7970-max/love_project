from django.urls import path
from . import views

urlpatterns = [
    path('', views.birthday_wish, name='birthday'),
    path('proposal/', views.proposal_page, name='proposal'),
    path('congratulations/', views.congratulations_page, name='congratulations'),
    path('memories/', views.memories_page, name='memories'),
]
