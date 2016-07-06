from django import forms

EMPTY_EMAIL_ERROR = 'Musíte zadať vašu emailovú adresu'
EMPTY_MESSAGE_ERROR = 'Musíte zadať text správy'


class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Váš email',
            'class': 'form-control',
        }),
        error_messages={
            'required': EMPTY_EMAIL_ERROR,
        },
    )
    message = forms.CharField(
        label='Správa',
        help_text='Radi vám odpovieme na všetky otázky',
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Vaša správa',
            'class': 'form-control',
        }),
        error_messages={
            'required': EMPTY_MESSAGE_ERROR,
        },
    )
