from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

sub_category = (
    ("Airpods", "Airpods"),
    ("Bathtub", "Bathtub"),
    ("Bed", "Bed"),
    ("Bedsheet", "Bedsheet"),
    ("Belt", "Belt"),
    ("Book", "Book"),
    ("Bracelet", "Bracelet"),
    ("Camera", "Camera"),
    ("Carpet", "Carpet"),
    ("Chair", "Chair"),
    ("Charger", "Charger"),
    ("Coat", "Coat"),
    ("Colors", "Colors"),
    ("Comod", "Comod"),
    ("Copy", "Copy"),
    ("Cupboard", "Cupboard"),
    ("Curtain", "Curtain"),
    ("Handbag", "Handbag"),
    ("Headphones", "Headphones"),
    ("Jacket", "Jacket"),
    ("Laptop", "Laptop"),
    ("Mike", "Mike"),
    ("Necklace", "Necklace"),
    ("Pant", "Pant"),
    ("PC", "PC"),
    ("Pen & Pencil", "Pen & Pencil"),
    ("Pillow", "Pillow"),
    ("Purse", "Purse"),
    ("Ring", "Ring"),
    ("Shirt", "Shirt"),
    ("Shoes", "Shoes"),
    ("Slippers", "Slippers"),
    ("Soap & Shampoo", "Soap & Shampoo"),
    ("Socks", "Socks"),
    ("Sofa", "Sofa"),
    ("Table", "Table"),
    ("Toilet Paper", "Toilet Paper"),
    ("Toothbrush & paste", "Toothbrush & paste"),
    ("T-Shirt", "T-Shirt"),
    ("TV", "TV"),
    ("VideoProjector", "VideoProjector"),
    ("Watch", "Watch"),
    ("Others", "Others"),
)

BRANDS = (
    ("Acer", "Acer"),
    ("Adidas", "Adidas"),
    ("Apple", "Apple"),
    ("Canon", "Canon"),
    ("Champion", "Champion"),
    ("Colors", "Colors"),
    ("Dell", "Dell"),
    ("Fila", "Fila"),
    ("Goldstar", 'Goldstar'),
    ("Gucci", "Gucci"),
    ("Hp", "Hp"),
    ("Hubolt", "Hubolt"),
    ("Huwawei", "Huwawei"),
    ("IMac", "IMac"),
    ("Jordan", "Jordan"),
    ("Lava", "Lava"),
    ("LG", "LG"),
    ("Louis Vitton", "Louis Vitton"),
    ("Macbook", "Macbook"),
    ("Motorola", "Motorola"),
    ("Nike", "Nike"),
    ("Nikon", "Nikon"),
    ("Nokia", "Nokia"),
    ("One Plus", "One Plus"),
    ("Oppo", "Oppo"),
    ("Razor", "Razor"),
    ("Realme", "Realme"),
    ("Rolex", "Rolex"),
    ("Samsung", "Samsung"),
    ("Sony", "Sony"),
    ("Underarmour", "Underarmour"),
    ("Versace", "Versace"),
    ("Videocon", "Videocon"),
    ("Vivo", "Vivo"),
    ("Xaomi", "Xaomi"),
    ("Others", "Others")
)

MATERIAL = (
    ("Wollen", "Wollen"),
    ("Cotton", "Cotton"),
    ("Polyster", "Polyster"),
    ("Others", "Others"),
)


GENDER = (
    ("Men", "Men"),
    ("Women", "Women"),
    ("Children", "Children"),
)

COLOR = (

    ("Black", "Black"),
    ("Blue", "Blue"),
    ("Gold", "Gold"),
    ("Green", "Green"),
    ("Orange", "Orange"),
    ("Pink", "Pink"),
    ("Purple", "Purple"),
    ("Red", "Red"),
    ("Silver", "Silver"),
    ("White", "White"),
    ("Yellow", "Yellow"),
    ("Others", "Others")
)

SIZE = (
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
    ("XL", "XL"),
    ("XXL", "XXL"),
    ("3XL", "3XL"),
    ("Others", "Others"),)


