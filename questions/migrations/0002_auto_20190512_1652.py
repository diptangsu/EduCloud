# Generated by Django 2.2.1 on 2019-05-12 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='student',
            new_name='user',
        ),
    ]