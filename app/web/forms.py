from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(
        label='Titulo',
        required=True,
    )
    url = forms.URLField(
        label='Ruta',
        required=True,
    )
