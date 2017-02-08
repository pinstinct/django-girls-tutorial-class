from django import forms


# 폼을 자동으로 생성해줌
class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(
        widget=forms.Textarea
    )
