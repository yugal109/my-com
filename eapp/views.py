from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from random import shuffle


# MAIN HOME PAGE
def homeFirst(request):

    # feedbackform at the bottom
    form = FeedbackForm()

    # product inorder of decreasing discount %
    product = Product.objects.all().order_by("-discount_percent")

    # product inorder of decreasing date %
    pro = Product.objects.all().order_by("-date")

    # all category list
    category = Type_Wise.objects.all()
    # all subcategory list
    sub_category = Sub_Cat.objects.all()

    # user authentication check to show total amount of product in cart logo
    if request.user.is_authenticated:

        # checking total items from cart in database
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        # checking total items from cart in sessions storage
        li = request.session.get("cart")

        # checking is session storage i empty or no
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            print(yug)
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0

    # AFTER FEEDBACK FORM SUBMIT
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thanks for your review.We will definately take it into consideration.")

            return redirect('ehomefirst')

    return render(request, 'eapp/homefirst.html', {"category": category, "form": form, "pro": pro, "product": product, "sub_category": sub_category, "total": total})


# SHOPPING PAGE
def home(request):
    #  all products form database
    products = Product.objects.all()
    product = products[::-1]

    # filter submissions
    if 'lh' in request.POST:
        product = Product.objects.all().order_by("price")
    elif 'hl' in request.POST:
        product = Product.objects.all().order_by("-price")
    elif 'id' in request.POST:
        product = Product.objects.all().order_by("-id")
    elif 'price_range' in request.POST:
        minimum = request.POST.get("min")
        maximum = request.POST.get("max")
        if minimum == "" or maximum == "" or minimum >= maximum:
            product = Product.objects.all().order_by("-id")
        else:
            product = Product.objects.filter(price__range=(minimum, maximum))

    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0

    return render(request, 'eapp/home.html', {"sub_cate": product,   "total": total})


def sub_category_wise(request, sub):

    sub_cate = Product.objects.filter(sub_categ=sub)
    if 'lh' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub).order_by("price")
    elif 'hl' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub).order_by("-price")

    elif 'id' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub).order_by("-id")
    elif 'price_range' in request.POST:
        minimum = request.POST.get("min")
        maximum = request.POST.get("max")

        if minimum == "" or maximum == "" or minimum >= maximum:
            sub_cate = Product.objects.filter(
                sub_categ=sub).order_by("-id")
        else:
            sub_cate = Product.objects.filter(
                sub_categ=sub, price__range=(minimum, maximum))

    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:

        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0

    return render(request, 'eapp/subcategory.html', {"sub_cate": sub_cate, "total": total})


def sub_category_brand_wise(request, sub, brand):
    sub_cate = Product.objects.filter(sub_categ=sub, brands=brand)
    if 'lh' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub,  brands=brand).order_by("price")
    elif 'hl' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub,  brands=brand).order_by("-price")

    elif 'id' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub, brands=brand).order_by("-id")
    elif 'price_range' in request.POST:
        minimum = request.POST.get("min")
        maximum = request.POST.get("max")

        if minimum == "" or maximum == "" or minimum >= maximum:
            sub_cate = Product.objects.filter(
                sub_categ=sub, brands=brand).order_by("-id")

        else:
            sub_cate = Product.objects.filter(
                sub_categ=sub,  brands=brand, price__range=(minimum, maximum))

    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0
    return render(request, 'eapp/subcategorybrand.html', {"sub_cate": sub_cate, "total": total})


def sub_category_material_wise(request, sub, material):
    sub_cate = Product.objects.filter(sub_categ=sub, material=material)
    if 'lh' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub, material=material).order_by("price")
    elif 'hl' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub, material=material).order_by("-price")

    elif 'id' in request.POST:
        sub_cate = Product.objects.filter(
            sub_categ=sub, material=material).order_by("-id")
    elif 'price_range' in request.POST:
        minimum = request.POST.get("min")
        maximum = request.POST.get("max")

        if minimum == "" or maximum == "" or minimum >= maximum:
            sub_cate = Product.objects.filter(
                sub_categ=sub, material=material).order_by("-id")

        else:
            sub_cate = Product.objects.filter(
                sub_categ=sub, material=material, price__range=(minimum, maximum))

    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0
    return render(request, 'eapp/subcategorymaterial.html', {"sub_cate": sub_cate, "total": total})


