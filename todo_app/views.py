from django.shortcuts import render, redirect
from .models import todo
from .form import TodoForm
from django.views.decorators.http import require_POST

def home(request):
    todo_list =todo.objects.order_by("id")
    
    form =TodoForm()
    
    context ={"todo_list": todo_list, "form": form}



    return render(request, "base.html", context)
@require_POST
def addTodo(request):

    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo =todo(text=request.POST["text"])
        new_todo.save()

    return redirect("home")


def completetodo(request, id):
    todo =todo.objects.get(pk=id)
    todo.complete =True
    todo.save()

    return redirect("home")


def deletecompleted(request):
    todo.objects.filter(complete__exact=True).delete()


    return redirect("home")


def deleteall(request):
    todo.objects.all().delete()

    return redirect("home")