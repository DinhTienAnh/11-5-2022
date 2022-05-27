from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'facebook'
urlpatterns = [
    path('register/',views.register, name = 'register'),
    path('home/<str:pk>/', views.homePage, name = 'home-page'),
    path('login/',views.login, name = 'login'), 
    path('profile/<int:pk>/', views.profile, name = 'profile'),
    path('logout/',views.logoutUser, name = 'logout'),
    path('messenger/<int:pk>/', views.messenger, name='messenger')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)