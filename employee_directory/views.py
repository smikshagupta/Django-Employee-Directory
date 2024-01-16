from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request, 'employee_directory/main.html',context)