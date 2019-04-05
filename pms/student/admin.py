from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportModelAdmin
from .models import StudentDetails,RegisterdStudents

@admin.register(StudentDetails)
class StudentDetailsAdmin(ImportExportModelAdmin):
    pass

admin.site.register(RegisterdStudents)