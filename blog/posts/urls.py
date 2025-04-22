from django.urls import path
from .import views

app_name="posts"

urlpatterns = [
    path('',views.post_list,name="list"),
    path('create/',views.post_create),
    path('detail/<slug:slug>/',views.post_detail,name="detail"),
    path('update/<slug:slug>/',views.post_update),
    path('delete/<slug:slug>/',views.post_delete),
]
