from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.safestring import mark_safe
from django.utils.text import slugify  
from .utils import generate_prod_code
class Category(MPTTModel):
 
    name = models.CharField( max_length= 300, db_index=True,verbose_name=_("Category Name"), )
    slug = models.SlugField(verbose_name=_("Category safe URL"),max_length= 300, unique=True,editable=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='children')   
    cat_image = models.ImageField(upload_to='products/images' , verbose_name=_("Image") , blank=True, null=True) 
    is_active = models.BooleanField(default=True)
    class MPTTMeta:
        order_insertion_by = ['name']
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")  
        
    def get_absolute_url(self):
        return reverse("products:category_list", args=[self.slug])
  
      
        # display image in admin panel
    def Cat_image_disp(self):

        if self.cat_image:
            return mark_safe(f'<img src="{self.cat_image.url}" height="50"/>')
        else:
            return ""
    
    #get unique slug
    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug

     #save slug
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name 
        


class Product(models.Model):
    """
    tuoteiden taulussa sisältä kaikki tuoteitä
    """
    product_code= models.CharField(max_length=10, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    name = models.CharField(help_text=_("Required"),max_length=255,verbose_name=_("Product Name "))
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(verbose_name=_("Product safe URL"),max_length= 300, unique=True,editable=False)
    discount_percent = models.DecimalField(verbose_name=_("discount percent%"),  max_digits=20 , decimal_places=2,  blank=True, default=0)
    regular_price = models.DecimalField(verbose_name=_("Regular price"), max_digits=20,decimal_places=2)
    discounted_price = models.DecimalField(verbose_name=_("Discount price"),max_digits=20,decimal_places=2,blank=True,null=True)
    cost = models.DecimalField(max_digits=20 , decimal_places=2 , verbose_name=_("Cost"),blank=True,null=True)
    prod_image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="products/images",
        default="products/images/default.png",
    )
    in_stock = models.BooleanField(default=True, verbose_name=_("Varastossa "))
  
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    PRDISNew = models.BooleanField(default=True , verbose_name=_("Uusi tuote "))
    PRDISBestSeller = models.BooleanField(default=False , verbose_name=_("Best Seller"))
   
   
       
    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("product")
        verbose_name_plural = _("products")
    
    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.slug])
    
    
    # ----------------------# display image in admin panel if i want CategoryAdminI-----------------------
    def Prod_image(self):
    
        if self.prod_image:
            return mark_safe(f'<img src="{self.prod_image.url}" height="50"/>')
        else:
            return ""
    
# -------------------------------------save slug and discount prices------------------------------------------------------------------
  
       
        

        
    #get unique slug
    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = "{}-{}".format(slug, counter)
            counter += 1
        return unique_slug
    
     #save slug
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        self.discounted_price= self.regular_price * (self.discount_percent /100)
        self.cost = self.regular_price - (self.discounted_price)
        if self.product_code == '':
            self.product_code = generate_prod_code()
        return super(Product, self).save(*args, **kwargs)
            
    def __str__(self):
        return self.name 
        
    