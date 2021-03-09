from django.shortcuts import render

# Create your views here.
def dinner(request, menu, num):
    context = {
        'menu': menu,
        'num': num,
    }
    return render(request, 'workshop0309/dinner.html', context)