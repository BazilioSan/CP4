from django.forms import ModelForm

from newsletter.models import Recipient, Message

# Define a form for creating new recipients.
class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

