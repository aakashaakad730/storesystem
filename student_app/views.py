from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpRequest,HttpResponse
from .models import ProductModel,CategoryModel,ProductList
from .forms import UserForm,ProductForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView
from django import forms

# login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/index/')
    else:
        form = AuthenticationForm()
    return render(request,'login1.html',{'form':form})

# logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponse('<h3>you have been logged out !!!</h3>')

#add products
class CreateProduct(FormView):
    form_class = ProductForm
    template_name = 'products.html'
    success_url = '/addproduct/'
    
    
#PRODUCT DETAILS WITH CATEGORY
class ProductDetails(ListView):
    model = ProductModel
    template_name = 'prod_details.html'

#UPDATE PRODUCT DETAILS   
class UpdateProductDetails(UpdateView):
    model = ProductModel
    fields = '__all__'
    template_name = 'update_prod.html'
    success_url = '/proddetails/'
    def get_form(self):
        form = super().get_form()
        form.fields['product_name'].widget=forms.TextInput(attrs={'class':'form-control'})
        form.fields['quantity'].widget=forms.TextInput(attrs={'class':'form-control'})
        form.fields['cost_price'].widget=forms.TextInput(attrs={'class':'form-control'})
        form.fields['MRP'].widget=forms.TextInput(attrs={'class':'form-control'})
        return form
    
class DeleteProductDetails(DeleteView):
    model = ProductModel
    template_name = 'delete_prod.html'
    
#Product list with image cards   
class ProductDescDetails(ListView):
    model = ProductList
    template_name = 'prod_desc.html'
    




#admin page
@login_required
def index(request):
    request.session['page'] = 'indexpage'
    request.session.modified = True
    if 'page' in request.session:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/logout/')

@login_required
def user_profile(request):
    return render(request,'profile.html')

#user registration page
@login_required
def signup_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['first_name']
            data = user_form.save()
            user_form = UserForm()
            return render(request, 'userauth.html', {'user_form': user_form,'name':name,'data':data})

    else:
        user_form = UserForm()
    return render(request,'userauth.html',{'user_form':user_form})

def set_session(request):
    request.session['name'] = 'ajay'
    return render(request,'setsession.html') 

def get_session(request):
    if 'name' in request.session:
        request.session.modified = True
        name = request.session['name']
        
        return render(request,'getsession.html',{'name':name})
    else:
        return HttpResponse('your page session is expired')