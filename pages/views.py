from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView 
from django.views import View 
from django.http import HttpResponseRedirect
 
 # Create your views here. 

class homePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 

    def get_context_data(self, **kwargs): 

        context = super().get_context_data(**kwargs) 

        context.update({ 

            "title": "About us - Online Store", 

            "subtitle": "About us", 

            "description": "This is an about page ...", 

            "author": "Developed by: Your Name", 

        }) 

 

        return context 
    
class ContactPageView(TemplateView): 
    template_name = 'pages/contact.html' 

    def get_context_data(self, **kwargs): 

        context = super().get_context_data(**kwargs) 

        context.update({ 

            "title": "Contact - Online Store", 

            "subtitle": "Email: Test@test.com", 

            "description": "Cel: 316 316 3162", 

            "author": "Direction: Cra 59b # 209-34", 

        }) 

 

        return context 
    
class Product: 

    products = [ 

        {"id":"1", "name":"TV", "description":"Best TV", "price":200}, 

        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":300}, 

        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":400}, 

        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":500} 

    ] 

 

class ProductIndexView(View): 

    template_name = 'products/index.html' 

 

    def get(self, request): 

        viewData = {} 

        viewData["title"] = "Products - Online Store" 

        viewData["subtitle"] =  "List of products" 

        viewData["products"] = Product.products 

 

        return render(request, self.template_name, viewData) 

 

class ProductShowView(View): 

    template_name = 'products/show.html' 

 

 

    def get(self, request, id): 
        try:

            viewData = {} 

            product = Product.products[int(id)-1] 

            viewData["title"] = product["name"] + " - Online Store" 

            viewData["subtitle"] =  product["name"] + " - Product information" 

            viewData["product"] = product 
        
        except:
            return HttpResponseRedirect(reverse('home'))

        return render(request, self.template_name, viewData)