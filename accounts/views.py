from django.shortcuts import render
from accounts.models import User
from django.views import View
from accounts.forms import UserSignUpForm
from django.contrib import messages

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
            return render(request, 'index.html', {'form':form})
        return render(request, self.template_name, {'form':form})