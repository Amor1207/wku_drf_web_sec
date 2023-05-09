from django.contrib import admin

# Register your models here.
from .models import Book, Course, Department, Instructor, Section, Semester, Student, Textbook, TextbookOrder

admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Section)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Textbook)
admin.site.register(TextbookOrder)

