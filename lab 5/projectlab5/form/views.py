from django.shortcuts import render

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

people = []

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        people.append(person)
    return render(request, 'add.html')

def default(request):
    return render(request, 'default.html', {'people': people})
