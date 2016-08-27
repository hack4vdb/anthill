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
from anthill import api_views
from anthill import views

# from mailviews.previews import autodiscover, site

apiRouter = routers.DefaultRouter()
# apiRouter.register(r'users', api_views.UserViewSet)
# apiRouter.register(r'groups', api_views.GroupViewSet)
apiRouter.register(r'activists', api_views.ActivistViewSet, base_name='activists')
apiRouter.register(r'meetups', api_views.MeetupViewSet, base_name='meetups')
apiRouter.register(
    r'meetupsnearactivist',
    api_views.MeetupNearActivistViewSet,
    base_name='meetupsnearactivist')

# for mailviews preview:
# autodiscover()

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^login/$', views.login_by_email, name='login_by_email'),
    url(r'^login/(?P<login_token>[\d\w-]+)/$', views.login_with_token, name='login_with_token'),
    url(r'^unsubscribe/(?P<uuid>[\d\w-]+)/$', views.unsubscribe, name='unsubscribe'),
    url(r'^join_meetup_from_email/(?P<login_token>[\d\w-]+)/$', views.join_meetup_from_email,
        name='join_meetup_from_email'),
    url(r'^check_mail/$', views.check_mail, name='check_mail'),
    url(r'^meetups/$', views.meetups, name='meetups'),
    url(r'^howto/?$', views.instructions, name='instructions'),
    url(r'^about/?$', views.about, name='about'),
    url(r'^invite/(?P<meetup_id>.+)/?$', views.invite, name='invite'),
    url(r'^thankyou/(?P<meetup_id>.+)/?$', views.thankyou, name='thankyou'),
    url(r'^join_meetup/$', views.join_meetup, name='join_meetup'),
    url(r'^join_meetup_fb_messenger/(?P<signeddata>[\d\w\.-]+)/', views.join_meetup_fb_messenger,
        name='join_meetup_fb_messenger'),
    url(r'^invite/$', views.invite, name='invite'),
    url(r'^i/(?P<invite_code>.+)/$', views.short_invite, name='short_invite'),
    url(r'^join_first_event/$', views.join_first_event, name='join_first_event'),
    url(r'^start_event/$', views.start_event, name='start_event'),
    url(r'^logout/$', views.logout_view, name='logout_view'),

    url(r'^admin/', admin.site.urls),

    #  unused api endpoints are hidden.
    # url(r'^api/', include(apiRouter.urls)),
    # url(r'^api/meetups/(?P<meetupid>[\d\w-]+)/partake/(?P<userid>[\d\w-]+)/', api_views.partake_meetup, name='partake_meetup'),
    url(r'^api/meetupsbylatlng/(?P<latlong>.+)/', api_views.meetupsByLatLng, name='meetupsbylatlng'),
    # url(r'^api/interestingplaces/(?P<id>[\d\w-]+)/', api_views.interesting_places, name='interesting_places'),
    # url(r'^api/potentialmeetups/(?P<user_bot_id>[\d\w-]+)/', api_views.potential_meetups, name='potential_meetups'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/staticmaps/(?P<city>[\d\w-]+)/(?P<street>[\d\w\W-]*)/', api_views.static_maps, name='static_maps')

    # url(regex=r'^emails/', view=site.urls),
]
