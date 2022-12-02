from django.contrib import admin
from .models import Order, OrderTour

class OrderTourInline(admin.TabularInline):
    model = OrderTour
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
    model = Order
    inlines = [OrderTourInline]
    #fields = ['client', 'payment_type', 'orders']

    def get_readonly_fields(self, request, obj=None):
        try:
            return [f.name for f in obj._meta.fields if not f.editable] + 'total_cost'
        except:
            return ['total_cost']
    

    class Media:
        js = [ 'https://code.jquery.com/jquery-3.3.1.min.js', 'order_autofill.js']

admin.site.register(Order, AdminOrder)
