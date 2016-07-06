import requests
from django.shortcuts import render


# Create your views here.
from contact.forms import ContactForm
from siloe.settings import CONTACT_EMAIL, MAILGUN_API_KEY

SUCCESS_SENDING_MSG = 'Správa bola úspešne odoslaná'
ERROR_SENDING_MSG = 'Správu sa nepodarilo odoslať. Skúste to prosím znovu alebo priamo na {}.'.format(CONTACT_EMAIL)


def view_contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            if send_email(request.POST):
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


def send_email(data):
    response = requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": "Excited User <excited@samples.mailgun.org>",
              "to": ["devs@mailgun.net"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomeness!"})
    return False
