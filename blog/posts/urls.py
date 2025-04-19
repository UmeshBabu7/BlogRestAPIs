from django.urls import path
from .import views

app_name="posts"

urlpatterns = [
    path('',views.post_list,name="list"),
    path('create/',views.post_create),
    path('detail/<int:id>/',views.post_detail,name="detail"),
    path('update/<int:id>/',views.post_update),
    path('delete/<int:id>/',views.post_delete),
]
