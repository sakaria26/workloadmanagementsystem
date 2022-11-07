# Generated by Django 4.1.2 on 2022-11-07 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_group',
            name='course_group_name',
        ),
        migrations.AddField(
            model_name='course_group',
            name='course_group_mode',
            field=models.CharField(choices=[('Full Time', 'FULL TIME'), ('Part Time', 'PART TIME'), ('Distance', 'DISTANCE')], default='Full Time', max_length=255),
        ),
        migrations.AddField(
            model_name='course_group',
            name='course_group_session',
            field=models.CharField(choices=[('Theory', 'THEORY'), ('Practical', 'PRACTICAL')], default='Theory', max_length=255),
        ),
        migrations.AlterField(
            model_name='course_group',
            name='course_group_number',
            field=models.IntegerField(null=True),
        ),
    ]
