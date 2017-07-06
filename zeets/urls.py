from django.conf.urls import url 


from . import views 

urlpatterns = [
				url(r'^post/$', views.post_zeet, name = 'post'),
				url(r'^zeet/$', views.all_zeets, name = 'home'),
				url(r'^edit-zeet/(?P<zeet_id>[0-9]+)/$', views.edit_zeet, name = 'edit_zeet'),
				url(r'^delete/(?P<zeet_id>[0-9]+)/$', views.delete_zeet, name = 'delete'),
				]