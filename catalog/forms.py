from django import forms
from catalog.models import Book, Author,Genre


'''class CustomForms(forms.Form):
    username=forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=
        {'placeholder':'Your Username','class':'form-control'}))


    email=forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs=
        {'placeholder':'ac@gmail.com','class':'form-control'}))

    password=forms.CharField(
        label='Your Password',
        widget=forms.TextInput(attrs=
        {'placeholder':'','class':'form-control'}))

    confirm_password=forms.CharField(
        label='Password Again',
        widget=forms.TextInput(attrs=
        {'placeholder':'','class':'form-control'}))'''
class BookForms(forms.Form):
        title=forms.ModelChoiceField(
            queryset=Book.objects.all(),
            empty_label='Title',widget=forms.Select(attrs={'name':'book','id':'book',
            'class':'custom-select'})
        )

        author=forms.ModelChoiceField(
            queryset=Author.objects.all(),
            empty_label='Title',widget=forms.Select(attrs={'name':'author','id':'author',
            'class':'custom-select'})
        )

        purchase_date=forms.DateField(label='',widget=forms.DateInput(
           attrs={'placeholder':'Purchase_Date','name':'date','id':'date','class':'form-control'})
        )

        genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)