from django.shortcuts import render

# Create your views here.
def hi(request):
    return render(request, 'hello/hi.html')

def me_too(request):
    hi = request.GET.get('hi')
    context = {
        'hi' : hi
    }
    return render(request, 'hello/me_too.html', context)