class Type_Wise(models.Model):
    TYPE = (
        ('Accessories', 'Accessories'),
        ("Bathroom Items", "Bathroom Items"),
        ('Clothing', 'Clothing'),
        ('Electronics', 'Electronics'),
        ("Household Items", "Household Items"),
        ('Mobile Phones', 'Mobile Phones'),
        ("Stationery Items", "Stationery Items"),
        ("Others", "Others")
    )
    types = models.CharField(max_length=120, choices=TYPE)
    imagesc1 = models.ImageField(upload_to='eapp/images', default='')

    def __str__(self):
        return self.types


class Sub_Cat(models.Model):
    types = models.ForeignKey(Type_Wise, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=200, choices=sub_category)

    def __str__(self):
        return self.sub_category


class Product(models.Model):

    name = models.CharField(max_length=150, default='')
    category = models.ForeignKey(Type_Wise, on_delete=models.CASCADE)
    sub_categ = models.CharField(
        max_length=200, blank=True, null=True, choices=sub_category)
    brands = models.CharField(
        max_length=200, null=True, blank=True, choices=BRANDS)
    material = models.CharField(
        max_length=200, null=True, blank=True, choices=MATERIAL)
    gender = models.CharField(
        max_length=10, choices=GENDER, blank=True, null=True)
    color = models.CharField(
        max_length=10, choices=COLOR, blank=True, null=True, default=None)
    size = models.CharField(
        max_length=10, choices=SIZE, blank=True, null=True, default=None)
    price = models.IntegerField(default='')

    discount_percent = models.PositiveIntegerField(
        default=0, blank=True, null=True)
    description = models.TextField(max_length=200, default='')
    image1 = models.ImageField(
        upload_to='eapp/images', default='', blank=True, null=True)
    image2 = models.ImageField(
        upload_to='eapp/images', default='', blank=True, null=True)
    image3 = models.ImageField(
        upload_to='eapp/images', default='', blank=True, null=True)
    seller = models.CharField(
        max_length=200, blank=True, default="Respective Company")
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def discount_price_from_percent(self):
        return self.price-(self.discount_percent/100)*self.price

    def get_absolute_url(self):
        return reverse('eproduct', args=[self.slug])


class CommentModel(models.Model):

    product = models.ForeignKey(
        Product,  on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,  on_delete=models.CASCADE)
    comment = models.TextField()
    date_comment = models.DateTimeField()

    def __str__(self):
        return self.user.username+" comments : "+self.comment

    # def get_absolute_url(self):
    #     return reverse("edeletereview", kwargs={"pk": self.id,"slug":self.product.slug})


class RatingModel(models.Model):
    RATING = (
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1)
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING, default=1)

    def __str__(self):
        return self.user.username + " rates "+self.product.name+" "+str(self.rating)


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    question = models.TextField(default='', blank=True, null=True)
    answer = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.user.username+" asks : "+self.question+"product name :"+self.products.name


class OrderItems(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    latest = models.BooleanField(default=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity*self.item.price

    def discount_amount(self):
        return self.item.price-(self.item.discount_percent/100)*self.item.price

    def final_price(self):
        final = self.quantity*self.discount_amount()
        final_2dec = "{:.2f}".format(final)

        return float(final_2dec)

    def __str__(self):
        return self.item.name+" : " + str(self.quantity)+"  ||  "+" total cost : "+str(self.final_price())


class FinalPrice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(
        OrderItems, on_delete=models.CASCADE, blank=True, null=True)
    added = models.BooleanField(default=False)
    final_price = models.IntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItems)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    first_name = models.TextField(max_length=50, blank=False, null=False)
    last_name = models.TextField(max_length=50, blank=False, null=False)
    address1 = models.CharField(max_length=100, blank=False, null=False)
    address2 = models.CharField(max_length=150, blank=False, null=False)
    phonenumber = models.BigIntegerField(
        validators=[MaxLengthValidator(10), MinLengthValidator(10)])
    city = models.TextField(max_length=30, blank=False, null=False)
    state = models.TextField(max_length=30, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                blank=True, null=True, default=0, )

    def __str__(self):
        return self.user.username+" places some orders "


class Feedbacks(models.Model):
    email = models.EmailField()
    feedback = models.CharField(max_length=250)

    def __str__(self):
        return self.email
