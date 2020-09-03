from django.contrib import admin

# Register your models here.
from .models import Product, CommentModel, Type_Wise,Feedbacks, RatingModel, Order, OrderItems, FinalPrice, Questions, Sub_Cat
admin.site.register((Product, CommentModel, Type_Wise,Feedbacks,
                     Order, OrderItems, FinalPrice, Questions, Sub_Cat, RatingModel))
