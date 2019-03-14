from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news'),
	path('<int:post_id>', views.post, name='post'),
]






