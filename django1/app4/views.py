from django.shortcuts import render
#program1 is app4
# Create your views here.


def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

def home(request):
    n1 = 5
    square = n1 * n1
    fact = factorial(n1)
    
    context = {
        'number': n1,
        'square': square,
        'factorial': fact
    }
    
    return render(request, 'facto.html', context)