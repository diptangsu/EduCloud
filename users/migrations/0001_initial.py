# Generated by Django 2.2.1 on 2019-05-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('P', 'Professor'), ('S', 'Student')], max_length=1)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=14)),
                ('phone2', models.CharField(blank=True, default=None, max_length=14, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.TextField()),
                ('picture', models.ImageField(upload_to='user_profile_pictures/')),
                ('year_of_joining', models.IntegerField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorDetail',
            fields=[
                ('professor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.User')),
                ('university_roll_no', models.BigIntegerField()),
                ('university_administration_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfessorSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.Subject')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.ProfessorDetail')),
            ],
        ),
    ]