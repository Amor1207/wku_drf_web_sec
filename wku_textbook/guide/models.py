from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    edition = models.CharField(max_length=200)
    year = models.IntegerField()
    def __str__(self):
        return self.title

class Course(models.Model):
    course_number = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    def __str__(self):
        return self.course_number

class Department(models.Model):
    department_name = models.CharField(max_length=200)
    def __str__(self):
        return self.department_name

class Instructor(models.Model):
    instructor_name = models.CharField(max_length=200)
    def __str__(self):
        return self.instructor_name

class Section(models.Model):
    section_number = models.CharField(max_length=200)
    def __str__(self):
        return self.section_number

class Semester(models.Model):
    semester_name = models.CharField(max_length=200)
    def __str__(self):
        return self.semester_name

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    def __str__(self):
        return self.student_name

class Textbook(models.Model):
    textbook_name = models.CharField(max_length=200)
    def __str__(self):
        return self.textbook_name

class TextbookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.title

# Compare this snippet from wku_textbook/guide/apps.py:
# from django.apps import AppConfig
