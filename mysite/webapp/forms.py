from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Product, Account, ContactUs, Subscriber


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'price', 'description', 'amount', 'image', 'size']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'size': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
            'message': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


class AccountForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Gender',
                               choices=[('none', 'Not selected'), ('male', 'Male'), ('female', 'Female'), ],
                               widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    phoneNumber = forms.CharField(label='Phone number', required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('full_name', 'gender', 'email', 'phoneNumber', 'is_superuser' , 'password')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'is_superuser': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AccountCreationForm(UserCreationForm):
    gender = forms.ChoiceField(label='Gender', choices=[('none', 'Not selected'), ('male', 'Male'), ('female', 'Female'),], widget=forms.Select(attrs={'class': 'form-select'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password conformation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Account
        fields = ('full_name', 'gender', 'email', 'phoneNumber', 'password1', 'password2')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AccountChangePassword(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ('password')

# class AccountChangeForm(UserChangeForm):
#     gender = forms.ChoiceField(label='Gender',
#                                choices=[('none', 'Not selected'), ('male', 'Male'), ('female', 'Female'), ],
#                                widget=forms.Select(attrs={'class': 'form-select'}), required=False)
#     phoneNumber = forms.CharField(label='Phone number', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = Account
#         fields = ('full_name', 'gender', 'email', 'phoneNumber', 'is_superuser')
#         widgets = {
#             'full_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#            #'is_superuser': forms.CheckboxInput(attrs={'class': 'form-control'}),
#         }