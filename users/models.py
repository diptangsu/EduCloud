from django.db import models
from academics.models import Department


class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    USER_TYPES = (
        ('P', 'Professor'),
        ('S', 'Student')
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPES)

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)

    email_id = models.EmailField(max_length=255)

    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14, default=None, blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    date_of_birth = models.DateField(blank=True, null=True)

    address = models.TextField()
    picture = models.ImageField(upload_to='student_profile_pictures/')
    year_of_joining = models.IntegerField()

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.user_type}: {self.first_name} {self.last_name} [{self.department.short_form}]'


class StudentDetail(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    university_roll = models.BigIntegerField(primary_key=True)


class ProfessorDetail(models.Model):
    professor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
