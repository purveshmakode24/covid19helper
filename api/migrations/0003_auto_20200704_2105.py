# Generated by Django 3.0.3 on 2020-07-04 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200704_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='name',
            new_name='applicant_name',
        ),
        migrations.RenameField(
            model_name='applicant',
            old_name='job',
            new_name='job_name',
        ),
    ]