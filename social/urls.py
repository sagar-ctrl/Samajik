
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from social import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(url="home")),
    path("home/",views.HomeView.as_view()),
    path('profile/<int:pk>',views.ProfileView.as_view()),
    path("profile/",views.ProfileList.as_view()),
    path('profile/edit/<int:pk>',views.ProfileEdit.as_view(success_url='/social'))
]
