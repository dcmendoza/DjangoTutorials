from django.urls import path
from pages import views as Views
urlpatterns = [
    path('', Views.HomePageView.as_view(), name='home'),
    path('about/', Views.AboutPageView.as_view(), name='about'),
    path('contact/', Views.ContactPageView.as_view(), name='contact'),
    path('products/', Views.ProductIndexView.as_view(), name='index'),
    path('products/create', Views.ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', Views.ProductShowView.as_view(), name='show'),
]
