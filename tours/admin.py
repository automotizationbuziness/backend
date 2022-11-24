from django.contrib import admin
from .models import Tour, TourClient
from .forms import TourForm

#admin.site.register(Tour)
admin.site.register(TourClient)

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
  def get_readonly_fields(self, request, obj=None):
    try:
        return [f.name for f in obj._meta.fields if not f.editable]
    except:
        return []
# @admin.register(Tour)
# class TourAdmin(admin.ModelAdmin):
#     form=TourForm

#     class Media:
#         js = (
#             '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
#             'js/myscript.js',       # project static folder
#             'app/js/myscript.js',   # app static folder
#             'https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js'
#         )
