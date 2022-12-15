from django.contrib import admin
from .models import Report, ReportTable

class ReportTableInline(admin.TabularInline):
    model = ReportTable
    extra = 0

    # def get_formsets(self, request, obj=None):
    #     for inline in self.get_formsets(request, obj):
    #         inline.form.current_user = request.user
    #         yield inline.get_formset(request, obj), inline
    
    def get_readonly_fields(self, request, obj=None):
        return ['tour', 'has_offer', 'has_payed']


class ReportAdmin(admin.ModelAdmin):
    inlines=[ReportTableInline]
    model=Report
    def get_readonly_fields(self, request, obj=None):
        return ['payed_sum']

admin.site.register(Report, ReportAdmin)
