from django.views.generic.base import TemplateView
from norman.web.forms.accounts import AuthenticationForm


class AuthLoginView(TemplateView):
    template_name = 'norman/login.html'

    def get_context_data(self, **kwargs):
        context = super(AuthLoginView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            context['login_form'] = AuthenticationForm()
            return context
        elif self.request.method == 'POST':
            pass
