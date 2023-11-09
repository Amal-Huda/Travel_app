from django.contrib import admin
from .models import destinations,mydestination,people,mypeople

# Register your models here.
admin.site.register(destinations)
admin.site.register(mydestination)
admin.site.register(people)
admin.site.register(mypeople)
