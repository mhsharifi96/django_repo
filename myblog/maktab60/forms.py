from django import forms
from post.models import Tag,Post,Category,Comment
from django.contrib.auth.models import User

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

class CommentModelForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(SampleClass, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs['class'] = 'my_class'

    class Meta : 
        model = Comment
        fields = ['title','desc']
        labels ={
            'title': 'عنوان',
            'desc' : 'توضیحات'
        }
        error_messages = {
            'title': {
                'max_length': "This writer's name is too long.",
                'required': "حتما وارد کنید",
            },
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255,min_length=5,label="نام کاربری" )
    password =  forms.CharField(widget=forms.PasswordInput)



class UserRegisterFormModel(forms.ModelForm):


    class Meta :
        model = User
        fields = ['username','email','password']

from django.core.exceptions import ValidationError

class SetNewPasswordForm(forms.Form):
    password =  forms.CharField(widget=forms.PasswordInput)
    password1 =  forms.CharField(widget=forms.PasswordInput)
    password2 =  forms.CharField(widget=forms.PasswordInput)

    # def clean_password2(self):
    #     password2 = self.cleaned_data['password2']
    #     password1 = self.cleaned_data['password1']
    #     if password1 != password2:
    #         raise ValidationError("password1  == password2 ")

    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return password2
    
    def clean(self):    
        cleaned_data = super().clean()
        password1 =  cleaned_data.get("password1")
        password2 =  cleaned_data.get("password2")

        if password1 != password2:
                raise ValidationError(
                   "password1 and password2  not equal"
                )
        if password1 == '1234':
            raise ValidationError(
                   "password1  have not 1234"
                )

