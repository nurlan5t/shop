from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView

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
