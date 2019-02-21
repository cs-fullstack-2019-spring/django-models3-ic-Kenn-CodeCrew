from django.contrib import admin
from .models import Chair
from .models import Person

# Register your models here.
admin.site.register(Chair)
admin.site.register(Person)