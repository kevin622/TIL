from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
# read(retrieve)
def index(request):
    students = Student.objects.all()
    context = {'students': students,}
    return render(request, 'orm_practice/index.html', context)

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student}
    return render(request, 'orm_practice/detail.html', context)

# create
def new(request):
    return render(request, 'orm_practice/new.html')


def create(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.hobby = request.POST.get('hobby')
        student.save()
        return redirect('detail', pk=student.id)
    return redirect('new')


# update
def edit(request, pk):
    student = Student.objects.get(pk=pk)
    context = {'student': student}
    return render(request, 'orm_practice/edit.html', context)

def update(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.major = request.POST.get('major')
        student.hobby = request.POST.get('hobby')
        student.save()
        return redirect('detail', pk=student.pk)
    return redirect('edit', pk=pk)

# delete
def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.delete()
        return redirect('index')