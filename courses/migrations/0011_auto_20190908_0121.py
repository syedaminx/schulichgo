# Generated by Django 2.2.4 on 2019-09-08 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20190907_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='syllabus',
            field=models.FileField(upload_to='syllabus/'),
        ),
    ]
