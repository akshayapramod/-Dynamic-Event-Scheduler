from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Session
from .forms import EventForm, SessionForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_confirm_delete.html', {'event': event})

def session_create(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event_id)
    else:
        form = SessionForm(initial={'event': event})
    return render(request, 'session_form.html', {'form': form})

def session_update(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=session.event.pk)
    else:
        form = SessionForm(instance=session)
    return render(request, 'session_form.html', {'form': form})

def session_delete(request, pk):
    session = get_object_or_404(Session, pk=pk)
    event_id = session.event.pk
    if request.method == 'POST':
        session.delete()
        return redirect('event_detail', pk=event_id)
    return render(request, 'session_confirm_delete.html', {'session': session})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to a page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')
