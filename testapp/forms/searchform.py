from django import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Поиск по автору или названию',
            'class': 'form-control',
            'name': 'q'  # явно указываем name
        })
    )