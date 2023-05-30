from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import RegisterForm
def home(request):
    return render(request,'index.html')
class signup(CreateView):
    model =User
    form_class=RegisterForm
    template_name="singup.html"
    success_url=reverse_lazy("login")
    def form_valid(self, form):

        return super().form_valid(form)
    
@login_required
def Logout(request):
    
   logout(request)
   return redirect(reverse_lazy("login"))



