from mailviews.messages import TemplatedHTMLEmailMessageView


class TemplatedNotificationView(TemplatedHTMLEmailMessageView):
    subject_template_name = ''
    body_template_name = ''
    html_body_template_name = ''
    bot_template_name = ''

    def __init__(self, recipient, *args, **kwargs):
        super(TemplatedNotificationView, self).__init__(*args, **kwargs)
        self.recipient = recipient

    def get_context_data(self, **kwargs):
        context = super(TemplatedNotificationView, self).get_context_data(**kwargs)
        context['recipient'] = self.recipient
        return context

    def render_to_message(self, *args, **kwargs):
        assert 'to' not in kwargs  # this should only be sent to the user
        if self.recipient.email:
            kwargs['to'] = (self.recipient.email,)
        else:
            kwargs['to'] = ("{}@fb_bot".format(self.recipient.facebook_bot_id),)
        kwargs['from_email'] = 'VDB 4 President <noreply@weilsumwasgeht.at>'
        return super(TemplatedNotificationView, self).render_to_message( *args, **kwargs)


class LoginLinkMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/login/subject.txt'
    body_template_name = 'emails/login/body.html'
    html_body_template_name = 'emails/login/body.html'
    # bot_template_name = 'emails/login/bot.txt'


class WelcomeMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/welcome/subject.txt'
    body_template_name = 'emails/welcome/body.html'
    html_body_template_name = 'emails/welcome/body.html'
    bot_template_name = 'emails/welcome/bot.txt'


class NewNearMeetupMessageView(TemplatedNotificationView):
    subject_template_name = 'emails/1_new_meetup_1person/subject.txt'
    body_template_name = 'emails/1_new_meetup_1person/body.html'
    html_body_template_name = 'emails/1_new_meetup_1person/body.html'
    bot_template_name = 'emails/1_new_meetup_1person/bot.txt'
