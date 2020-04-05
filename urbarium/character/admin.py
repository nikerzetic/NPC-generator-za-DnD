from django.contrib import admin

from .models import Gender, Race, Appearance, Mannerism, InteractionTrait, Ideal, Bond, Character


admin.site.register(Character)
admin.site.register(Gender)
admin.site.register(Race)
admin.site.register(Appearance)
admin.site.register(Mannerism)
admin.site.register(InteractionTrait)
admin.site.register(Ideal)
admin.site.register(Bond)
