from django.contrib import admin

from .models import GoodPoll
from .models import BadPoll

# Register your models here.
class GoodPollAdmin(admin.ModelAdmin):
    pass
admin.site.register(GoodPoll, GoodPollAdmin)

class BadPollAdmin(admin.ModelAdmin):
    pass
admin.site.register(BadPoll, BadPollAdmin)