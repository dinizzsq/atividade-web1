from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/painel/')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/painel/')
        else:
            erro = 'Usuário ou senha incorretos. Tente novamente.'
            return render(request, 'login.html', {'erro': erro})


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('/')


class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'painel.html'


class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'perfil.html'
