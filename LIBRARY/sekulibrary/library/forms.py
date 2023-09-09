from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class BookSearchForm(forms.Form):
    bookFields = [
        ("title", "title"),
        ("isbn", "isbn"),
        ("author", "author"),
        ("publisher", "publisher")
    ]
    search = forms.CharField(max_length=20)
    search_by = forms.ChoiceField(choices=bookFields)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
