from django.shortcuts import render
from .models import Work

def show(request):
    all_work = Work.objects.all()
    render(request, 'showcase/index.html', {'all_work': all_work})
