from django.urls import path

from . import views

app_name = 'nonnas'
urlpatterns = [
        path('', views.homepage, name="homepage"),
        path('<int:post_id>/', views.post_detail, name="detail"),
        path('register/', views.register, name='register'),
]
