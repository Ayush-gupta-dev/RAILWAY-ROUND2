from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from users.forms import LoginForm
from booking.admin import booking_admin_site
from myapp.admin import TrainAndStationAdminArea_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/admin/',booking_admin_site.urls),
    path('trainstation/admin/',TrainAndStationAdminArea_site.urls),
    path('', include('myapp.urls')),
    path('booking/',include('booking.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path("register/", user_views.register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="users/login.html", authentication_form=LoginForm),name="login"),
    path("logout/",user_views.logout,name="logout"),
    path("profile/",user_views.profile,name="profile"),
    path("accounts/",include("allauth.urls")),

]
