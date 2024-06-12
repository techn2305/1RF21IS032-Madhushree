from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

def home(request):
    if request.method == 'POST':
        number = int(request.POST.get('number', 0))
        result = factorial(number)
        return render(request, 'factorials.html', {'result': result, 'number': number})
    return render(request, 'factorials.html')