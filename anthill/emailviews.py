#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import bot_api

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
            text = message.body[:320]
            bot_api.send_text(text=text, fb_bot_id=self.recipient.facebook_bot_id)
        else:
            return super(TemplatedNotificationView, self).send(extra_context=extra_context, **kwargs)



class LoginLinkMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/login/subject.txt'
    body_template_name = 'emails/login/body.txt'
    html_body_template_name = 'emails/login/body.html'
    bot_template_name = 'emails/login/bot.txt'


class WelcomeMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/welcome/subject.txt'
    body_template_name = 'emails/welcome/body.html'
    html_body_template_name = 'emails/welcome/body.html'
    bot_template_name = 'emails/welcome/bot.txt'


class NewNearMeetupMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/1_new_meetup_1person/subject.txt'
    body_template_name = 'emails/1_new_meetup_1person/body.txt'
    html_body_template_name = 'emails/1_new_meetup_1person/body.html'
    bot_template_name = 'emails/1_new_meetup_1person/bot.txt'


class MeetupBecameViableMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/4_date_confirmation/subject.txt'
    body_template_name = 'emails/4_date_confirmation/body.txt'
    html_body_template_name = 'emails/4_date_confirmation/body.html'
    bot_template_name = 'emails/4_date_confirmation/bot.txt'


class WelcomeToViableMeetupMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/welcome_to_viable_meetup/subject.txt'
    body_template_name = 'emails/welcome_to_viable_meetup/body.txt'
    html_body_template_name = 'emails/welcome_to_viable_meetup/body.html'
    bot_template_name = 'emails/welcome_to_viable_meetup/bot.txt'


