from django.urls import path
from location_app.views import (
    your_view,
    sign_up_view,
    index_view,
    add_location_data,
    sign_in_view,
    delete_data,
    search_data,
    sign_out_view,
)

urlpatterns = [
    path("", sign_in_view, name="sign_in"),
    path("sign-up/", sign_up_view, name="sign_up"),
    path("index/", index_view, name="index"),
    path("sign-in/", sign_in_view, name="sign_in"),
    path("add/", add_location_data, name="add_location_data"),
    path("delete/<int:location_id>/", delete_data, name="delete_data"),
    path("search/", search_data, name="search"),
    path("sign-out/", sign_out_view, name="sign_out"),
]
