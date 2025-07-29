from django.shortcuts import render
from .models import task

# Create your views here.
def dashboard(request):
    tasks = task.objects.all()
    return render(request, 'dashboard.html', {'tasks': tasks})
