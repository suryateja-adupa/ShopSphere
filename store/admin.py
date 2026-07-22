from django.contrib import admin
from .models import Category, Product, Cart, Order, OrderItem
from .models import Wishlist
from .models import Review
from .models import Profile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Wishlist)
admin.site.register(Review)
admin.site.register(Profile)
