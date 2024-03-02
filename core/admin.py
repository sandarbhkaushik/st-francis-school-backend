from django.contrib import admin
# from .models import (History, PrincipalMessage, HeadMistressMessage, Vision, Mission)
from .models import (CorePage, Media, Event)
# Register your models here.

admin.site.register(CorePage)
admin.site.register(Media)
admin.site.register(Event)