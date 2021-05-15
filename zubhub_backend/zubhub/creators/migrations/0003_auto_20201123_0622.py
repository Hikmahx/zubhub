# Generated by Django 2.2.7 on 2020-11-23 06:22

import creators.models
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0002_auto_20201123_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='phone',
            field=models.CharField(blank=True, max_length=17, unique=True),
        ),
    ]
