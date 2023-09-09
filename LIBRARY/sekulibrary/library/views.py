from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm, BookSearchForm

from django.contrib import messages


# Create your views here.


def registerpage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' " " + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, 'library\index.html')


def gallery(request):
    books = Catalogue.objects.all()
    form = BookSearchForm()
    return render(request, 'library\gallery.html', {'books': books, 'form': form})


def bookSearch(request):
    result = ''
    books = None
    title = request.GET.get("search")
    bkFilter = request.GET.get("search_by")
    print(title, bkFilter)
    if title and bkFilter:
        if bkFilter == "author":
            result = Catalogue.objects.filter(author__name__contains=title)
        elif bkFilter == "publisher":
            result = Catalogue.objects.filter(publisher__name__contains=title)
        elif bkFilter == "title":
            result = Catalogue.objects.filter(title__contains=title)
        elif bkFilter == "isbn":
            result = Catalogue.objects.filter(isbn__contains=title)
    if not result:
        result = "Sorry! no matches found"
    if not isinstance(result, str):
        books = result
    return render(request, "library/gallery.html", {"result": result, "books": books})
