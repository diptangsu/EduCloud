from django.db import models

from academics.models import Department
from academics.models import Subject

from questions.models import Question
from questions.models import Answer
from questions.models import QuestionVote
from questions.models import AnswerVote


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
    password = models.CharField(max_length=50)

    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14, default=None, blank=True, null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    date_of_birth = models.DateField(blank=True, null=True)

    address = models.TextField()
    picture = models.ImageField(upload_to='user_profile_pictures/')
    year_of_joining = models.IntegerField()

    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.user_type}: {self.first_name} {self.last_name} [{self.department.short_form}]'

    def reputation(self):
        questions = Question.objects.filter(user=self)
        answers = Answer.objects.filter(user=self)

        rep = 0

        for question in questions:
            question_upvotes = QuestionVote.objects.filter(question=question, vote_type='U').count()
            question_downvotes = QuestionVote.objects.filter(question=question, vote_type='D').count()

            rep += question_upvotes * 10
            rep -= question_downvotes * 1

        for answer in answers:
            answer_upvotes = AnswerVote.objects.filter(answer=answer, vote_type='U').count()
            answer_downvotes = AnswerVote.objects.filter(answer=answer, vote_type='D').count()

            rep += answer_upvotes * 20
            rep -= answer_downvotes * 2

        return rep


class StudentDetail(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    university_roll_no = models.BigIntegerField()
    university_administration_no = models.BigIntegerField()


class ProfessorDetail(models.Model):
    professor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class ProfessorSubject(models.Model):
    professor = models.ForeignKey(ProfessorDetail, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
