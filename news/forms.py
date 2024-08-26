from django import forms
from news.models import Contact

class ContactForm(forms.ModelForm):

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class' : "form-control", 'placeholder' : "Your Name"}
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class' : "form-control", 'placeholder' : "Your Email"}
        )
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'class' : "form-control", 'placeholder' : "Subject"}
        )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'class' : "form-control", 'rows' : "5", 'placeholder' : "Enter Message"}
        )
    )


    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'subject', 'message')