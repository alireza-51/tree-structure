from django.shortcuts import render, redirect, get_object_or_404
from .models import Node
from .forms import NodeForm

def tree_view(request):
    nodes = Node.objects.all()
    return render(request, 'tree.html', {'nodes': nodes})

def add_node(request):
    if request.method == 'POST':
        form = NodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tree_view')
    else:
        form = NodeForm()
    return render(request, 'add_node.html', {'form': form})

def edit_node(request, pk):
    node = get_object_or_404(Node, pk=pk)
    if request.method == 'POST':
        form = NodeForm(request.POST, instance=node)
        if form.is_valid():
            form.save()
            return redirect('tree_view')
    else:
        form = NodeForm(instance=node)
    return render(request, 'edit_node.html', {'form': form, 'node': node})

def delete_node(request, pk):
    node = get_object_or_404(Node, pk=pk)
    node.delete()
    return redirect('tree_view')
