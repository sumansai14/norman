from norman.web.frontend.base import BaseAuthTemplateView


class OrganizationInventoryView(BaseAuthTemplateView):
    """Inventory View."""
    template_name = "norman/organization/inventory.html"