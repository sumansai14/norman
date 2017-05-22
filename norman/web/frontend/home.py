from norman.web.frontend.base import BaseAuthTemplateView


class HomeView(BaseAuthTemplateView):
    template_name = 'norman/home.html'
