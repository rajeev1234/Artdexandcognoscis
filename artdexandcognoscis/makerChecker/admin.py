from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Variant)