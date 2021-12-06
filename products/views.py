from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Category, Product
from .forms import ProductModelForm
from django.http import HttpResponseRedirect, HttpResponse
def product_all(request):
    products = Product.objects.all()
    categories= Category.objects.all()
    paginator = Paginator(products, 10) 
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, "products/product_all.html", {"products": products, 'categories' : categories})


    
def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True))    
    page = request.GET.get('page')
    paginator = Paginator(products, 1) 
    products = paginator.get_page(page)
    return render(request, "products/category.html", {"category": category, "products": products})
    
    
    
    
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "products/product-detail.html", {"product": product})    
    
    
    
def add_product(request,  *args, **kwargs):  # Add product from browser
    added_message=None
    categories= Category.objects.all()
    if request.method=="POST":
        form = ProductModelForm(request.POST, request.FILES )
            
        if form.is_valid():
            form = form.save()
                
            added_message = "The product has been added"
      
    form = ProductModelForm()
     
    context = {'form': form,
            'added_message':added_message,
                'categories' : categories,
            }
     
    return render(request, 'products/add_product.html', context)         
    
    
def categories(request): 
    categories= Category.objects.all()
    context = {'categories' : categories}
    return render(request , 'products/categories_list.html' , context)    
    
    

    
    

def product_search(request, sort_by="", search="empty"):
    if request.POST:
        search = request.POST['search_by']
        prod_name= dict()
        product= dict()
    
        if search:
            if search.isnumeric(): # The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
                """If user look for product code we load the details view"""
                print("got in id")
                product = Product.objects.get(product_code=search)
               

                print ('details=', product)
                return render(request, "products/product-detail.html", {'product':product})
                
            else:
                """Function looks for products based on name and filter it """
                if sort_by == "":
                    prod_name = Product.objects.filter(name__istartswith=search)
                   
                else:
                    prod_name = Product.objects.filter(name__istartswith=search).order_by(sort_by)
               
        else:
            search="empty"#search value can not be blank
            prod_name = Product.objects.all()#If search field is blank show all
         
        
        return render(request, "products/products_search.html", {'prod_name':prod_name, "search":search })

    if search == "empty" and sort_by == "":
        prod_name = Product.objects.all()
    elif search == "empty" and sort_by != "":
        prod_name = Product.objects.all().order_by(sort_by)
    elif search != "empty" and sort_by == "":
        prod_name = Product.objects.filter(name__istartswith=search)
    elif search != "empty" and sort_by != "":
        prod_name = Product.objects.filter(name__istartswith=search).order_by(sort_by)
    
    

    return render(request, "products/products_search.html",{'prod_name':prod_name, "sort_by":sort_by, "search":search})
        
        
