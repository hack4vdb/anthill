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
apiRouter.register(r'activists', views.ActivistViewSet)
apiRouter.register(r'meetups', views.MeetupViewSet)
apiRouter.register(r'meetupsnearactivist', views.MeetupNearActivistViewSet)


urlpatterns = [
    url(r'^$', staticviews.home, name='home'),
    url(r'^events/$', staticviews.events, name='events'),
    url(r'^join_event/$', staticviews.join_event, name='join_event'),
    url(r'^join_first_event/$', staticviews.join_first_event, name='join_first_event'),
    url(r'^start_event/$', staticviews.start_event, name='start_event'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apiRouter.urls)),
    #url(r'^api/meetupsnearactivist/(?P<id>[\d\w-]+)/', views.meetups_near_activist, name='meetups_near_activist'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
