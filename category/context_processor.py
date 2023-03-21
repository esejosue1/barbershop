#information to be presented in evey page

from os import link
from sre_constants import CATEGORY
from .models import typeOfService

def menu_links(request):
    links=typeOfService.objects.all()
    return dict(links=links)