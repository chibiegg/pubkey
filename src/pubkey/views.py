# encoding=utf-8
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from pubkey.models import PublicKey, Server
from pubkey.forms import PublicKeyForm

from django.db.models import Q

def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")

    else:
        form = AuthenticationForm(request)

    return render(request, "login.html", {"form":form})


def publickey_list(request):
    keys = PublicKey.objects.filter(user=request.user)


    return render(request, "key_list.html", {"keys":keys})


def add_publickey(request, publickey_id=None):
    
    publickey = None
    if publickey_id:
        publickey = PublicKey.objects.get(id=publickey_id)


    form = PublicKeyForm(instance=publickey)
    if request.method == "POST":
        form = PublicKeyForm(request.POST, instance=publickey)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect("publickey_list")
    
    
    return render(request, "key_form.html", {"form":form})
    


def authorized_keys(request):

    apikey = request.GET["apikey"]
    server = Server.objects.get(apikey=apikey)

    keys = PublicKey.objects.filter(Q(server=server) | Q(server=None), user=request.user)

    print keys
    return render(request, "authorized_keys.txt", {"keys":keys})