def mobile_category(request, category, brandphone):
    cate = Type_Wise.objects.get(types=category)
    sub_cate = Product.objects.filter(category=cate, brands=brandphone)

    if 'lh' in request.POST:
        sub_cate = Product.objects.filter(
            category=cate, brands=brandphone).order_by("price")
    elif 'hl' in request.POST:
        sub_cate = Product.objects.filter(
            category=cate, brands=brandphone).order_by("-price")

    elif 'id' in request.POST:
        sub_cate = Product.objects.filter(
            category=cate, brands=brandphone).order_by("-id")
    elif 'price_range' in request.POST:
        minimum = request.POST.get("min")
        maximum = request.POST.get("max")

        if minimum == "" or maximum == "" or minimum >= maximum:
            sub_cate = Product.objects.filter(
                category=cate, brands=brandphone).order_by("-id")

        else:
            sub_cate = Product.objects.filter(
                category=cate, brands=brandphone, price__range=(minimum, maximum))

    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0
    return render(request, 'eapp/mobilecategory.html', {"sub_cate": sub_cate, "total": total})


def contact(request):
    total = 0
    for quan in OrderItems.objects.filter(user=request.user, ordered=False):
        total += quan.quantity
    return render(request, 'eapp/contact.html', {"total": total})


# REGISTER PAGE
def registerPage(request):
    # if already authenticated return to logout page to logoutfirst
    if request.user.is_authenticated:
        return redirect('loginPage')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            # if registration form valid
            if form.is_valid():
                form.save()
                messages.success(
                    request, "You have been successfully registered.")

                return redirect('loginPage')
            # if not
            else:
                messages.warning(
                    request, "Registration failed !!!"
                    "This could be due to: Error in filling the registration forms. ")
                return redirect('registerPage')

    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0

    context = {"form": form, "total": total}
    return render(request, "eapp/register.html", context)

# lOGINPAGE


def loginPage(request):
    # if user already authenticated redirect to logoutpage to logout first

    if request.user.is_authenticated:
        return redirect('logoutPage')
    # else
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            # after getting username and password checking it
            user = authenticate(request, username=username,
                                password=password)

            # if there exists any user with that username and password then

            if user is not None:

                # logging the user in
                login(request, user)

                messages.success(
                    request, f"{request.user} have successfully  logged in.")

                li = request.session.get("cart")

                # checking if session storage is empty or not
                test = not bool(li)
                # if not empty
                if test == False:
                    # list of the values of the dicionary
                    # example {"12":10},"13":9} this gives [10,9]
                    yug = list(request.session.get('cart').values())
                    # chainging string list into integer
                    yug = list(map(int, yug))
                    totals = 0
                    for i in yug:

                        totals += i

                    # getting the session storage which is in dictionary form which has id of product and the ordered quantity
                    li = request.session.get('cart')

                    # if the cart is not empty pushing the session storage data in database
                    if totals != 0:
                        # looping through id of product and their quantity
                        for ids, value in li.items():

                            item = get_object_or_404(Product, id=int(ids))

                            # creating object in database of corresponding session storage
                            order_item = OrderItems.objects.create(

                                user=request.user, item=item, ordered=False, quantity=value)
                            order_item.save()

                        return redirect("echeckout")

                return redirect("ehomefirst")

            else:
                # if the user with that username and password dosnot exist
                messages.success(
                    request, "Either Username or Password didn't match.")

                return redirect('loginPage')

    li = request.session.get("cart")
    test = not bool(li)
    if test == False:
        yug = list(request.session.get('cart').values())
        yug = list(map(int, yug))
        total = 0
        for i in yug:
            total += i
    else:
        total = 0

    context = {"total": total}

    return render(request, "eapp/login.html", context)

