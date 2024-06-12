from django.shortcuts import render
from django.http import HttpResponse
import itertools
# Create your views here.

def home(request):
    n=6
    fact1=1
    for i in range(1,n+1,1):
        fact1=fact1*i
    return render(request,'index.html',{'param1':fact1,'param2':n})



# from django.shortcuts import render
# import itertools

# def generate_combinations(s):
#     combinations = []
#     for i in range(1, len(s) + 1):
#         combinations.extend([''.join(p) for p in itertools.permutations(s, i)])
#     return combinations

# def index(request):
#     s = "eat"
#     combinations = generate_combinations(s)
#     return render(request, 'combinations/index.html', {'combinations': combinations})


from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def generate_combinations(s):
    result = []
    def helper(current, index):
        if index == len(s):
            if current:
                result.append(current)
            return
        # Include the current character
        helper(current + s[index], index + 1)
        # Exclude the current character
        helper(current, index + 1)
    
    helper("", 0)
    return result

def home(request):
    word = "word"  # You can change this word as needed
    combinations = generate_combinations(word)
    
    return render(request, 'index.html', {'combinations': combinations, 'word': word})

from django.shortcuts import render
from itertools import permutations

def generate_combinations(s):
    perms = permutations(s)
    result = [''.join(p) for p in perms]
    return result

def home(request):
    word = "eat"  # You can change this word as needed
    combinations = generate_combinations(word)
    
    return render(request, 'index.html', {'combinations': combinations, 'word': word})


from django.shortcuts import render

def generate_combinations(s):
    if len(s) == 1:
        return [s]
    result = []
    for i, c in enumerate(s):
        rest = s[:i] + s[i+1:]
        for p in generate_combinations(rest):
            result.append(c + p)
    return result

def home(request):
    word = "eat"  # You can change this word as needed
    combinations = generate_combinations(word)
    
    return render(request, 'index.html', {'combinations': combinations, 'word': word})

