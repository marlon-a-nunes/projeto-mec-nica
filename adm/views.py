from django.shortcuts import render, get_object_or_404, redirect
from adm.models import Client, Car
from adm.forms import Newclient, Newcar, Newservice, Newparts


def home(request):
    return render(request, 'base.html' )

def listClient(request):
    clients = Client.objects.all().order_by('-created_at')
    
    return render(request, 'listclient.html', {'clients' : clients})

def cardetail(request, id):
    client = get_object_or_404(Client, pk=id)

    return render(request, 'cardetail.html', {'client' : client})

def newclient(request):
    formclient = Newclient(Client)
    formcar = Newcar()
    formservice = Newservice()
    formparts = Newparts()
    if request.method == 'POST':
        formclient = Newclient(request.POST)
        formcar = Newcar(request.POST)
        formservice = Newservice(request.POST)
        formparts = Newparts(request.POST)
        
        if formclient.is_valid():
            formclient.save()
            
        if formcar.is_valid():
            formcar.save()
        
        if formservice.is_valid():
            formservice.save()
            
        if formparts.is_valid():
            formparts.save()
            return redirect('/listclient/')
    else:
        formclient = Newclient()
        formcar = Newcar()
        formservice = Newservice()
        formparts = Newparts()
    return render(request, 'newclient.html', {'formclient' : formclient, 'formcar' : formcar, 'formservice' : formservice, 'formparts' : formparts})

def teste(request):
    formservice = Newservice()
    if request.method == 'POST':
        if formservice.is_valid():
            formservice.save()
            return redirect('/teste/')
        
    else:
        formservice = Newservice()
    return render(request, 'teste.html', {'formservice' : formservice})
    
        
    

    
    


    
            
    
