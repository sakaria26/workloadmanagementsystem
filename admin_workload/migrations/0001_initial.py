# Generated by Django 4.1.2 on 2022-10-31 00:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminWorkload',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('activity_type', models.CharField(choices=[('Compulsory', 'Compulsory'), ('Major', 'Major'), ('Minor', 'Minor'), ('Voluntary', 'Voluntary')], max_length=12)),
                ('hours_per_semester', models.IntegerField()),
            ],
        ),
    ]
