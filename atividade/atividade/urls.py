
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.list, name="list"),
    path("add/",views.add, name='add'),
    path("detail/<int:pessoa_id>", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
]
