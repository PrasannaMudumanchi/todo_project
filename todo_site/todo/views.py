from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from datetime import datetime


# Create your views here.
def index(request):
    items_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        title = request.POST.get("title","")
        details = request.POST.get("details","")

        to_do = Todo(
            title=title,
            details=details,
            date = datetime.now()
        )
        to_do.save()
        return redirect('todo')
        # form = TodoForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('todo')

    page = {
        "list":items_list,
        "title":"TODO LIST",
    }
    return render(request,'todo/index.html',page)

def remove(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"Item Deleted...")
    return redirect('todo')
