from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    short_form = models.CharField(max_length=10)

    def __str__(self):
        return self.name + ' [' + self.short_form + ']'


class Subject(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ' [' + self.code + ']'
