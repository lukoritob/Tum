from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',views.indexView,name="home"),
path('dashboard/',views.dashboardView,name="dashboard"),
path('login/',LoginView.as_view(), name="login_url"),
path('register/',views.registerView,name="register_url"),
path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
path('bid/',     views.bid,name="bid"),
path("upload/",  views.model_form_upload, name="upload"),
path("doc/",     views.aboard, name="doc"),
path('input1/',  views.query1, name='input1'),
path('input2/',  views.query2, name='input2'),
path('input3/',  views.query3, name='input3'),
path('input4/',  views.query4, name='input4'),
path('input5/',  views.query5, name='input5'),
path('delete1/', views.deleteme1, name='employee_delete'),
path('edit/',    views.edit, name='edit'),
path('delete3/', views.deleteme3, name='delete3'),
path('delete4/', views.deleteme4, name='delete4'),
path('delete5/', views.deleteme5, name='delete5'),
path('display1/', views.display1, name='display1'),
path('display2/', views.display2, name='display2'),
path('display3/', views.display3, name='display3'),
path('display4/', views.display4, name='display4'),
#path('save/',     views.save,     name='save'),

path('document/<str:doc>', views.board, name="document"),

path('delete/<str:doc>', views.delete, name="delete"),

path('more/<str:doc>', views.more, name="more"),

path('add/',       views.add,       name="add"),

path('tender/',       views.add,       name="tender"),

path('addTender/', views.addTender, name="addTender"),


#path('add/', views.DocumentCreateView.as_view(), name="add"),

] 

