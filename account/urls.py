from django.conf.urls import url 
from django.contrib.auth import views as auth_views


from . import views 

urlpatterns = [
				url(r'^login/$', auth_views.login, name = 'login'),
				url(r'^logout/$', auth_views.logout, name = 'logout'),
				url(r'^logout-then-login/$', auth_views.logout_then_login, name = 'logout_then_login'),
				#url(r'^password-change/$', auth_views.PasswordChangeView.as_view(), name = 'password_change'),
				#url(r'^password-change/done/$', auth_views.PasswordChangeDoneView.as_view(), name = 'password_change_done'),
				url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
				url(r'^edit/$', views.edit, name = 'edit'),
				url(r'^list/$', views.users_list, name = 'users_list'),
				url(r'^register/$', views.register, name = 'register'),
				url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name = 'user_detail'),
				]
