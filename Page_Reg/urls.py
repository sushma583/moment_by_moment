from django.urls import path,re_path
from Page_Reg import views

urlpatterns = [
    re_path(r'^$',views.home,name='home'),
]