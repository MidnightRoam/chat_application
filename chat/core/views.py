from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from .forms import SignUpForm


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'index.html'


# def choosechat(request):
#     return render(request, 'room_list.html')


class SignUpView(View):
    """User signup logic"""
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()

                if user and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#
#             login(request, user)
#
#             return redirect('home')
#
#     else:
#         form = SignUpForm()
#
#     return render(request, 'signup.html', {'form': form})