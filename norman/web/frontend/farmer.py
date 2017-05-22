from norman.web.frontend.base import BaseAuthTemplateView


class OrganizationFarmerListView(BaseAuthTemplateView):
    """Farmers list view."""

    template_name = 'norman/organization_farmer_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrganizationFarmerListView, self).get_context_data(**kwargs)
        context['farmers'] = []
        return context
