# Generated by Django 2.2.7 on 2021-03-28 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creators', '0052_auto_20210325_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creator',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveIndex(
            model_name='creator',
            name='creators_cr_search__44165d_gin',
        ),
        migrations.RemoveField(
            model_name='creator',
            name='search_vector',
        ),
    ]
