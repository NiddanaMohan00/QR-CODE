from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        label='Restaurant Name', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Restaurant Name', 'class': 'form-control'})
        )
    url=forms.URLField(label='Menu URL',
                       max_length=500,
                       widget=forms.URLInput(attrs={'placeholder':'Enter Menu URL','class':'form-control'})
                       )
    
