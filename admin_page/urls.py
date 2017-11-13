from django.conf.urls import url

from . import views as user_views

urlpatterns = [
    url(r'view_news', user_views.view_news),
    url(r'view_user', user_views.view_user),
    url(r'view_employee', user_views.view_employee),
    url(r'view_zone', user_views.view_zone),
    url(r'view_division',user_views.view_division),
    url(r'view_news', user_views.view_news),
    url(r'view_user', user_views.view_user),
    url(r'update_employee', user_views.view_employee),
    url(r'update_zone', user_views.view_zone),
    url(r'update_division',user_views.view_division),
    url(r'delete_employee', user_views.view_employee),
    url(r'delete_news', user_views.view_news),
    url(r'employee', user_views.view_employee),
    url(r'zone', user_views.view_zone),
    url(r'division',user_views.view_division),
    url(r'complaint',user_views.view_complaint),
    url(r'feedback',user_views.view_feedback),
]