# LOGOUTPAGE


@ login_required(login_url='loginPage')
def logoutPage(request):

    if request.method == "POST":
        # logout the user
        logout(request)
        messages.success(
            request, f"You have successfully  logged out.")

        return redirect('ehomefirst')

    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0
    return render(request, 'eapp/logout.html', {"total": total})


def categoryPage(request, pk_str):

    # getting the category
    type_wise = get_object_or_404(Type_Wise, types=pk_str)

    #  getting products according to their catgeory
    categoryproduct = Product.objects.filter(category=type_wise)

    # submission data
    if 'lh' in request.POST:
        categoryproduct = Product.objects.filter(
            category=type_wise).order_by("price")
    elif 'hl' in request.POST:
        categoryproduct = Product.objects.filter(
            category=type_wise).order_by("-price")
    elif 'id' in request.POST:
        categoryproduct = Product.objects.filter(
            category=type_wise).order_by("-id")
    elif 'price_range' in request.POST:
        minimum = request.POST.get("min")
        maximum = request.POST.get("max")

        if minimum == "" or maximum == "" or minimum >= maximum:
            categoryproduct = Product.objects.filter(
                category=type_wise).order_by("-id")

        else:
            categoryproduct = Product.objects.filter(
                price__range=(minimum, maximum), category=type_wise)

    total = 0
    if request.user.is_authenticated:
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0

    return render(request, 'eapp/categorywise.html', {'sub_cate': categoryproduct, "total": total})


