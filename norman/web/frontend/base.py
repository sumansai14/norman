from __future__ import absolute_import

from django.core.context_processors import csrf
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from norman.web.helpers import render_to_response

import logging

logger = logging.getLogger(__name__)


class BaseView(View):
    auth_required = True

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if self.is_auth_required(request, *args, **kwargs):
            pass  # Do something here
        self.default_context = self.get_context_data(request, *args, **kwargs)
        return self.handle(request, *args, **kwargs)

    def get_context_data(self, request, **kwargs):
        context = csrf(request)
        return context

    def is_auth_required(self, request, *args, **kwargs):
        return (
            self.auth_required
            and not (request.user.is_authenticated() and request.user.is_active)
        )

    def respond(self, template, context=None, status=200):
        default_context = self.default_context
        if context:
            default_context.update(context)
        return render_to_response(template, default_context, self.request,
                                  status=status)