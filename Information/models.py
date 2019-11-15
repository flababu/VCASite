from django.db import models
from django.core.validators import MaxValueValidator
from users.models import Parent


# Create your models here.

class YearLevel(models.Model):
    year_level = models.CharField(max_length = 100)


    Preschool = 'Preschool'
    Gradeschool = 'Gradeschool'
    JuniorHighschool = 'Junior Highschool'
    SeniorHighschool = 'Senior Highschool'
    Unspecified = 'None'
    SchoolLevel_choices = (
        ('Preschool', Preschool),
        ('Gradeschool', Gradeschool),
        ('JuniorHighschool', JuniorHighschool),
        ('SeniorHighschool', SeniorHighschool),
        ('Unspecified', Unspecified),
    )
    school_level = models.CharField(max_length = 30, choices=SchoolLevel_choices , default = Unspecified)

    def __str__(self):
        return self.year_level

class Section(models.Model):
    year_level = models.ForeignKey(YearLevel, on_delete=models.SET_NULL, null = True)
    section = models.CharField(max_length = 100)

    def __str__(self):
        return '{}'.format(self.section)



class Student(models.Model):

    first_name = models.CharField(max_length = 100, default = '')
    last_name = models.CharField(max_length = 100, default = '')
    middle_name = models.CharField(max_length = 100, null = True)
    birth_date = models.DateField(null = True)
    student_number = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)])
    year_level = models.OneToOneField(YearLevel, on_delete=models.SET_NULL, null = True)
    section = models.OneToOneField(Section, on_delete=models.SET_NULL, null = True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null = True)


    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

class Subject(models.Model):
    subject_name = models.CharField(max_length = 100)


class StudentGrade(models.Model):

    PERIOD_CHOICES = [
        (1, 'First Grading'),
        (2, 'Second Grading'),
        (3, 'Third Grading'),
        (4, 'Fourth Grading'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE,) #null=True)
    period = models.PositiveSmallIntegerField(choices=PERIOD_CHOICES)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)
