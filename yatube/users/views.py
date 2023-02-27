from django.views.generic import CreateView

from django.urls import reverse_lazy
"""Функция reverse_lazy позволяет получить URL по параметрам функции path()
Берём, тоже пригодится"""

from .forms import CreationForm
""" Импортируем класс формы, чтобы сослаться на неё во view-классе"""


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
