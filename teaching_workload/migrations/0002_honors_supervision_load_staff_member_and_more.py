# Generated by Django 4.1.2 on 2022-11-08 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appauth', '0001_initial'),
        ('teaching_workload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='honors_supervision_load',
            name='staff_member',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appauth.staff_member'),
        ),
        migrations.CreateModel(
            name='Teaching_Load_Remove_Request',
            fields=[
                ('remove_request_id', models.AutoField(primary_key=True, serialize=False)),
                ('teaching_load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching_workload.teaching_load')),
            ],
        ),
        migrations.CreateModel(
            name='Honors_Supervision_Load_Remove_Request',
            fields=[
                ('remove_request_id', models.AutoField(primary_key=True, serialize=False)),
                ('honors_supervision_load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching_workload.honors_supervision_load')),
            ],
        ),
    ]
