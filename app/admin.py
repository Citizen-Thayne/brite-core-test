from django.contrib import admin
from app.models import RiskType, AbstractRiskFieldType, DateRiskField, EnumRiskField, TextRiskField, NumberRiskField

# Register your models here.


class RiskTypesAdmin(admin.ModelAdmin):
    pass


admin.site.register(RiskType, RiskTypesAdmin)
admin.site.register(DateRiskField, RiskTypesAdmin)
admin.site.register(EnumRiskField, RiskTypesAdmin)
admin.site.register(TextRiskField, RiskTypesAdmin)
admin.site.register(NumberRiskField, RiskTypesAdmin)
