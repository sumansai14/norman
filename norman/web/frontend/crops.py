from norman.web.frontend.base import BaseAuthTemplateView


class OrganizationCropsListView(BaseAuthTemplateView):
	template_name = 'norman/organization/crops_list.html'
