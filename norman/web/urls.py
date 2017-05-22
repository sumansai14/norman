from norman.web.frontend.auth_login import AuthLoginView
from norman.web.frontend.auth_logout import AuthLogoutView
from norman.web.frontend.home import HomeView
from norman.web.frontend.farmer import OrganizationFarmerListView, OrganizationFarmerAddView
from norman.web.frontend.crops import OrganizationCropsListView
from norman.web.frontend.inventory import OrganizationInventoryView
from norman.web.frontend.orders import OrganizationOrdersView

from django.conf.urls import url

__all__ = ('urlpatterns')

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='norman-home'),
    url(r'^auth/login/$', AuthLoginView.as_view(),
        name='norman-login'),
    url(r'^auth/logout/$', AuthLogoutView.as_view(),
        name='norman-logout'),
    url(r'^farmers/$', OrganizationFarmerListView.as_view(), name='organization-farmer-list'),
    url(r'^farmers/add/$', OrganizationFarmerAddView.as_view(), name='organization-farmer-add'),
    url(r'^crops/$', OrganizationCropsListView.as_view(), name='organization-crops-list'),
    url(r'^inventory/$', OrganizationInventoryView.as_view(), name='organization-inventory'),
    url(r'^orders/$', OrganizationOrdersView.as_view(), name='organization-orders'),
]