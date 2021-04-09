from django.contrib import admin
from .models import Details2

class DetailsModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "Publisher", "Class",  "Your_Address","Phone_number", "Edition", "Status"]
    class Meta:
        model = Details2

admin.site.register(Details2, DetailsModelAdmin)
