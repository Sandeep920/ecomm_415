from .views import *
from django.urls import path
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('product/<slug>', ProductDetailView.as_view(), name='product'),
    path('search', SearchView.as_view(), name='search'),
    path('product_review/<slug>', productReview, name='product_review'),
    path('signup', signup, name='signup'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),

]