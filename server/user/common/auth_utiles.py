from user.models import User


def authenticate(email:str, password:str ) -> bool:
    user = User.objects.get(user_email=email)
    if user.user_password == password:
        return True
    else:
        return False