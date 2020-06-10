from django.urls import path, include
from django.conf import settings
from main_project.views import index, service, about, client, \
                             blog, single_blog, sign_in, logout_view



urlpatterns = [
		path('logout/', logout_view, name='sign_out'),
        path('', index, name='index'),
        path('service/', service, name='service'),
        path('about/', about, name='about'),
        path('client/', client, name='client'),
        path('blog/', blog, name='blog'),
        path('single_blog/<int:blog_id>', single_blog, name='single_blog'),
        path('sign_in/', sign_in, name='sign_in'),
]
