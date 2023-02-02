from django import forms
from.models import customer

class Customerform(forms.ModelForm):
    class Meta:
        model=customer
        fields=('cust_id','cust_name','cust_address','cust_phone')
        