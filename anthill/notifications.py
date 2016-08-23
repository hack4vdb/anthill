from anthill.emailviews import WelcomeMessageView
from anthill.emailviews import NewNearMeetupMessageView
from anthill.emailviews import LoginLinkMessageView
from anthill.emailviews import MeetupBecameViableParticipantMessageView
from anthill.emailviews import MeetupBecameViableOwnerMessageView
from anthill.emailviews import WelcomeToViableMeetupMessageView
import anthill.models
from anthill.utils import make_absolute_url, concat_list_verbosely

from django.urls import reverse


class Notifications:
    """
    Has convenience methods to send the right notifications with the right
    parameters and at the intended cadence.

    Put anti-spam logic (e.g. checking in DB if user received that email in the
    last 7 days) and logic about selecting multiple recipients in here.
    """

    @staticmethod
    def send_login_link(request, recipient, invited_to_id=None):
        """Generates a login_token and sends out the login email"""
        token = recipient.generate_login_token()
        login_link = request.build_absolute_uri(reverse('login_with_token', kwargs={
                'login_token': token
            }))
        if invited_to_id:
            login_link += '?invited_to={}'.format(invited_to_id)
        LoginLinkMessageView(recipient=recipient).send(extra_context={
            'login_link': login_link
        })

    @staticmethod
    def send_meetup_created_notifications(request, meetup):
        for activist in meetup.find_activists_nearby().all():
            #TODO despam
            join_login, created = anthill.models.EmailLoginJoinMeetupCode.objects.get_or_create(activist=activist, meetup=meetup)
            join_link = request.build_absolute_uri(reverse('join_meetup_from_email', kwargs={
                'login_token': join_login.invite_code
            }))
            NewNearMeetupMessageView(recipient=activist).send(extra_context={
                'meetup': meetup,
                'join_link': join_link,
                'fb_button': {
                    'text': 'Ich bin dabei!',
                    'url': join_link
                }
            })

    @staticmethod
    def send_welcome_notification(activist):
        WelcomeMessageView(recipient=activist).send()

    @staticmethod
    def send_meetup_became_viable_notifications(meetup):
        for activist in meetup.activists.all():
            invite_link = make_absolute_url(reverse('invite', kwargs={'meetup_id': meetup.uuid}))
            extra_context={
                'meetup': meetup,
                'invite_link': invite_link,
                'participants_string': concat_list_verbosely([a.first_name for a in meetup.activists.all()])
            }
            if activist == meetup.owner:
                MeetupBecameViableOwnerMessageView(recipient=activist).send(extra_context=extra_context)
            else:
                MeetupBecameViableParticipantMessageView(recipient=activist).send(extra_context=extra_context)

    @staticmethod
    def send_welcome_to_viable_meetup(activist, meetup):
        invite_link = make_absolute_url(reverse('invite', kwargs={'meetup_id': meetup.uuid}))
        WelcomeToViableMeetupMessageView(recipient=activist).send(extra_context={
            'meetup': meetup,
            'invite_link': invite_link,
            'participants_string': concat_list_verbosely([a.first_name for a in meetup.activists.all()])
        })

