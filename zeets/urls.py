from django.conf.urls import url 


from . import views 

urlpatterns = [
				url(r'^post/$', views.post_zeet, name = 'post'),
				url(r'^feed/$', views.feed, name = 'feed'),
				url(r'^zeet/$', views.all_zeets, name = 'home'),
				url(r'^edit-zeet/(?P<zeet_id>[0-9]+)/$', views.edit_zeet, name = 'edit_zeet'),
				url(r'^delete/(?P<zeet_id>[0-9]+)/$', views.delete_zeet, name = 'delete'),
				url(r'^comments/(?P<zeet_id>[0-9]+)/$', views.comment, name = 'comment'),
				url(r'^delete-comment/(?P<comment_id>[0-9]+)/$', views.delete_comment, name = 'delete_comment'),
				url(r'^add_like/(?P<zeet_id>[0-9]+)/$', views.add_like, name = 'add_like'),
				url(r'^remove_like/(?P<zeet_id>[0-9]+)/$', views.remove_like, name = 'remove_like'),
				]