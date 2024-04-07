from django.urls import path

from . import views

app_name = "team_members"
urlpatterns = [
    path("", views.ListView.as_view(), name="index"),
    path("create", views.CreateView.as_view(), name="create"),
    path("<int:pk>/", views.EditMemberView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.DeleteMemberView.as_view(), name="delete"),
]
