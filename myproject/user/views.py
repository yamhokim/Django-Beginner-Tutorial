from django.shortcuts import render
from .models import User

# Create your views here.
def register_view(request):
    return render(request, "user/register.html")