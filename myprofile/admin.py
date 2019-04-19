from django.contrib import admin
from .models import Myprofile, Skill
# Register your models here.

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class MyprofileAdmin(admin.ModelAdmin):
    list_display =('phone_number','facebook','twitter','instagram','github','gitlab')
    inlines = [SkillInline]
    class Meta:
        model = Myprofile

admin.site.register(Myprofile, MyprofileAdmin)