def oneProduct(request, slug):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Anonymus"
    # getting product according to slug
    product = get_object_or_404(Product, slug=slug)

    # getting reviews of the chosen product
    reviews = CommentModel.objects.filter(
        product=product)
    questions = reviews[::-1]

    comment_id = list(range(1, len(reviews)+1))
    print(comment_id)

    new_list = []

    for i in range(len(reviews)):
        new_list.append((questions[i], comment_id[i]))

    question = new_list
    total_reviews = len(reviews)

    # getting question of the chosen product
    prashna = Questions.objects.filter(products=product)
    prash = prashna[::-1]

    # getting ratings of the chosen product
    ratings = RatingModel.objects.filter(product=product)
    total_ratings = 0

    # calculationg average rating
    average_rating = 0
    for total_rat in ratings:
        total_ratings += total_rat.rating

    try:
        average_rating_float = total_ratings/len(ratings)

        # limiting the floating integer upto 1 decimal place
        average_rating = "{:.1f}".format(average_rating_float)

    except:
        average_rating = 0

    rating_count = len(ratings)
    order_form = OrderItemsForm()
    comment_form = CommentForm()
    question_form = QuestionsForm()
    rating_form = RatingForm()

    pro = Product.objects.filter(slug=slug)

    if request.user.is_authenticated:

        # when form is submitted
        if request.method == "POST":
            order_form = OrderItemsForm(request.POST or None)
            comment_form = CommentForm(request.POST or None)
            question_form = QuestionsForm(request.POST or None)
            rating_form = RatingForm(request.POST or None)

            # when order form is valid
            if order_form.is_valid():

                # get the product's id
                item = get_object_or_404(Product, slug=slug)
                # store the id
                item_id = item.id

                # quantity of the product added to cart
                quantity_form_field = request.POST.get("quantity")

                # checking if that object already exists in query set
                if OrderItems.objects.filter(user=request.user, item=item, ordered=False).exists():

                    # if exists : add the new quantity with existing quantity
                    item_in_list = OrderItems.objects.get(user=request.user, ordered=False,
                                                          item=item)
                    item_in_list.quantity += int(quantity_form_field)
                    item_in_list.save()
                else:
                    # if not create new item in cart
                    order_item = OrderItems.objects.create(

                        user=request.user, item=item, ordered=False, quantity=quantity_form_field)

                # filter items in cart according to current user and ordered status i.e the object is not yet ordered
                order_items = OrderItems.objects.filter(
                    user=request.user, ordered=False)

                messages.success(
                    request, f"{quantity_form_field} {item.name} has been  added to your cart.")

                return redirect(f"/product/{slug}")

            # if review form is valid
            if comment_form.is_valid():
                # get the comment
                review = request.POST.get("comment")
                # when the review was made
                date = timezone.now()
                box = CommentModel.objects.create(
                    product=product, user=request.user, comment=review, date_comment=date)
                box.save()

                messages.success(
                    request, f"Your review has been posted.")

                return redirect(f"/product/{slug}")

            # if rating form is valid
            if rating_form.is_valid():
                # get the rating
                ratings = request.POST.get("rating")
                product = get_object_or_404(Product, slug=slug)

                # create object and save
                if RatingModel.objects.filter(product=product, user=request.user).exists():
                    rating_model = RatingModel.objects.get(
                        product=product, user=request.user)
                    rating_model.rating = ratings
                    rating_model.save()
                    messages.success(
                        request, "Your rating has been updated.")
                    return redirect(f"/product/{slug}")
                else:
                    rating_box = RatingModel.objects.create(
                        product=product, user=request.user, rating=ratings)
                    rating_box.save()

                    messages.success(
                        request, f"Your rating has been posted.")

                    return redirect(f"/product/{slug}")

            # if question_form.is_valid():
            #     question = request.POST.get("question")

            #     question_box = Questions.objects.create(
            #         products=product, user=request.user, question=question)
            #     question_box.save()
            #     messages.success(
            #         request, f"Your question has been posted.")

            #     return redirect(f"/product/{slug}")

        else:
            order_form = OrderItemsForm()
            comment_form = CommentForm()
            question_form = QuestionsForm()
            rating_form = RatingForm()

        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity

    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0

    if not request.user.is_authenticated:

        # when anonymus user adds to cart
        if request.method == "POST":
            #  get the product ir form the input field
            p = request.POST.get('product')
            # get the quantity of the product
            quan = request.POST.get('quantity')

            # get the session storage
            cart = request.session.get("cart")
            # if cart exists
            if cart:
                # get the value of the dictionary for e.g.:
                # {"12":10} this gives 10 as result

                quantity = cart.get(p)
                # if there is any quantity
                if quantity:
                    # set the value of dictionary to older quantity added with the new quantity recived
                    cart[p] = int(quantity)+int(quan)
                # else
                else:
                    # set the value to new quantity received
                    cart[p] = quan
            # if session storage doesnot exist
            else:
                # make a session storage by firstof all making it a empty dictionary
                cart = {}
                # then set the value : this gives result eg: {"12":10}
                cart[p] = quan
            # create session storage
            request.session['cart'] = cart

            # getting the id of the product
            item = Product.objects.get(id=p)

            messages.success(
                request, f"{quan} {item.name} has been  added to your cart.")
            return redirect(f"/product/{slug}")

    yan = request.session.get('cart')

    context = {"product": pro, "quest": question, "username": username,
               "total_reviews": total_reviews,
               "form": comment_form, "order": order_form, "prashnas": prashna, "total": total,
               "prashna": prash, "rating_count": rating_count, "yan": yan, "ques_form": question_form, "rating_form": rating_form, "rating": average_rating}

    return render(request, "eapp/content.html", context)


@ login_required(login_url='loginPage')
def add_to_cart(request, pk):

    item = get_object_or_404(Product, id=pk)

    order_item = OrderItems.objects.create(
        user=request.user, item=item)
    ordered_date = timezone.now()
    order = Order.objects.create(
        user=request.user, ordered_date=ordered_date)
    order.items.add(order_item)

    return redirect("/")


@ login_required(login_url='loginPage')
def remove_form_cart(request, pk_id):
    ordd = OrderItems.objects.get(id=pk_id)
    ordd.delete()
    messages.success(
        request, "This product has been removed from your cart.")

    return redirect("/orderview")


