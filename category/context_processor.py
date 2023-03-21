#information to be presented in evey page

from os import link
from sre_constants import CATEGORY
from .models import Services

def menu_links(request):
    links=Services.objects.all()
    return dict(links=links)