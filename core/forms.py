from django import forms


class ParagraphForm(forms.Form):
    paragraph = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 12,
                'class': 'form-control',
                'placeholder': 'Enter paragraph here',
                'id': 'paragraph-text'
            }
        )
    )

    class Meta:
        fields = ['paragraph', ]