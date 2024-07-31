from django.shortcuts import render

# Create your views here.
import math

def calculate(request):
    n1 = 5
    square = n1 ** 2
    factorial = math.factorial(n1)
    context = {
        'n1': n1,
        'square': square,
        'factorial': factorial
    }
    return render(request, 'calculate.html', context)