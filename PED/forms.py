from django import forms

sprint_choices = [
    ('17.12', '17.12'),
    ('18.2', '18.2'),
     ]


class srint_select_form(forms.Form):
    select_Sprint = forms.ChoiceField(choices=sprint_choices, label='')
     
