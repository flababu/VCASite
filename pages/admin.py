from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Philosophy, Mission, Vision, Virtues, Prayer, PhysicalAddress, MailingAddress, ContactPerson, ExtraContact, DrivingDirection


# Register your models here.
class LogEntryAdmin(admin.ModelAdmin):
    model = LogEntry

    # get_change_message.short_description = 'ACTIONS'

    actions = None
    list_display = ['user','content_type','object_id','object_repr', 'action_flag','get_change_message','action_time']
    link_display_link = (None,)

admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(Philosophy)
admin.site.register(Mission)
admin.site.register(Vision)
admin.site.register(Virtues)
admin.site.register(Prayer)
admin.site.register(PhysicalAddress)
admin.site.register(MailingAddress)
admin.site.register(ContactPerson)
admin.site.register(ExtraContact)
admin.site.register(DrivingDirection)
admin.site.site_title = 'VCAAT Admin Page'
admin.site.site_header = 'VCAAT Admin Page'
