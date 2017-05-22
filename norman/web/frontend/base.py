from __future__ import absolute_import


from django.views.generic.base import TemplateView
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_protect
# from norman.web.helpers import render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin

import logging

logger = logging.getLogger(__name__)


class BaseAuthTemplateView(LoginRequiredMixin, TemplateView):
    """
    All templateviews which require login will extend from the BaseTemplateView.

    so that we can add context about what page we are in and other dynamic details like that
    """

    def get_context_data(self, **kwargs):
        context = super(BaseAuthTemplateView, self).get_context_data(**kwargs)
        categories = ['farmer', 'crops', 'inventory', 'orders']
        for category in categories:
            if category in self.request.path:
                context['category'] = category
                break
        return context


# class BaseView(View):
#     auth_required = True

#     @method_decorator(csrf_protect)
#     def dispatch(self, request, *args, **kwargs):
#         if self.is_auth_required(request, *args, **kwargs):
#             pass  # Do something here
#         self.default_context = self.get_context_data(request, *args, **kwargs)
#         return self.handle(request, *args, **kwargs)

#     def get_context_data(self, request, **kwargs):
#         context = csrf(request)
#         return context

#     def is_auth_required(self, request, *args, **kwargs):
#         return (
#             self.auth_required
#             and not (request.user.is_authenticated() and request.user.is_active)
#         )

#     def respond(self, template, context=None, status=200):
#         default_context = self.default_context
#         if context:
#             default_context.update(context)
#         return render_to_response(template, default_context, self.request,
#                                   status=status)