from django import forms
from post.models import Tag,Post,Category


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=255,min_length=5,label="نام" ,help_text="توضیح اضافه")
    name_maktab = forms.IntegerField(label="دوره")
    # phone = forms.IntegerField()
    # text = forms.CharField(label="نظرات",widget=forms.Textarea)
    # password =  forms.CharField(widget=forms.PasswordInput)
    # choice = forms.ChoiceField(label="الکی",choices=((1,'one'),(2,'two')))
    # tags = forms.ModelChoiceField(label=" model choice",queryset=Tag.objects.all()) #to_field_name = "title" --> chose value of select
    


class TagForm (forms.Form):
    title = forms.CharField(max_length=255,min_length=3,label="تگ",error_messages={'required':'وارد کردن تگ ضروری است'} )

    def save(self):
        print(self.cleaned_data)
        Tag.objects.create(title=self.cleaned_data['title'])


class TagModelForm(forms.ModelForm):

    class Meta : 
        model = Tag
        # fields = "__all__"
        fields = ['title']


class TagDeleteModelForm(forms.ModelForm):
    class Meta : 
        model = Tag
        fields = []


