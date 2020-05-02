from django import forms


class Search(forms.Form):
    """Search definition."""
    searchword = forms.CharField(label='Movie',widget=forms.TextInput(attrs={'class':'forms-control'}))