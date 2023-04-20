from django.shortcuts import render, redirect


def messages(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "messages.html", context)


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})
