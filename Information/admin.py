from django.contrib import admin
from .models import YearLevel, Section, Student, StudentGrade, Subject

# Register your models here.

@admin.register(YearLevel)
class YearLevelAdmin(admin.ModelAdmin):
    list_display = ['year_level']
    list_filter = ['school_level']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'year_level',]
    list_filter = ['year_level']
    fieldsets = (
        (('Section'), {'fields': ('section', 'year_level',)}),)

admin.site.register(Student)
admin.site.register(StudentGrade)
admin.site.register(Subject)
