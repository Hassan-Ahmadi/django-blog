from django import forms
from .models import Contact, Newsletter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
    
    def clean_name(self):
        return "ناشناس"
    
class NewsletterForm(forms.ModelForm):
        
        class Meta:
            model = Newsletter
            fields = ['email']