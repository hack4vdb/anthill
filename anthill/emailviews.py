from mailviews.messages import TemplatedEmailMessageView


class GenericMessageView(TemplatedEmailMessageView):
    subject_template_name = ''
    body_template_name = ''

    def __init__(self, email, *args, **kwargs):
        super(GenericMessageView, self).__init__(*args, **kwargs)
        self.email = email

    def get_context_data(self, **kwargs):
        context = super(GenericMessageView, self).get_context_data(**kwargs)
        context['email'] = self.email
        return context

    def render_to_message(self, *args, **kwargs):
        assert 'to' not in kwargs  # this should only be sent to the user
        kwargs['to'] = (self.email,)
        return super(
            GenericMessageView,
            self).render_to_message(
            *
            args,
            **kwargs)


class WelcomeMessageView(GenericMessageView):
    subject_template_name = 'emails/welcome/subject.txt'
    body_template_name = 'emails/welcome/body.txt'
