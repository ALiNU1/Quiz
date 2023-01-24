from django.contrib import admin
from .models import Categories,Answer,Question

# Register your models here.
admin.site.register(Categories)
admin.site.register(Question)
admin.site.register(Answer)
