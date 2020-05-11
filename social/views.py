from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView, DetailView, ListView

from social.models import Profile

@method_decorator(login_required,name="dispatch")
class HomeView(TemplateView):
    template_name = 'index.html'

class ProfileEdit(UpdateView):
    model = Profile
    fields = ['name','age','status','desc',"ProfilePic",'CoverPics']

class ProfileList(ListView):
    model = Profile

class ProfileView(DetailView):
    model = Profile




