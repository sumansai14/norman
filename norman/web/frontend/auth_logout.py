from django.contrib.auth import logout, REDIRECT_FIELD_NAME
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseRedirect
from django.views.generic import View


class AuthLogoutView(View):
    auth_required = False

    def get(self, request, *args, **kwargs):
        next = request.GET.get(REDIRECT_FIELD_NAME, '')
        if not next:
            next = '/'
        logout(request)
        request.user = AnonymousUser()
        return HttpResponseRedirect(next)