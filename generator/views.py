from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    char = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        char.extend(list('0123456789'))

    if request.GET.get('special'):
        char.extend(list('!@#$%&*?'))


    length = int(request.GET.get('length'))
    passw =""
    for x in range(length):
        passw += random.choice(char)

    return render(request, 'generator/test.html', {'password':passw})

# def data(request):
#     char = list('abcdefghijklmnopqrstuvwxyz')
#     length = request.GET.get('length')
#     passw =""
#     for x in range(length):
#         passw += random.choice(char)


#     return render(request, 'generator/data.html', {'password':passw})