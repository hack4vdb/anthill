"""hack4vdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin

from anthill import views
from anthill import staticviews

apiRouter = routers.DefaultRouter()
#apiRouter.register(r'users', views.UserViewSet)
#apiRouter.register(r'groups', views.GroupViewSet)
apiRouter.register(r'activists', views.ActivistViewSet, base_name='activists')
apiRouter.register(r'meetups', views.MeetupViewSet, base_name='meetups')
apiRouter.register(
    r'meetupsnearactivist',
    views.MeetupNearActivistViewSet,
    base_name='meetupsnearactivist')


urlpatterns = [
    url(r'^$', staticviews.home, name='home'),
    url(r'^registerfailed/$', staticviews.register_failed, name='register_failed'),
    url(r'^login/(?P<userid>[\d\w-]+)/$', staticviews.login_with_uuid, name='login_with_uuid'),
    url(r'^check_mail/$', staticviews.check_mail, name='check_mail'),
    url(r'^meetups/$', staticviews.meetups, name='meetups'),
    url(r'^join_meetup/$', staticviews.join_meetup, name='join_meetup'),
    url(r'^join_meetup/(?P<meetupid>[\d\w-]+)/(?P<signeddata>[\d\w\.-]+)/', staticviews.join_meetup_bot, name='join_meetup_bot'),
    url(r'^invite/$', staticviews.invite, name='invite'),
    url(r'^join_first_event/$', staticviews.join_first_event, name='join_first_event'),
    url(r'^start_event/$', staticviews.start_event, name='start_event'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apiRouter.urls)),
    url(r'^api/meetups/(?P<meetupid>[\d\w-]+)/partake/(?P<userid>[\d\w-]+)/', views.partake_meetup, name='partake_meetup'),
    url(r'^api/meetupsbylatlng/(?P<latlong>.+)/', views.meetupsByLatLng, name='meetupsbylatlng'),
    url(r'^api/interestingplaces/(?P<id>[\d\w-]+)/', views.interesting_places, name='interesting_places'),
    url(r'^api/potentialmeetups/(?P<user_bot_id>[\d\w-]+)/', views.potential_meetups, name='potential_meetups'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
