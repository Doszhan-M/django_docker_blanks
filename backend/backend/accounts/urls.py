from django.urls import path

from .views import (
    SessionLogin, SessionCheck, SessionLogout, GetCsrf
)


urlpatterns = [
    path("session_login/", SessionLogin.as_view(), name="session_login"),
    path("session_logout/", SessionLogout.as_view(), name="session_logout"),
    path("check_session/", SessionCheck.as_view(), name="check_session"),
    path("get_csrf/", GetCsrf.as_view(), name="get_csrf"),
]