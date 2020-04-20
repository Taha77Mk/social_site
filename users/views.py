from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, Profilep
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'account was created for ' + user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(request, username=username, password=password)
        if account is not None:
            login(request, account)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/account_setting.html'


@login_required(login_url='login')
def account(request):
    context = {'profiles': Profile.objects.all()}
    return render(request, 'users/account_setting.html', context)


class updateprofile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ['name', 'phone', 'email', 'profile_pic']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Profile = self.get_object()
        if self.request.user == Profile.user:
            return True
        return False


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = 'users/update_profile.html'
    fields = ['name', 'phone', 'email', 'profile_pic']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
