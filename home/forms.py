from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
