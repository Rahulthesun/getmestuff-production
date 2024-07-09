from django.urls import path , include
from .views import CreatorLogin, LogoutView , CreatorSignup , CreateGoal, LiveGoalLink
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("" , views.landing_page , name="landing_page"),
    path("login/" , CreatorLogin.as_view() , name='login'),
    path("logout/" , LogoutView.as_view(next_page = 'login') , name='logout'),
    path("signup/" , CreatorSignup.as_view() , name='signup'),
    path("home/" , views.homepage , name='home'),
    path("create_goal/", CreateGoal.as_view(), name="create_goal"),
    path("goal_preview/<int:pk>/" , views.GoalPreview , name="goal_preview"),
    path("live_goal_link/<int:pk>/" ,LiveGoalLink.as_view() , name='live_goal' ),
    path("payment/<int:pk>/" , views.payment , name='payment'),
    path("payment_success/<int:pk>/" , views.payment_success , name="payment_success"),
    path("payment_failure/<int:pk>/" , views.payment_failure , name="payment_failure"),
    path("payment_status/<int:pk>/" , views.payment_status , name='payment_status'),
    path("paypal/" , include('paypal.standard.ipn.urls'))
    ] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)