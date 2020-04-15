from django.contrib import admin

from .models import Settlement, Location, KnownFor, Economy, SettlementType


admin.site.register(Settlement)
admin.site.register(Location)
admin.site.register(KnownFor)
admin.site.register(Economy)
admin.site.register(SettlementType)
