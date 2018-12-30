from django import forms

class SearchForm(forms.Form):
    search_album = forms.CharField(max_length=50,widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Album Name'}),label="")
    search_artist = forms.CharField(max_length=50,widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Artist Name'}),label="")
