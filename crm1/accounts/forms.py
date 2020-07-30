from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order   #creating a form from Order model in models.py,
        fields = '__all__'  #create a form with all the fields in Order model, eg customer,prodcut,status etc


