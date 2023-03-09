from django.urls import path

from . import views

app_name = 'www'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:house_id>', views.detail, name='detail'),
    path('<int:house_id>/results/', views.results, name='results'),
    path('<int:house_id>/vote/', views.vote, name='vote'),
]