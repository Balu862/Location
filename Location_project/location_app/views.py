from django.shortcuts import render, redirect, HttpResponse
from location_app.models import User, PlacesModel
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

import json


def your_view(request):
    return render(request, "location.html", data={"location_list": ""})


def sign_up_view(request):
    page_name = "signup.html"
    if request.method == "POST":
        # logic to create the user
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if not username:
            return render(
                request, page_name, {"error": True, "msg": "Username is required"}
            )
        if not email:
            return render(
                request, page_name, {"error": True, "msg": "Email is required"}
            )
        if not password:
            return render(
                request, page_name, {"error": True, "msg": "Password is required"}
            )
        if User.objects.filter(username=username).exists():
            return render(
                request,
                page_name,
                {"error": True, "msg": "This username already exists"},
            )
        if User.objects.filter(email=email).exists():
            return render(
                request, page_name, {"error": True, "msg": "This email already exists"}
            )

        User.objects.create_user(username=username, email=email, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:

            auth.login(request, user)
            return redirect("index")
        else:
            return render(
                request,
                page_name,
                {"error": True, "msg": "Authentication could not happen"},
            )
    else:
        # GET Method render the page
        return render(request, page_name)


@login_required(login_url="sign_in")
def sign_out_view(request):
    auth.logout(request)
    return redirect("sign_in")


@login_required(login_url="sign_in")
def index_view(request):
    values = PlacesModel.objects.filter(user_name=request.user)
    location_list = []
    if values:
        values = values
        for value in values:
            data = {
                "id": value.id,
                "place_name": value.place_name,
                "description": value.description,
                "latitude": value.latitude,
                "longitude": value.longitude,
                "created_at": value.created_at,
            }
            location_list.append(data)


        data = {"location_list": location_list if request.user.is_authenticated else []}

    else:
        data = {}

    return render(request, "location.html", data)


@login_required(login_url="sign_in")
def add_location_data(request):

    if request.method == "POST":

        place_name = request.POST["name"]
        description = request.POST["description"]
        lat = request.POST["lat"]
        long = request.POST["long"]
        if not place_name or not description:
            return HttpResponse("Please fill the Name and description")

        PlacesModel.objects.create(
            user_name=request.user,
            place_name=place_name,
            description=description,
            latitude=lat,
            longitude=long,
        )
    else:
        return HttpResponse("Please Use get Method")

    return redirect("index")


def sign_in_view(request):
    page_name = "sign.html"
    if request.method == "POST":
        # sign in logic
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:

            auth.login(request, user)
            return redirect("index")
        else:
            return render(
                request,
                page_name,
                {"error": True, "msg": "Authentication could not happen"},
            )
    else:
        # GET Method render the page
        return render(request, page_name)


@login_required(login_url="sign_in")
def delete_data(request, location_id):
    if request.method != "POST":
        return HttpResponse("Error method not allowed")
    else:
        location = PlacesModel.objects.get(id=location_id)
        location.delete()
        return redirect("index")


@login_required(login_url="sign_in")
def search_data(request):
    found_data = []

    if request.method == "POST":
        values = PlacesModel.objects.filter(user_name=request.user)
        search_data = request.POST["search_data"]
        for data in values:

            if (
                search_data.lower() == data.place_name.lower()
                or search_data.lower() == data.description.lower()
            ):

                found_data.append(
                    {
                        "id": data.id,
                        "place_name": data.place_name,
                        "description": data.description,
                        "latitude": data.latitude,
                        "longitude": data.longitude,
                        "created_at": data.created_at,
                        "show_flag": "Yes",
                    }
                )

    data = {"location_list": found_data}
    return render(request, "location.html", data)
