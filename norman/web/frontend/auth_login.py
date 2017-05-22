from __future__ import absolute_import

from django.views.generic.base import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect


from norman.utils import auth
from norman.web.forms.accounts import AuthenticationForm


class AuthLoginView(TemplateView):
    template_name = 'norman/login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        return self.get_context_data(self, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super(AuthLoginView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            self.request.session.set_test_cookie()
            context['login_form'] = AuthenticationForm(self.request)
            return context
        elif self.request.method == 'POST':
            login_form = AuthenticationForm(self.request, self.request.POST or None)
            if not login_form.is_valid():
                context['login_form'] = login_form
                return super(TemplateView, self).render_to_response(context)
            user = login_form.get_user()
            auth.login(self.request, user)
            return HttpResponseRedirect(reverse('norman-home'))

