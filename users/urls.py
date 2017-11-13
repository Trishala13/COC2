from django.conf.urls import url

from . import views as user_views

urlpatterns = [
    url(r'user_site', user_views.user_site),
    url(r'sign-in', user_views.sign_in),
    url(r'sign-up', user_views.sign_up),
    url(r'sign_up_form',user_views.sign_up_form),
    url(r'sign_in_form',user_views.sign_in_form),
    url(r'complaint_form',user_views.complaint_form),
    url(r'complaint',user_views.complaint),
    url(r'zone_fill', user_views.zone_fill),
    url(r'zone', user_views.zone),
    url(r'resubmit',user_views.resubmit),
    url(r'feedback_form',user_views.feedback_form),
    url(r'update_fill',user_views.update_fill),
    url(r'update',user_views.update),
    url(r'division_fill',user_views.division_fill),
    url(r'division', user_views.division),
    url(r'official_login_fill', user_views.official_login_form),
    url(r'official-login', user_views.official_login),
    url(r'employee_site', user_views.emp_site),
    url(r'garbage_fill',user_views.garbage_fill),
    url(r'garbage_form_fill',user_views.garbage_entries),
    url(r'garbage_form',user_views.garbage_form),
    url(r'garbage', user_views.garbage),
    url(r'reset_passwrd',user_views.reset_passwrd),
    url(r'feedback',user_views.feedback),
    url(r'signout',user_views.signout),
]
