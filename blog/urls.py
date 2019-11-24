from django.urls import path
from . import views

urlpatterns = [
    path('',views.showBlogs,name='blogs'),
    path('<int:blog_id>',views.detail,name='details')
]

