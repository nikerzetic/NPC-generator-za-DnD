from django.contrib import admin

from .models import AdministrativeUnit, SettlementType, SettlementProperties, Settlement


admin.site.register(Settlement)
admin.site.register(AdministrativeUnit)
admin.site.register(SettlementProperties)
admin.site.register(SettlementType)
