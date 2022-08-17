from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registragion/signup.html"
    success_url = reverse("login")