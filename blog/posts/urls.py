from django.urls import path
from .import views

urlpatterns = [
    path('',views.post_list),
    path('create/',views.post_create),
    path('detail/<int:id>/',views.post_detail,name="detail"),
    path('update/<int:id>/',views.post_update),
    path('delete/',views.post_delete),
]
