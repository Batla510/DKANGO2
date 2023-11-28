from django.urls import path,re_path
from .views import index,user1,error

urlpatterns = [
    path('',index,name='home'),
    re_path(r'^user/(?P<login>\D+)/(?P<Nameofpapka>\D+)/(?P<num>\d+)/',user1,name='user'),
    # re_path(r'^user',user),
    path('error/',error),
    # path('user/<str:login>/<str:Nameofpapka>/<int:num>/', user1, name='user'),
]