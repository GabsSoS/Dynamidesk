from django import forms

class login_cliente(forms.Form):
    email = forms.CharField(max_length=100,required= True,
        widget=forms.TextInput(attrs={'class': 'login-email', 'placeholder': 'Digite seu email'})
    )
    password = forms.CharField(max_length=100,required= True,
        widget=forms.PasswordInput(attrs={'class': 'login-senha', 'placeholder': 'Digite sua senha'})
    )
