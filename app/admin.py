from django.contrib import admin
from app.models import RiskType, RiskTypeField

# Register your models here.


class RiskTypesAdmin(admin.ModelAdmin):
    pass


admin.site.register(RiskType, RiskTypesAdmin)
admin.site.register(RiskTypeField, RiskTypesAdmin)
