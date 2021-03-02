from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('<int:num>',views.index,name='home'),
    path('sort/<int:num>', views.sort, name='sort'),
    path('add', views.add,name='add'),
    path('updata/<int:num>', views.updata, name='updata'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('complete/<int:num>', views.complete, name='complete'),
    path('completion_home', views.completion_home, name='completion_home'),
    path('completion_home<int:num>', views.completion_home, name='completion_home'),

]