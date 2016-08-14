from anthill.models import Activist

class UuidAuthBackend(object):
    """
    """

    def authenticate(self, uuid=None):
        try:
            return Activist.objects.get(uuid=uuid)
        except Activist.DoesNotExist:
            return None


    def get_user(self, user_id):
        try:
            return Activist.objects.get(pk=user_id)
        except Activist.DoesNotExist:
            return None
