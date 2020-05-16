from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment
from django.contrib import messages

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Twoje wiadomość została wysłana.")
            return redirect('home')
        else:
            form = CommentForm(request.POST)
    else:
        form = CommentForm()
    context = {
        'form': form,
    }
    return render(request, 'forum/forum.html', context)
