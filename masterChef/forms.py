from django import forms

class ReceipeForm(forms.Form):
    receipe_message = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':"Ask Your Receipe"}))