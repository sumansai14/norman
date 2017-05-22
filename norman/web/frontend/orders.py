from norman.web.frontend.base import BaseAuthTemplateView


class OrganizationOrdersView(BaseAuthTemplateView):
    """Inventory View."""
    template_name = "norman/organization/orders.html"