from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                                widget=forms.TextInput(
                                       attrs={
                                       "calss": "form-control"
                               }
                           ))
    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(
                                      attrs={
                                      "calss": "form-control"
                               }
                           ))