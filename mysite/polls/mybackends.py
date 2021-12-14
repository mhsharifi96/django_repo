# from .models import CustomUser

from django.contrib.auth import get_user_model

from django.contrib.auth.backends import BaseBackend
User = get_user_model()
print(User)
class EmailModelBackend(BaseBackend):
    print('here')
    def authenticate(self,request, username=None, password=None, **kwargs):
        
        print(username)
        if '@' in username:
            kwargs = {'email': username}
        else:
             kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            
            if user.check_password(password) is True:
                return user
        except User.DoesNotExist:
            pass

    def get_user(self,user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None