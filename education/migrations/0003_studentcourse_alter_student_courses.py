# Generated by Django 4.1.4 on 2023-01-05 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_course_options_alter_degree_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_mark', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='education.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='education.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, through='education.StudentCourse', to='education.course',
                                         verbose_name='Courses'),
        ),
    ]