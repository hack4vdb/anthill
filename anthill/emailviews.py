#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured

from anthill import bot_api
from anthill.utils import split_string_by_newlines

from mailviews.messages import TemplatedHTMLEmailMessageView
from mailviews.utils import unescape


class TemplatedNotificationView(TemplatedHTMLEmailMessageView):
    subject_template_name = ''
    body_template_name = ''
    html_body_template_name = ''
    bot_template_name = ''

    def __init__(self, recipient, *args, **kwargs):
        super(TemplatedNotificationView, self).__init__(*args, **kwargs)
        self.recipient = recipient

    def _is_facebook_bot(self):
        return bool(self.recipient.facebook_bot_id)

    def get_context_data(self, **kwargs):
        context = super(TemplatedNotificationView, self).get_context_data(**kwargs)
        context['recipient'] = self.recipient
        return context

    def render_body(self, context):
        if self._is_facebook_bot():
            return self.bot_template.render(unescape(context))
        else:
            return super(TemplatedNotificationView, self).render_body(context)

    def _get_bot_template(self):
        if getattr(self, '_bot_template', None) is not None:
            return self._bot_template
        if self.bot_template_name is None:
            raise ImproperlyConfigured('A `bot_template` or '
                '`bot_template_name` must be provided to render this '
                'bot message.')
        return self._get_template(self.bot_template_name)

    def _set_bot_template(self, template):
        self._bot_template = template

    bot_template = property(_get_bot_template, _set_bot_template)

    def render_to_message(self, *args, **kwargs):
        assert 'to' not in kwargs  # this should only be sent to the user
        if not self._is_facebook_bot():
            kwargs['to'] = (self.recipient.email,)
            kwargs['from_email'] = 'Weil\'s um was geht <aktiv@weilsumwasgeht.at>'
        return super(TemplatedNotificationView, self).render_to_message( *args, **kwargs)

    def send(self, extra_context=None, **kwargs):
        if self._is_facebook_bot():
            message = self.render_to_message(extra_context=extra_context, **kwargs)
            text = message.body
            text_chunks = split_string_by_newlines(text, 320)
            for i in range(len(text_chunks)):
                if 'fb_button' in extra_context and i == 0:
                    bot_api.send_text_with_button(
                        text=text_chunks[i],
                        button=extra_context.get('fb_button', {}),
                        fb_bot_id=self.recipient.facebook_bot_id,
                        delay=i*5
                    )
                else:
                    bot_api.send_text(
                        text=text_chunks[i],
                        fb_bot_id=self.recipient.facebook_bot_id,
                        delay=i*5
                    )
        else:
            return super(TemplatedNotificationView, self).send(extra_context=extra_context, **kwargs)



class LoginLinkMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/login_link/subject.txt'
    body_template_name = 'emails/login_link/body.txt'
    html_body_template_name = 'emails/login_link/body.html'
    bot_template_name = 'emails/login_link/bot.txt'


class WelcomeMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/welcome/subject.txt'
    body_template_name = 'emails/welcome/body.txt'
    html_body_template_name = 'emails/welcome/body.html'
    bot_template_name = 'emails/welcome/bot.txt'


class NewNearMeetupMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/new_meetup_in_proximity/subject.txt'
    body_template_name = 'emails/new_meetup_in_proximity/body.txt'
    html_body_template_name = 'emails/new_meetup_in_proximity/body.html'
    bot_template_name = 'emails/new_meetup_in_proximity/bot.txt'


class MeetupBecameViableParticipantMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/meetup_became_viable_participant/subject.txt'
    body_template_name = 'emails/meetup_became_viable_participant/body.txt'
    html_body_template_name = 'emails/meetup_became_viable_participant/body.html'
    bot_template_name = 'emails/meetup_became_viable_participant/bot.txt'


class MeetupBecameViableOwnerMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/meetup_became_viable_owner/subject.txt'
    body_template_name = 'emails/meetup_became_viable_owner/body.txt'
    html_body_template_name = 'emails/meetup_became_viable_owner/body.html'
    bot_template_name = 'emails/meetup_became_viable_owner/bot.txt'


class WelcomeToViableMeetupMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/welcome_to_viable_meetup/subject.txt'
    body_template_name = 'emails/welcome_to_viable_meetup/body.txt'
    html_body_template_name = 'emails/welcome_to_viable_meetup/body.html'
    bot_template_name = 'emails/welcome_to_viable_meetup/bot.txt'


