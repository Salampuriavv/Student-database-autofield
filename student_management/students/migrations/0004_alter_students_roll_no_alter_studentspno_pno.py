# Generated by Django 5.1.3 on 2024-12-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_students_name_alter_students_roll_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='roll_no',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='studentspno',
            name='pno',
            field=models.CharField(max_length=15),
        ),
    ]
