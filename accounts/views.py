from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
from accounts.forms import RegisterForm
from accounts.models import LoginValue


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


# class View(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'



def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'registration/create.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/create.html', {'form': form})

    return render(request, 'homepage.html')


def add_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            login1 = form.cleaned_data.get('login')
            first_name = form.cleaned_data.get('firstname')
            email = form.cleaned_data.get('email')
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1 == pass2:
                new_user = LoginValue.objects.create(login=login1,
                                                         first_name=first_name,email=email)
                new_user.set_password(pass1)
                new_user.save()
                return render(request, 'base.html')
            form.save()

    return render(request, 'registration/create.html')