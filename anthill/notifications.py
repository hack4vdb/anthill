from anthill.emailviews import WelcomeMessageView
from anthill.emailviews import NewNearMeetupMessageView
from anthill.emailviews import LoginLinkMessageView
from anthill.models import EmailLoginJoinMeetupCode

from django.urls import reverse


class Notifications:
    """
    Has convenience methods to send the right notifications with the right
    parameters and at the intended cadence.

    Put anti-spam logic (e.g. checking in DB if user received that email in the
    last 7 days) and logic about selecting multiple recipients in here.
    """

    @staticmethod
    def send_login_link(request, recipient):
        """Generates a login_token and sends out the login email"""
        token = recipient.generate_login_token()
        LoginLinkMessageView(recipient=recipient).send(extra_context={
            'login_link': request.build_absolute_uri(reverse('login_with_token', kwargs={
                'login_token': token
            }))
        })

    @staticmethod
    def send_meetup_created_notifications(request, meetup):
        for activist in meetup.find_activists_nearby().all():
            #TODO despam
            join_login, created = EmailLoginJoinMeetupCode.objects.get_or_create(activist=activist, meetup=meetup)
            print('email for {} - {}'.format(activist.email, join_login.invite_code))
            NewNearMeetupMessageView(recipient=activist).send(extra_context={
                'meetup': meetup,
                'join_link': request.build_absolute_uri(reverse('join_meetup_from_email', kwargs={ #TODO: join_url
                    'login_token': join_login.invite_code
                }))
            })
