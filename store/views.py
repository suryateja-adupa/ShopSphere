from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages

from .models import Product, Cart, Order, OrderItem,  Wishlist, Review, Profile, Category


@login_required(login_url='login')
def home(request):

    categories = Category.objects.all()
    products = Product.objects.order_by('?')

    query = request.GET.get("q")

    if query:
        products = products.filter(
            name__icontains=query
        )

    return render(
        request,
        "home.html",
        {
            "products": products,
            "categories": categories,
            "query": query,
        }
    )

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "category_products.html",
        {
            "category": category,
            "products": products,
        }
    )


@login_required(login_url='login')
def product_details(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        rating = request.POST["rating"]
        comment = request.POST["comment"]

        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )

        return redirect("product_details", id=product.id)

    reviews = Review.objects.filter(product=product).order_by("-created_at")

    return render(
        request,
        "product_details.html",
        {
            "product": product,
            "reviews": reviews
        }
    )

@login_required(login_url='login')
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    Cart.objects.create(
        user=request.user,
        product=product,
        quantity=1
    )

    return redirect("home")


def register(request):
    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful!")
        return redirect("login")

    return render(request, "register.html")


def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            storage = get_messages(request)
            for _ in storage:
                pass

            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "auth/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    grand_total = 0

    for item in cart_items:
        grand_total += item.product.price * item.quantity

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "grand_total": grand_total
        }
    )


@login_required(login_url='login')
def increase_quantity(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    cart_item.quantity += 1

    cart_item.save()

    return redirect("cart")


@login_required(login_url='login')
def decrease_quantity(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    if cart_item.quantity > 1:

        cart_item.quantity -= 1
        cart_item.save()

    else:

        cart_item.delete()

    return redirect("cart")


@login_required(login_url='login')
def remove_from_cart(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    cart_item.delete()

    return redirect("cart")


@login_required(login_url='login')
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    grand_total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )
    if request.method == "POST":
        order = Order.objects.create(
            user=request.user,
            full_name=request.POST["full_name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            address=request.POST["address"],
            pincode=request.POST["pincode"],
            total_price=grand_total,
            payment_method = request.POST["payment_method"]
        )
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()
        return redirect("order_success")
    return render(
        request,
        "checkout.html",
        {
            "cart_items": cart_items,
            "grand_total": grand_total
        }
    )


@login_required(login_url='login')
def order_success(request):
    return render(request, "order_success.html")


@login_required(login_url='login')
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "my_orders.html",
        {
            "orders": orders
        }
    )

@login_required(login_url='login')
def order_details(request, id):

    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )
    order_items = OrderItem.objects.filter(order=order)
    return render(
        request,
        "order_details.html",
        {
            "order": order,
            "order_items": order_items
        }
    )

@login_required(login_url='login')
def wishlist(request):

    wishlist_items = Wishlist.objects.filter(user=request.user)

    return render(
        request,
        "wishlist.html",
        {
            "wishlist_items": wishlist_items
        }
    )


@login_required(login_url='login')
def add_to_wishlist(request, id):

    product = get_object_or_404(Product, id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect("home")


@login_required(login_url='login')
def remove_from_wishlist(request, id):

    wishlist_item = get_object_or_404(
        Wishlist,
        id=id,
        user=request.user
    )

    wishlist_item.delete()

    return redirect("wishlist")

@login_required(login_url='login')
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        "profile.html",
        {
            "profile": profile
        }
    )

@login_required(login_url='login')
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        request.user.email = request.POST["email"]
        request.user.save()

        profile.phone = request.POST["phone"]
        profile.address = request.POST["address"]

        if request.FILES.get("image"):
            profile.image = request.FILES["image"]

        profile.save()

        return redirect("profile")

    return render(
        request,
        "edit_profile.html",
        {
            "profile": profile
        }
    )