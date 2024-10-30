from django import forms
from .models import videos,inventory

class VideoForm(forms.ModelForm):
    class Meta:
        model = videos
        fields = ['username','vidname', 'link']  # Specify the fields you want to edit

class UpdateForm(forms.ModelForm):
    class Meta:
        model = videos
        fields = ['vidname', 'link']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        fields = ['username','item', 'quan','units']