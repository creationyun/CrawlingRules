from django.contrib import admin
from rules.models import Rule, Filter, Attribute

# Register your models here.
admin.site.register(Rule)
admin.site.register(Filter)
admin.site.register(Attribute)
