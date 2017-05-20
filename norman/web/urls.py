from norman.web.frontend.auth_login import AuthLoginView
from norman.web.frontend.home import HomeView

from django.conf.urls import url

__all__ = ('urlpatterns')

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='norman-home'),
    url(r'^auth/login/$', AuthLoginView.as_view(),
        name='norman-login'),
]