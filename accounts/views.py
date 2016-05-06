from django.shortcuts import render

# Create your views here.


def login_index(request):
    return render(request, 'accounts/login.html')


def register_index(request):
    return render(request, 'accounts/register.html')


def register_try(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
