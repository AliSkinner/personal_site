from homepage.models import Item

def items_processor(request):
    items = {'items': Item.objects.exclude(active=False)}
    return items
