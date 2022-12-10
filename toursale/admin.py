from django.contrib import admin
from .models import TourSale, TourSaleEnd, OrderTourEnd
from order.admin import OrderTourInline
from django.shortcuts import redirect



class TourAdmin(admin.ModelAdmin):
    model = TourSale

    class Media:
        js = ['tour_sale_autofill.js']
    

    def response_add(self, request, obj, post_url_continue=None):
        body = max(map(lambda x: x.id, TourSaleEnd.objects.all()))
        return redirect(
            f'/admin/toursale/toursaleend/{body}/change/'
        )


class OrderTourEndInline(admin.TabularInline):
    model = OrderTourEnd
    extra = 1

    # def get_formsets(self, request, obj=None):
    #     for inline in self.get_formsets(request, obj):
    #         inline.form.current_user = request.user
    #         yield inline.get_formset(request, obj), inline
    
    def get_readonly_fields(self, request, obj=None):
        try:
            return [f.name for f in obj._meta.fields if not f.editable] + 'total_cost'
        except:
            return ['total_cost']
    



class AdminOrder(admin.ModelAdmin):
    model = TourSaleEnd
    inlines = [OrderTourEndInline]
    #fields = ['client', 'payment_type', 'orders']

    def get_readonly_fields(self, request, obj=None):
        try:
            return [f.name for f in obj._meta.fields if not f.editable] + 'total_cost'
        except:
            return ['total_cost']
    
    
    
    
    class Media:
        js = [ 'https://code.jquery.com/jquery-3.3.1.min.js', 'order_autofill.js']


admin.site.register(TourSale, TourAdmin)
admin.site.register(TourSaleEnd, AdminOrder)