from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			messages.success(request, "Registration successful." )
# 			return redirect("login")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render(request=request, template_name="accounts/register.html", context={"register_form":form})

class RegistrationView(SuccessMessageMixin, CreateView):
    form_class = NewUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    success_message = "Registration successful."
    

# def login_user(request):

#     if request.method == 'POST':

#         username = request.POST.get('username')
#         passwd = request.POST.get('password')
#         user = authenticate(username=username, password=passwd)
    

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Invalid Username or Password')
#             return render(request, 'accounts/login.html')

#     return render(request, 'accounts/login.html')

def logout_user(request):

    logout(request)

    return redirect('home')