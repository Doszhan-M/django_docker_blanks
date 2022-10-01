
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import SessionAuthentication

from .exceptions import ProvideError, CredentialsError


class SessionLogin(APIView):
    ''' Session based login
    '''
    def get(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        email = 'admin@admin.kz'
        password = 'scENoUsemArl'
        if email is None or password is None:
            raise ProvideError
        user = authenticate(email=email, password=password)
        if user is None:
            raise CredentialsError
        login(request, user)
        return Response({'detail': f'logged in as {user}'})
    
    
class SessionLogout(APIView):
    ''' Session based login
    '''
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Successfully logged out.'})


class SessionCheck(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(f'isAuthenticated {request.user}')


class GetCsrf(APIView):
    
    def get(self, request):
        return Response({'X-CSRFToken' : get_token(request)})
    