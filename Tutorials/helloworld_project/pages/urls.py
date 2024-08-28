from django.urls import path
from pages import views as Views
from .utils import ImageLocalStorage

urlpatterns = [
    path('', Views.HomePageView.as_view(), name='home'),
    path('about/', Views.AboutPageView.as_view(), name='about'),
    path('contact/', Views.ContactPageView.as_view(), name='contact'),
    path('products/', Views.ProductIndexView.as_view(), name='index'),
    path('products/create', Views.ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', Views.ProductShowView.as_view(), name='show'),
    path('success/', Views.success_view, name='success'),
    path('cart/', Views.CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', Views.CartView.as_view(), name='cart_add'),
    path('cart/removeAll', Views.CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', Views.ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', Views.ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('imagenotdi/', Views.ImageViewNoDI.as_view(), name='imagenodi_index'),
    path('image/save', Views.ImageViewNoDI.as_view(), name='imagenodi_save'),
]
