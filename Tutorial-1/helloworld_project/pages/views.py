from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title": "About us - Online Store",
        "subtitle": "About us",
        "description": "This is an about page ...",
        "author": "Developed by: Danna Mendoza",
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title": "Contact us - Online Store",
        "subtitle": "Contact us",
        "email": "danna@gmail.com",
        "adress": "Calle 1 #111-1",
        "phonenumber": "111-111-111"
        })
        return context

class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV", "price":90},
    {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":1670},
    {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":182700},
    {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":80}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id)-1]
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
            return render(request, self.template_name, viewData)
        except (IndexError, ValueError):
            # Agregar un mensaje de error
            messages.error(request, 'El ID del producto no es válido. Por favor, intenta con otro ID.')
            # Redirigir a la página de inicio
            return HttpResponseRedirect(reverse('home'))

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

class ProductCreateView(View):
    template_name = 'products/create.html'
    success_template_name = 'products/success.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return render(request, self.success_template_name, {'title': 'Product created'})
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
