from random import randint
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User, Code
from django.core.mail import send_mail
from users.serializers import UserSerializer

confirm_code = randint(100000,999999)

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

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        new_user = User.objects.create(username=username, password=password)
        new_user.is_active=False
        new_user.save()
        send_mail(
            'Confirm code for register!',
            f'{confirm_code}',
            'nur23kg@mail.ru',
            [f'{username}'],
            fail_silently=False,)
        # code = Code.objects.create(conf_code=confirm_code)
        # code.save()
        return Response(status=status.HTTP_200_OK, data=UserSerializer(new_user).data)

# class ActivateUser(APIView):
