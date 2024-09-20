from django.shortcuts import render, redirect, get_object_or_404
from .models import thing
from .forms import thingForm


# Create
def item_create(request):
    if request.method == 'POST':
        form = thingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = thingForm()
    return render(request, 'item_form.html', {'form': form})

# Read
def item_list(request):
    items = thing.objects.all()
    return render(request, 'item_list.html', {'items': items})

# Update
def item_update(request, pk):
    item = get_object_or_404(thing, pk=pk)
    if request.method == 'POST':
        form = thingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = thingForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

# Delete
def item_delete(request, pk):
    item = get_object_or_404(thing, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})



# Create your views here.
# def index(request):
#     return render(request,'index.html')

# def first(request):
#     return render(request,'first.css')