from rest_framework import status
from rest_framework.exceptions import APIException


class CustomApiException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__()
        self.detail = self.default_detail


class ProvideError(CustomApiException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        'detail': 'provide username and password',
        'error_code': 'provide_error'
    }
    
class CredentialsError(CustomApiException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {
        'detail': 'Invalid credentials',
        'error_code': 'credentials_error'
    }