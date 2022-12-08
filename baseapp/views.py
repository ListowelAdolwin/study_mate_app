from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q # This allows the use of |, &&
from .models import Room, Topic, Message, Profile
from .forms import RoomForm, UserProfileForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm



#LOGIN PAGE
def loginPage(request):
    page = 'login' # This variable confirms in the login/register to know what content to render
    # This prevents logged in users from going to the login page again
    if request.user.is_authenticated:
        return redirect('home')

    already_printed = False
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, f'User {username} is not registered ')
            already_printed = True


        user = authenticate(request, username=username, password=password)

        if user  is not None:
            login(request, user)
            return redirect('home')
        else:
            if already_printed:
                pass
            else:
                messages.error(request, 'Incorrect password entered')

    context = {'page':page,}
    return render(request, 'baseapp/login_register.html', context)

# LOGOUT
def logoutPage(request):
    logout(request)
    return redirect('home' )

# REGISTER PAGE
def registerPage(request):
    '''
    Page for users to register
    '''
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # this accesses the created user and not save it directly
            user.username = user.username.lower() # This ensures only lowercase usernames are stored in the database
            user.save()

            Profile.objects.create(
                user = user
            )
            messages.success(request, "Congratulation, registration successful")
            login(request, user)
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    context = {
        'form':form,
    }
    return render(request, 'baseapp/login_register.html', context)

# PROFILE VIEW
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.first_name = request.POST.get('first_name')
            profile.last_name = request.POST.get('last_name')
            profile.save()
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'baseapp/update_profile.html', context)

# HOME PAGE
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)  |  #contains returns any topic whose first characters match q. Since all all topics start with an empty string, '' returns all topics. i there makes the search non-case sensitive
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()[0:5]
    room_count = rooms.count()
    recent_messages = Message.objects.filter(Q(room__topic__name__icontains=q)).order_by('-updated')

    context = {
        'rooms':rooms,
        'topics': topics,
        'room_count':room_count,
        'recent_messages':recent_messages
    }
    return render(request, 'baseapp/home.html', context)

# DISPLAY ROOM
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all().order_by('-updated')
    partcipants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )

        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {
        'rooms':room,
        'room_messages': room_messages,
        'participants': partcipants,
    }
    return render(request, 'baseapp/room.html', context)

# CREATE ROOM
@login_required(login_url='login_register')
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()[0:5]
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
        )
        return redirect('home')

    context = {
        'form':form,
        'topics':topics,
    }
    return render(request, 'baseapp/create_room.html', context)

# UPDATE ROOM
@login_required(login_url='login_register') # Decorator ensures only logged in users are able to update rooms
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()


    # Two lines below ensures only hosts of a room are able to edit room
    if request.user != room.host:
        return HttpResponse('Only room admins can edit room')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        print(room)
        room.save()

        return redirect('home')

    context = {
        'form':form,
        'topics':topics,
        'room':room,
        }

    return render(request, 'baseapp/update_room.html', context)

# DELETE ROOM
@login_required(login_url='login_register')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    # Two lines below ensures only hosts of a room are able to edit room
    if request.user != room.host:
        return HttpResponse('Only room admins can edit room')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request, 'baseapp/delete.html', context)


# DELETE MESSAGE
@login_required(login_url='login_register')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    # Two lines below ensures only hosts of a room are able to edit room
    if request.user != message.user:
        return HttpResponse('Only message owner can delete message')

    if request.method == 'POST':
        message.delete()
        return redirect('room', pk=message.room.id)
    context = {'obj':message}
    return render(request, 'baseapp/delete.html', context)

# USER PROFILE
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    topics = Topic.objects.all()
    recent_messages = user.message_set.all()
    rooms = user.room_set.all()

    context = {
        'user':user,
        'topics':topics,
        'recent_messages':recent_messages,
        'rooms':rooms,
    }

    return render(request, 'baseapp/profile.html', context)
