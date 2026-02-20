from django.shortcuts import render
from todoapp.models import Task

def home(request):
    
    tasks = Task.objects.filter(is_completed = False).order_by('-updatedAt')
    context = {'tasks':tasks}

   

    return render(request , 'home.html', context)
   # return HttpResponse('<h1> HomePage</h1>')
   