from django.shortcuts import render
from django.http import HttpResponse
from freshapp.models import User
from . import forms

# Create your views here.
def index(request):
    home = """<html><body><h1>Welcome!</h1>
    <h2>Go to /user to see the list of user information!</h2></body></html>"""
    return HttpResponse(home)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('ERROR FROM INVALID!')

    return render(request, 'freshapp/form.html', {'form':form})

def users(request):
    user_list = User.objects.order_by('first_name')
    my_dict = {'users':user_list}
    return render(request, 'freshapp/user.html', context=my_dict)

