from django.core.management.base import BaseCommand, CommandError

from anthill.models import *
from anthill.views import ActivistViewSet
import imaplib
import email, email.header, email.message


class Command(BaseCommand):
    help = 'imports mails from IMAP to Activists'

    def add_arguments(self, parser):
        parser.add_argument('action', choices=['import', 'show'])


    def handle(self, *args, **options):

        from anthill import settings

        M = imaplib.IMAP4_SSL(settings.IMAP_HOST)
        M.login(settings.IMAP_USER, settings.IMAP_PASSWORD)
        M.select()

        typ, data = M.search(None, 'ALL')
        for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')
            msg = email.message_from_string(data[0][1])
            msg_text = msg.get_payload(decode=True)
            subject = unicode(email.header.decode_header(msg['Subject'])[0][0])

            if settings.MAIL_SUBJECT != subject:
                continue
            if settings.MAIL_FROM != msg['From'].split(' ')[0]:
                continue

            data = {}
            for line in msg_text.split("\r\n"):
                if not line:
                    continue
                else:
                    print("line:"+line)
                    split = line.split(': ')

                    data[split[0]] = split[1]

           # TODO:
           # translate field names in data[] to API names (eg; data['Vorname'] would be first_name in the API implementation)
           # POST to API (internally?http?), probably there is some kind of validation in the API (postalcodes,etc),
           # which would be bypassed if written directly to the model?
            print 'Message num: %s\nSubject: %s\nmsg-data:%s\n' % (num, subject, msg.get_payload(decode=True))
        M.close()
        M.logout()

