from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("category/<int:id>/", views.category_products, name="category_products"),
    path("product/<int:id>/", views.product_details, name="product_details"),
    path("add-to-cart/<int:id>/", views.add_to_cart, name="add_to_cart"),

    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("cart/", views.cart, name="cart"),
    path("increase/<int:id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:id>/", views.decrease_quantity, name="decrease_quantity"),
    path("remove/<int:id>/", views.remove_from_cart, name="remove_from_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order-success/", views.order_success, name="order_success"),
    path("my-orders/", views.my_orders, name="my_orders"),
    path(
        "order-details/<int:id>/",
        views.order_details,
        name="order_details"
    ),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("add-to-wishlist/<int:id>/", views.add_to_wishlist, name="add_to_wishlist"),
    path("remove-from-wishlist/<int:id>/", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),

]
