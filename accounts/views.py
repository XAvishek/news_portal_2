from django.shortcuts import render, redirect
from accounts.models import User
from django.views import View
from accounts.forms import UserSignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

class SignUpView(View):
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = UserSignUpForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            raw_password = form.cleaned_data['password1']
            user.set_password(raw_password)
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account succesfully created for {username}')
            return redirect('login')
        return render(request, self.template_name, {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            context = {
                'u_form':u_form,
                'p_form':p_form,
            }
        return render(request, 'accounts/profile.html', context)
    
