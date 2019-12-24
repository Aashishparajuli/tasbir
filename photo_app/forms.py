from django import forms
from .models import postmodel
class AddNewPostForm(forms.ModelForm):
    location = forms.CharField(
            widget = forms.TextInput(
                attrs={
                    'class': "edit-profile__input"
                }
            )
    )

    class Meta:
        model = postmodel
        fields = {
            'location',
            'photo',
        }