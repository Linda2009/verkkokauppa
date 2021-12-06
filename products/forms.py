from django import forms
from .models import  Product

# TYPE_CHOICES = (
# ('True', 'True'),
# ('False', 'False'),

# )
class ProductModelForm(forms.ModelForm):
    # in_stock  = forms.ChoiceField(choices=TYPE_CHOICES)
    # PRDISNew = forms.ChoiceField(choices=TYPE_CHOICES)
    # PRDISBestSeller = forms.ChoiceField(choices=TYPE_CHOICES)

        
        
    class Meta:
        model = Product
        fields = ['name','product_code', 'category', 'description' ,'discount_percent','regular_price',
        'discounted_price','cost',
         'prod_image',  ]
         

        
