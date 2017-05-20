from django.http import HttpResponse
from django.conf import settings
from django.template import loader, RequestContext, Context


def get_default_context(request, existing_context=None):
    context = {}
    # get all the user variables.
    # serialize all the objects - Not really necessary but some datetime objects might be here
    # update context with all the required data here
    return context


def render_to_string(template, context=None, request=None):

    # HACK: set team session value for dashboard redirect
    default_context = get_default_context(request, context)

    if context is None:
        context = default_context
    else:
        context = dict(context)
        context.update(default_context)

    if request:
        context = RequestContext(request, context)
    else:
        context = Context(context)

    return loader.render_to_string(template, context)


def render_to_response(template, context=None, request=None, status=200,
                       content_type='text/html'):
    response = HttpResponse(render_to_string(template, context, request))
    response.status_code = status
    response['Content-Type'] = content_type
    return response