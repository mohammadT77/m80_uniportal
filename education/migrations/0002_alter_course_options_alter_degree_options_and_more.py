# Generated by Django 4.1.4 on 2022-12-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='degree',
            options={'verbose_name': 'Degree', 'verbose_name_plural': 'Degrees'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': 'Professor', 'verbose_name_plural': 'Professors'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'verbose_name': 'Semester', 'verbose_name_plural': 'Semesters'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AddField(
            model_name='department',
            name='name',
            field=models.CharField(default=None, max_length=20, verbose_name='Department name'),
            preserve_default=False,
        ),
    ]