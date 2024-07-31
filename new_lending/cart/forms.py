from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderInformation(forms.Form):
    name = forms.CharField(max_length=64, widget=forms.TextInput())
    surname = forms.CharField(max_length=64, widget=forms.TextInput())
    second_name = forms.CharField(max_length=64, widget=forms.TextInput())
    phone_number = forms.CharField(max_length=64, widget=forms.TextInput())
    order_place = forms.CharField(max_length=255,widget=forms.TextInput())