from django import forms


class Search(forms.Form):
    """Search definition."""
    searchword = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Movie Title .....'}))