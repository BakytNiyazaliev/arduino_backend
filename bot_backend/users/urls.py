from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.CustomersList.as_view(), name='customers_list'),
    path("<str:rfid>/", views.get_user, name='get_user'),
    path('chat_id/<int:chat_id>/', views.get_customer_by_chat_id),
    path("chat_id/<int:chat_id>/history/", views.get_history, name="history"),
    path("phone_number/<str:phone_number>/", views.get_customer, name='customer by phone'),
    path('login/', views.login)
]