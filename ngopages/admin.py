from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import RegisterNgoForm
from .models import NgoActivityModel, RegisterNgoModel


# Register your models here
admin.site.register(RegisterNgoModel)


@admin.register(NgoActivityModel)
class NgoActivityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
