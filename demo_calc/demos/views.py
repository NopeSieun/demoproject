from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required
def calculator(request):
    #data
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    #calculate
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators == '-':
        result = int(num1) - int(num2)
    elif operators == '*':
        result = int(num1) * int(num2)
    elif operators == '/':
        result = int(num1) / int(num2)
    else:
        result = 0

    #respond
    context = {'result': result}
    return render(request, 'demos/calculator.html', context)

def detail(request, pk): #404에러
    article = get_object_or_404(Article,pk=pk)
    context = {
    	'article' : article,
        }