@ login_required(login_url='loginPage')
def delete_whole(request):
    ordd = OrderItems.objects.all()
    ordd.delete()
    messages.success(
        request, f"Everything in the cart has been deleted.")

    return redirect("/orderview")


@ login_required(login_url='loginPage')
def delete_reviews(request, pks):

    review_model = get_object_or_404(CommentModel, id=pks)

    review_model.delete()
    slug = review_model.product.slug
    messages.success(
        request, "This review has been deleted.")

    return redirect(f"/product/{slug}")


@ login_required(login_url='loginPage')
def update_reviews(request, id):
    review_model = get_object_or_404(CommentModel, id=id)
    slug = review_model.product.slug
    form = CommentForm(instance=review_model)

    if request.method == "POST":
        comments = request.POST.get("comment")
        review_models = get_object_or_404(CommentModel, id=id)
        review_models.comment = comments
        review_models.save()
        messages.success(
            request, "Your review has been updated.")

        return redirect(f"/product/{slug}")

    return render(request, 'eapp/update.html', {"form": form})


def orderview(request):

    if request.user.is_authenticated:
        orders_orders = OrderItems.objects.filter(
            user=request.user, ordered=False)
        order_order = orders_orders[::-1]

        # get the list of items of the filtered cart items
        orders = list(order_order)
        # get the list of numbers form 1 to the total no of products
        id_list = list(range(1, len(order_order)+1))

        # combine two lists  for e.g a=[1,2] b=["one","two"] result=[[1,"one"],[2,"two"]]

        final_list = []
        for i in range(len(order_order)):
            final_list.append([orders[i], id_list[i]])

        # get the cart form
        form = OrderItemsForm()
        tot_price = 0
        total = 0

        # total no of quanity and total price to show above cart icon
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
            tot_price += quan.final_price()

        tot_price = 0
        total = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
            tot_price += quan.final_price()

        if request.method == "POST":

            # inorder to update order where the orders and buttons are in loop

            update_order = OrderItems.objects.filter(
                user=request.user, ordered=False)

            li_update = []
            for i in range(1, len(update_order)+1):
                # geeting all updated quantity from clicked buttons
                update = request.POST.get("id_update"+str(i))
                li_update.append(int(update))
            li_updates = li_update[::-1]

            # array of the items in card with their new quantity new
            main_list = []
            for i in range(len(update_order)):
                main_list.append([update_order[i], li_updates[i]])

            # updating the quantity
            for final_update in main_list:
                final_update[0].quantity = final_update[1]
                final_update[0].save()

            messages.success(
                request, "Your cart has been updated")

            return redirect(".")
        total_elements = len(final_list)
        return render(request, 'eapp/cart.html', {"order": orders_orders, "total_elements": total_elements, "final_list": final_list, "orders": orders,  "form": form, "total": total, "price": tot_price})


