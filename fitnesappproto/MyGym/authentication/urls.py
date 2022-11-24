from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/signin', views.signin, name="signin"),
    path('/kcalcounter', views.kcalcounter, name="kcalcounter"),
    path('/signup', views.signup, name="signup")
]

