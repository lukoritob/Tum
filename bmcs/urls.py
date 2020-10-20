from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

path('dashboard/',views.dashboard  ,name="dashboard"),

path('login/',    LoginView.as_view(), name="login_url"),

path('register/', views.register,name="register_url"),

path('logout/', LogoutView.as_view(next_page='dashboard'),name="logout"),

path('bid/<int:doc>',      views.bid,name="bid"),

path('document/<str:doc>', views.board, name="document"),

path('download/<str:doc>', views.download, name="download"),

path('details/<str:doc>',     views.details, name="details"),

path('addTender/',         views.addTender, name="addTender"),

path('delete/<str:doc>',   views.delete, name="delete"),


] 

