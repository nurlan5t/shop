import datetime
import random
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User, Code
from django.core.mail import send_mail
from users.serializers import UserSerializer



class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return Response(data={'error':'Неправильный логин или пароль'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            token = None
            try:
                token = Token.objects.get(user=user)
                print('GET TOKEN')
            except:
                pass
            if token is None:
                token = Token.objects.create(user=user)
                token.save()
                print('CREATE TOKEN')
        return Response(status=status.HTTP_200_OK, data={'key':token.key})

def get_code():
    return str(random.randint(100000,999999))

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        new_user = User.objects.create(username=username)
        new_user.set_password(raw_password=password)
        new_user.is_active=False
        new_user.save()
        code = get_code()
        confirmation_code = Code.objects.create(conf_code=code, valid_until=datetime.datetime.now()+
                                                                            datetime.timedelta(minutes=5),
                                                user=new_user)
        confirmation_code.save()
        send_mail(
            'Confirm code for register!',
            f'{code}',
            settings.EMAIL_HOST_USER,
            [f'{username}'],
            fail_silently=False,)
        return Response(status=status.HTTP_200_OK, data=UserSerializer(new_user).data)

class ConfirmAPIView(APIView):
    def post(self, request):
        code =  request.data.get('code')
        confirmations = Code.objects.filter(conf_code=code, valid_until__gte=datetime.datetime.now())
        if not confirmations:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Невалидный код'})
        else:
            user = confirmations[0].user
            user.is_active = True
            user.save()
            confirmations.delete()
            return Response(status=status.HTTP_200_OK)
