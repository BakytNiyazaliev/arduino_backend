from django.urls import path

from . import views

app_name = 'container'

urlpatterns = [
    path("", views.ContainerList.as_view()),
    path("<int:pk>", views.UpdateContainer.as_view()),
    # path('<int:pk>/report', )
    path("session/", views.session_post),
]