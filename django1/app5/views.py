from django.shortcuts import render

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

def home(request):
    numbers = range(3, 9)
    factorials = {number: factorial(number) for number in numbers}
    
    return render(request, 'facti.html', {'factorials': factorials})