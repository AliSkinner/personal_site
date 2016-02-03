from models import Item

class SidebarMiddleware(object):

    def process_template_response(self, request, response):
        response.context_data['items'] = Item.objects.exclude(active=False)
        return response
