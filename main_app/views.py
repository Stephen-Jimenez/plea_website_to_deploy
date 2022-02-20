from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def bio(request):
    return render(request, 'bio.html')

def shows(request):
    context = {
        'upcoming_shows': Show.objects.filter(show_date__range=["2022-02-15", "2050-12-31"]),
        'past_shows': Show.objects.filter(show_date__range=["2016-01-01", "2022-02-14"]),
    }
    return render(request, 'shows.html', context)

def login_page(request):
    return render(request, 'login_page.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login_reg')
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        request.session['user_id'] = new_user.id
        return redirect('/shows')
    return redirect('/login_reg')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login_reg')
        this_user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = this_user.id
        return redirect('/shows')
    return redirect('/login_reg')

def logout(request):
    request.session.flush()
    return redirect('/login_reg')

def add_comment(request):
    if request.method == "POST":
        current_user = User.objects.get(id = request.session['user_id'])
        current_show = Show.objects.get(id = request.POST['id'])
        Comment.objects.create(comment = request.POST['comment'], posted_by = current_user, show_posted_on = current_show)
        return redirect('/shows')
    return redirect('/login_reg')

def media(request):
    return render(request, 'media.html')

def rsvp(request, user_id, show_id):
    current_user = User.objects.get(id = user_id)
    current_show = Show.objects.get(id = show_id)
    new_rsvp = current_show.rsvp.add(current_user)
    return redirect('/shows')

def rsvps(request, show_id):
    current_show = Show.objects.get(id = show_id)
    context = {
        'current_show_rsvps': current_show.rsvp.all()
    }
    return render(request, 'rsvps.html', context)

    
# Create your views here.