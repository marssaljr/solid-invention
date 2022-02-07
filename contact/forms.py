from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label=False, 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name', 
                'class': 'inputField',
            }))
    email = forms.EmailField(
        label=False, 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'inputField',
            }))
    message = forms.CharField(
        label=False, 
        widget=forms.Textarea(
            attrs={
                'placeholder': 'I want you on my team!',
                'class': 'textField',
            }), required=True)

