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
