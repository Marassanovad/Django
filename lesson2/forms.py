from django import forms
class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    address = forms.CharField(max_length=20)
    image = forms.ImageField()


class ProductForm(forms.Form):
    id = forms.IntegerField(min_value=1,required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите ID'}))
    name = forms.CharField(max_length=10,required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    description = forms.CharField(max_length=50,required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите Price'}))
    count = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите Count'}))
    image = forms.ImageField(required=False)
