from django.shortcuts import render,redirect
from django.views import generic
from .models import ProductRegister
from .forms import addProductForm
from django.urls import reverse_lazy
from .filters import ProductFilter

# Create your views here.
class ProductCreate(generic.CreateView):
    model=ProductRegister
    template_name='product/product_add.html'
    form_class=addProductForm
    success_url=reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['action']='Add'
        context['title']='Add Product'
        return context

class ProductUpdateView(generic.UpdateView):
    model=ProductRegister
    form_class=addProductForm
    template_name='product/product_add.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['action']='Update'
        context['title']='Update Product'
        return context


class ProductListView(generic.ListView):
    model=ProductRegister
    paginate_by=10
    context_object_name='product_list'
    template_name='product/product_list.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter']=ProductFilter(self.request.GET,self.get_queryset())
        return context

class ProductDetailView(generic.DetailView):
    model=ProductRegister
    context_object_name='product'
    template_name='product/product_detail.html'





