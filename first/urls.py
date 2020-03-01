from django.urls import path
from . import views

app_name = 'first'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.show, name='show'),
    path('<int:article_id>/comment/', views.comment, name='comment')
]
