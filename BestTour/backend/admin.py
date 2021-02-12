from django.contrib import admin

from .models import *


class BookedAdmin(admin.ModelAdmin):
    list_display = ("user", "tour")


admin.site.register(RoomType)
admin.site.register(MealType)
admin.site.register(Hotel)
admin.site.register(Tour)
admin.site.register(BookedTour, BookedAdmin)
admin.site.register(Request)
admin.site.register(Status)
admin.site.register(Invoice)
admin.site.register(Type)
admin.site.register(Job)
