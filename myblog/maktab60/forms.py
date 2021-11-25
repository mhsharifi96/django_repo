from django import forms
from post.models import Tag


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=255,min_length=5,label="نام" ,help_text="توضیح اضافه")
    name_maktab = forms.IntegerField(label="دوره")
    # phone = forms.IntegerField()
    # text = forms.CharField(label="نظرات",widget=forms.Textarea)
    # password =  forms.CharField(widget=forms.PasswordInput)
    # choice = forms.ChoiceField(label="الکی",choices=((1,'one'),(2,'two')))
    # tags = forms.ModelChoiceField(label=" model choice",queryset=Tag.objects.all()) #to_field_name = "title" --> chose value of select
    


class TagForm (forms.Form):
    title = forms.CharField(max_length=255,min_length=3,label="تگ" ,)
