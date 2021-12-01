from django.urls import path

from . import views

urlpatterns = [
        path('', views.homepage, name="homepage"),
        path('<int:post_id>/', views.post_detail),
]
