from django import forms

__author__ = 'Eraldo Helal'


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # TODO: send email with message to eraldo
        # send email using the self.cleaned_data dictionary
        print(
        "should send email now to {} with message {}".format(self.cleaned_data["email"], self.cleaned_data["message"]))
        pass