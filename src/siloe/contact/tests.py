from django.test import TestCase
from django.utils.html import escape

from contact.forms import ContactForm, EMPTY_EMAIL_ERROR, EMPTY_MESSAGE_ERROR
from contact.views import SUCCESS_SENDING_MSG


class ContactFormTest(TestCase):
    def test_form_has_all_fields(self):
        form = ContactForm()
        self.assertIn('Email', form.as_p())
        self.assertIn('placeholder="Váš email"', form.as_p())
        self.assertIn('Správa', form.as_p())
        self.assertIn('placeholder="Vaša správa"', form.as_p())

    def test_email_can_not_be_blank(self):
        form = ContactForm(data={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['email'],
            [EMPTY_EMAIL_ERROR]
        )

    def test_message_can_not_be_blank(self):
        form = ContactForm(data={'message': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['message'],
            [EMPTY_MESSAGE_ERROR]
        )


class ContactViewTest(TestCase):
    def test_contact_view_uses_contact_form(self):
        response = self.client.get('/contact/')
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_validation_errors_are_sent_back(self):
        response = self.client.post('/contact/', data={'email': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(EMPTY_EMAIL_ERROR))
        self.assertIsInstance(response.context['form'], ContactForm)

    def test_confirmation_is_shown_after_success_sending(self):
        response = self.client.post('/contact/', data={'email': 'a@a.sk', 'message': 'sprava'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, escape(SUCCESS_SENDING_MSG))
