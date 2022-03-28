from django.urls import path

from shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetails, name='details'),
    path('search', views.searching, name='search')
]
