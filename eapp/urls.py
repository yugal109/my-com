from django.urls import path
from eapp.views import home, update_reviews, delete_reviews, contact, oneProduct, orderview_anononymus, mobile_category, sub_category_material_wise, sub_category_brand_wise, sub_category_wise, categoryPage, delete_whole, homeFirst, remove_form_cart, add_to_cart, checkoutPage, orderview
urlpatterns = [
    path('', homeFirst, name="ehomefirst"),
    path('home/', home, name="ehome"),
    path('contact/', contact, name="econtact"),
    path('product/<str:slug>/', oneProduct, name="eproduct"),
    path('category/<str:pk_str>/', categoryPage, name="etype"),
    path('category/<str:category>/<str:brandphone>/',
         mobile_category, name="emobilebrand"),
    path('subcategory/<str:sub>/', sub_category_wise, name="esubtype"),

    path('subcategory/<str:sub>/brand/<str:brand>/',
         sub_category_brand_wise, name="esubtypebrand"),
    path('subcategory/<str:sub>/material/<str:material>/',
         sub_category_material_wise, name="esubtypematerial"),
    path('addcart/<str:pk>/', add_to_cart, name="ecart"),
    path('remove/<str:pk_id>/', remove_form_cart, name="eremovecart"),

    path("orderview/", orderview, name="eorderview"),
    path("orderviewanonymus/", orderview_anononymus, name="eorderviewanonymus"),
    path("checkout/", checkoutPage, name="echeckout"),

    path("deletewhole/", delete_whole, name="edeletewhole"),

    path("updatereview/<str:id>/",
         update_reviews, name="edupdatereviews"),
    path("deletereview/<str:pks>/",
         delete_reviews, name="edeletereviews"),

]
