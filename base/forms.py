from django import forms
from .models import CreatorGoal


class DonateForm(forms.Form):
    CHOICES = [('5', '$5'), ('10', '$10') , ('40', '$40')]

    tip_amount = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect()
    )
    custom_tip = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder': "$100" , "value":""}))
    email = forms.EmailField(
        required=True,
        widget = forms.TextInput(attrs={'placeholder':"JohnDoe@gmail.com"})
    )

class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = CreatorGoal
        fields = ['item_link', 'item_name','channel_name', 'item_image', 'item_price']
        widgets = {
            'channel_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_link': forms.URLInput(attrs={'class': 'form-control'}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'item_image': forms.ClearableFileInput(attrs={'class': 'file-input'}),
            
        }
    