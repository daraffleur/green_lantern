from django import forms

from .models import Article


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticleImageForm(forms.Form):
    image = forms.ImageField(required=True)


# creating a form
class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article

        # specify fields to be used
        fields = [
            "title",
            "body"]
