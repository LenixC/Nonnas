from django.urls import path

from . import views

app_name = 'nonnas'
urlpatterns = [
        path('', views.homepage, name="homepage"),
        path('<int:post_id>/', views.post_detail, name="detail"),
        path('register/', views.register, name='register'),
        path('logout/', views.logout_request, name='logout'),
        path('login/', views.login_request, name='login'),
        path('new_post/', views.new_post, name='new_post'),
        path('<int:post_id>/post_comment/', views.post_comment, name="post_comment"),
]
