from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .forms import NoteForm
from .models import Note



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('core:login')
    else:
        form = UserCreationForm()
    
    return render(request, 'core/signup.html', {'form':form})

@login_required
def home(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'core/home.html', {'notes':notes})


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('core:home')
    else:
        form = NoteForm()
    
    return render(request, 'core/add_note.html', {'form':form})

@login_required
def edit_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = NoteForm(instance=note)

    return render(request, 'core/edit_note.html', {'form':form})

@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('core:home')

    return render(request, 'core/delete_note.html', {'note': note})