def orderview_anononymus(request):

    if not request.user.is_authenticated:

        new_list = []
        price_list = []
        id_list = []
        final_list = []

        li = request.session.get("cart")
        # checking if session storage id empty of not
        test = not bool(li)

        if test == False:
            # if not empty
            # make list of the session storage
            li = list(request.session.get("cart"))

            for ids in li:
                product = get_object_or_404(Product, id=ids)
                # make list of the prices of products
                prices = product.discount_price_from_percent()
                price_list.append(prices)
                new_list.append([product])

            lis = new_list
            pl = price_list
            #  list of session storages' values
            yug = list(request.session.get('cart').values())

            yug = list(map(int, yug))
            #  list of product of quantity and price of each product
            total_list = [yug[i] * pl[i]
                          for i in range(len(yug))]
            # list of numbers form 1 to no of items in session storage to give it to buttons

            id_list = list(range(1, len(yug)+1))

            # array of the product,quantity in session storage,final multiplied  price,list of the is of buttons
            for i in range(len(yug)):
                final_list.append(
                    [lis[i], yug[i], "{:.2f}".format(total_list[i]), id_list[i]])
            fl = final_list
            total_quantity = 0
            total_prices = 0
            total_price = 0
            for i in yug:
                total_quantity += i
            for i in total_list:
                total_prices += i
                total_price = "{:.2f}".format(total_prices)

        else:
            fl = []
            total_quantity = 0
            total_price = 0

        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i

        else:
            total = 0

        if request.method == "POST":

            if "update" in request.POST:
                id_update_list = []
                id_product_list = []

                for i in range(1, len(yug)+1):

                    # get values inside the quantity input with help fo id of buttons
                    id_update = request.POST.get("id_order"+str(i))

                    # values of product id
                    id_product = request.POST.get("id_product"+str(i))
                    id_update_list.append(int(id_update))
                    id_product_list.append(id_product)

                product_id_list = id_product_list
                update_list = id_update_list

                # combining to lists to form a dictionary
                carts = dict(zip(product_id_list, update_list))
                # assing that dictionary to session storage
                request.session["cart"] = carts
                messages.success(request, "Your cart has been updated")

                return redirect(".")

            li = request.session.get("cart")
            test = not bool(li)
            if test == False:

                id_product_list = list(request.session.get('cart'))

                # for deleteing each cart items
                for x in id_product_list:

                    if "id_delete"+x in request.POST:

                        # get session storage
                        new_session = request.session.get("cart")
                        # remove the selected item form session storage
                        new_session.pop(x)
                        # set the new session storage
                        request.session["cart"] = new_session
                        messages.warning(
                            request, "The product has been removed.")
                        return redirect(".")

                # clear the session storage
                if "delete_all" in request.POST:
                    new_session_storage = request.session.get("cart")
                    new_session_storage.clear()
                    request.session["cart"] = new_session_storage
                    return redirect("eorderviewanonymus")

        total_elements = len(fl)

    return render(request, 'eapp/cart_anon.html', {"fl": fl, "tot": total, "total_elements": total_elements, "total": total_quantity, "totalprice": total_price})


@ login_required(login_url='loginPage')
def checkoutPage(request):
    total = 0
    for quan in OrderItems.objects.filter(user=request.user, ordered=False):
        total += quan.quantity
    if total == 0:
        messages.warning(
            request, "You must have atleast 1 item in your cart inorder to checkout.")
        return redirect("ehome")

    if request.method == "POST":

        ordered_date = timezone.now()
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        phonenumber = request.POST.get("phonenumber")

        city = request.POST.get("city")
        state = request.POST.get("state")
        price = request.POST.get("price")
        ordered_date = timezone.now()

        try:
            if int(phonenumber) > 0 and (len(phonenumber)) == 10:
                order = Order.objects.create(
                    user=request.user, ordered_date=ordered_date, ordered=True, first_name=first_name, last_name=last_name,
                    address1=address1, address2=address2,
                    phonenumber=phonenumber, city=city, state=state, price=price)

                o = OrderItems.objects.filter(
                    user=request.user, ordered=False, latest=True)
                for orr in o:
                    orr.ordered = True
                    orr.save()
                orders = OrderItems.objects.filter(
                    user=request.user, ordered=True, latest=True)
                order.items.add(*orders)
                od = OrderItems.objects.filter(
                    user=request.user, ordered=True)
                for orr in od:
                    orr.latest = False
                    orr.save()

                messages.success(
                    request, "Congratulations !!! Your order has been placed.")

                return redirect("ehome")
        except:
            messages.warning(
                request, "The phone number must contain exaclty 10 numbers.")

            return redirect("echeckout")

    if request.user.is_authenticated:
        total = 0
        tot_price = 0
        for quan in OrderItems.objects.filter(user=request.user, ordered=False):
            total += quan.quantity
            tot_price += quan.final_price()

    else:
        li = request.session.get("cart")
        test = not bool(li)
        if test == False:
            yug = list(request.session.get('cart').values())
            yug = list(map(int, yug))
            total = 0
            for i in yug:
                total += i
        else:
            total = 0
            tot_price = 0
    return render(request, 'eapp/checkout.html', {"total": total, "tot_price": tot_price})
