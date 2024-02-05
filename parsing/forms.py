from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (('kivano.kg', 'kivano.kg'),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'kivano.kg':
            noutbook_parser = parser.parser()
            for i in noutbook_parser:
                models.KivanoNouts.objects.create(**i)


