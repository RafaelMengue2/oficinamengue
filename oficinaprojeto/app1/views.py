from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Peca, Servico, Cliente, Mecanico, OrdemServico
from .forms import CarForm, PecaForm, ServicoForm, ClienteForm, MecanicoForm, OrdemServicoForm

from django.shortcuts import render

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def HomePage(request):
    cars = Car.objects.all()

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()

    return render(request, 'home.html', {'cars': cars, 'form': form})

@login_required(login_url='login')
def AddCarPage(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CarForm()

    return render(request, "addcar.html", {'form': form})

@login_required(login_url='login')
def HomePage(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})


@login_required(login_url='login')
def PecaPage(request):
    pecas = Peca.objects.all()
    return render(request, 'pecas.html', {'pecas': pecas})

@login_required(login_url='login')
def AddPecaPage(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pecas') 
    else:
        form = PecaForm()

    return render(request, 'addpecas.html', {'form': form})

@login_required(login_url='login')
def ServicoPage(request):
    servicos = Servico.objects.all()
    return render(request, 'servicos.html', {'servicos': servicos})

@login_required(login_url='login')
def AddServicoPage(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicos')
    else:
        form = ServicoForm()

    return render(request, 'addservicos.html', {'form': form})

@login_required(login_url='login')
def ClientePage(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

@login_required(login_url='login')
def AddClientePage(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente')
    else:
        form = ClienteForm()

    return render(request, 'addclientes.html', {'form': form})

@login_required(login_url='login')
def MecanicosPage(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'mecanicos.html', {'mecanicos': mecanicos})

@login_required(login_url='login')
def AddMecanicoPage(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mecanicos')
    else:
        form = MecanicoForm()

    return render(request, 'addmecanicos.html', {'form': form})

@login_required(login_url='login')
def OrdensPage(request):
    ordens = OrdemServico.objects.all()
    return render(request, 'ordens.html', {'ordens': ordens})

@login_required(login_url='login')
def AddOrdemPage(request):
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ordens')
    else:
        form = OrdemServicoForm()

    return render(request, 'addordem.html', {'form': form})