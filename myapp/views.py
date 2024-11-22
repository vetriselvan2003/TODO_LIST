from django.shortcuts import render,redirect
from .models import track

# Create your views here.

def index(request):
    mydata=track.objects.all()
    return render(request,"index.html",{'mydata':mydata})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('a')
        notes = request.POST.get('b')
        track.objects.create(tittle=title,notes=notes)
        return redirect('index')
    return render(request,'create.html',{})

def update(request, id):
    data = track.objects.get(id=id)
    if request.method == 'POST':
        value = request.POST
        data.tittle = value.get('a')
        data.notes = value.get('b')
        data.save()
        return redirect('index')

    return render(request, 'update.html', {'data': data})

def delete(request,id):
    data=track.objects.get(id=id)
    data.delete()
    return redirect('index')
