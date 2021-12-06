from django.urls import path
from . import views
from .views import add_product

app_name = 'products'

urlpatterns = [
    path("", views.product_all, name="product_all"),
    path("<slug:slug>", views.product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", views.category_list, name="category_list"),
    path('categories/', views.categories, name='categories'),
    path('add product/', add_product, name='add_product'),
    path("search/", views.product_search, name="product_search"),
    path("search/<slug:sort_by>/", views.product_search, name="product_search"),
    path("search/<slug:sort_by>/<slug:search>/", views.product_search, name="product_search"),

]
