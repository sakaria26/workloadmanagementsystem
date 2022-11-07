# Generated by Django 4.1.2 on 2022-11-07 23:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminWorkload',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('activity_type', models.CharField(choices=[('Compulsory', 'Compulsory'), ('Major', 'Major'), ('Minor', 'Minor'), ('Voluntary', 'Voluntary')], max_length=12)),
                ('hours_per_semester', models.IntegerField()),
                ('staff_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appauth.staff_member')),
            ],
        ),
    ]
