from django import forms
from .models import  Tag,Category,Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SimpleForm(forms.Form):
    name = forms.CharField(max_length=255,label="نام",initial="maktab",)
    lastname = forms.CharField(max_length=255,label="نام خانوادگی ",help_text="نام خانوادگی منظور همون فامیلی است ",initial="sharif")
    birthday = forms.IntegerField(label="سال تولد ") #required=False,    error_messages={'invalid':"داداش فقط عدد"}
    choice = forms.ChoiceField(label="الکی",choices=((1,'one'),(2,'two')))
    description = forms.CharField(widget=forms.Textarea)
    tags = forms.ModelChoiceField(label=" model choice",queryset=Tag.objects.all()) #to_field_name = "title" --> chose value of select
    #refrence : https://docs.djangoproject.com/en/3.2/ref/forms/fields/#django.forms.ModelChoiceField

    def save(self):
        print('on save method : ',self.cleaned_data)
        # ....
        #refrence : https://stackoverflow.com/questions/11943912/how-do-you-write-a-save-method-for-forms-in-django
from django.utils.translation import gettext_lazy as _


class SimpleModelForm(forms.ModelForm):
   
    class Meta :
        model = Category
        fields = '__all__'
        labels = {
            # 'title':'نام دسته بندی',
            # 'parent':'دسته پدر'
            'title':_('TITLE')
        }
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }


# model form refrence : https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
        


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
        




class UserFormModel(forms.ModelForm):
    class Meta : 
        model = User
        fields = ['username','email','password']



class NewPasswordForm(forms.Form):
    
    password = forms.CharField(widget=forms.PasswordInput)
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password_1 =  cleaned_data.get("password_1")
        password_2 =  cleaned_data.get("password_2")

        if password_1 != password_2:
                raise ValidationError(
                   "password1 and password2  not equal"
                )
        if password_1 == '1234':
            raise ValidationError(
                   "password1  have not 1234"
                )
    # def clean_password_2(self):
    #     print(self.cleaned_data)
    #     password_1 = self.cleaned_data['password_1']
    #     password_2= self.cleaned_data['password_2']
    #     if password_1 != password_2:
    #         raise ValidationError(
    #             "پسورد اول با پسورد دوم باید برابر باشد"
    #         )

    # refrence : https://docs.djangoproject.com/en/3.2/ref/forms/validation/#cleaning-a-specific-field-attribute