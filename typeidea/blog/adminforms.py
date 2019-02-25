from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', }, ),
        label='摘要',
        required=False
    )
