from django.shortcuts import render,redirect,get_object_or_404
from.models import*

# Create your views here.
def home(request):
    v=Task.objects.all()
    return render(request, 'home.html',{'taskV':v})

def about(request):
    return render(request,"about.html")

def todo1(request):
    if request.method == 'POST':
        name= request.POST['name']
        Task1= request.POST['task']
        s=Task(Name =name, task=Task1)
        s.save()
        return redirect('/home')
    
def deltodo(request,id):
    d=Task(id=id)
    d.delete()
    return redirect('/home')

def edit(request,id):
    e=get_object_or_404 (Task, id=id)
    if request .method=='POST':
        name1=request.POST['name1']
        task1=request.POST['task2']
        e.Name =name1
        e.task=task1
        e.save()
        return redirect('/home')
    return render (request,'edit.html',{'edits':e})
