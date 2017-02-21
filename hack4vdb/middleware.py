from django.utils.deprecation import MiddlewareMixin

class CacheControl(MiddlewareMixin):
    def process_response(self, request, response):
      response['Cache-Control'] = 'no-cache, max-age=0, must-revalidate'
      return response
