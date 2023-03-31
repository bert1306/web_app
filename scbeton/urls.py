from django.urls import path, include
from . import views
#from cards.utils import role_required
from django.conf import settings
from django.conf.urls.static import static

app_name = 'scbeton'

urlpatterns = [

    path('', views.scbeton, name='scbeton'),
]
