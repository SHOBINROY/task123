# from django import forms
# from django.forms import ModelForm
# from .models import details
#
# class DetailForm(forms.ModelForm):
#      class Meta:
#          model=details
#          fields ='__all__'


from django import forms
from .models import Form

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]
MATERIAL_CHOICES = [
    ('PEN', 'PEN'),
    ('BOOKS', 'BOOKS'),
    ('BAG', 'BAG'),
    ('BOTTLE', 'BOTTLE'),
    ('BOX', 'BOX'),

]


class OrderForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)

    materials = forms.MultipleChoiceField(
        label='materials',
        choices=MATERIAL_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Form
        # Specify the fields to include in the form
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'age': 'Age',
            'phone_number': 'Mobile No.',
            'mail_': 'Email ID',
            'address': 'Address',

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control',
                                          'id': 'datepicker'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'courses': forms.Select(attrs={'class': 'form-control'}),
            'purpose': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'phone_mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
