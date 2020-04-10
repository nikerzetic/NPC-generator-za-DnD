from django.contrib import admin

from .models import Settlement, SettlementCharacteristic1, SettlementCharacteristic2, SettlementCharacteristic3, SettlementType


admin.site.register(Settlement)
admin.site.register(SettlementCharacteristic1)
admin.site.register(SettlementCharacteristic2)
admin.site.register(SettlementCharacteristic3)
admin.site.register(SettlementType)
