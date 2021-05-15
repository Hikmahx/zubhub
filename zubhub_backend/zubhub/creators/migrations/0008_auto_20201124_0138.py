# Generated by Django 2.2.7 on 2020-11-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0007_creator_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator',
            name='is_admin',
        ),
        migrations.AlterField(
            model_name='creator',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
