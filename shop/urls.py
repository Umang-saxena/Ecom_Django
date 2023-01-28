from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="ShopHome"),
    path("search/", views.search,name="Search"),
    path("tracker/", views.tracker,name="tracker"),
    path("productview/", views.productview,name="productview"),
    path("about/", views.about,name="about"),
    path("checkout/", views.checkout,name="checkout"),
    path("contacts/", views.contacts,name="contacts"),
]