from django.contrib import admin
from django import forms
from .models import Carsoul,Car_des,Services,aboutUs,whyUs,list, projects, videos, team
# Register your models here.



admin.site.register(Services)
admin.site.register(aboutUs)
admin.site.register(whyUs)
admin.site.register(list)
admin.site.register(projects)
admin.site.register(videos)
admin.site.register(team)

@admin.register(Carsoul)
class CarsoulAdmin(admin.ModelAdmin):
    list_display= ("Carsoul_image",)
    list_filter = ("Carsoul_image", )
    #fields = ("first_name", "last_name", "courses") control order of field and which are included
    #search_fields = ("last_name__startswith", ) this is search field
    #get_full_name.short_description = 'my label' 
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["Carsoul_image"].label = "Carsoul Image(max=3):"
        return form
    
    
@admin.register(Car_des)
class Car_desAdmin(admin.ModelAdmin):
    list_display= ("Car_description",)
    
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["Car_description"].label = "Carsoul_description(appears below carsoul):"
        return form