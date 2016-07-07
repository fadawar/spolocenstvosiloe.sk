from smtplib import SMTPException

from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
from contact.forms import ContactForm
from siloe.settings import CONTACT_EMAIL

SUCCESS_SENDING_MSG = 'Správa bola úspešne odoslaná'
ERROR_SENDING_MSG = 'Správu sa nepodarilo odoslať. Skúste to prosím znovu alebo priamo na {}.'.format(CONTACT_EMAIL)


def view_contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            if send_confirm_email(form):
                response_data = {'form': ContactForm(), 'activated_menu_contact': 'active', 'sending': {
                    'status': True,
                    'message': SUCCESS_SENDING_MSG,
                }}
                return render(request, 'contact/contact.html', response_data)
            else:
                response_data = {'form': form, 'activated_menu_contact': 'active', 'sending': {
                    'status': False,
                    'message': ERROR_SENDING_MSG,
                }}
                return render(request, 'contact/contact.html', response_data)
        else:
            return render(request, 'contact/contact.html', {'form': form, 'activated_menu_contact': 'active'})
    else:
        return render(request, 'contact/contact.html', {'form': ContactForm(), 'activated_menu_contact': 'active'})


def send_confirm_email(form: ContactForm):
    try:
        send_mail('Správa zo spolocenstvosiloe.sk',
                  "Od: {}\n{}".format(form.cleaned_data['email'], form.cleaned_data['message']),
                  CONTACT_EMAIL,
                  [CONTACT_EMAIL],
                  fail_silently=False)
        return True
    except SMTPException:
        return False
