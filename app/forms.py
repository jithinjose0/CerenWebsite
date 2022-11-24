from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=1000)