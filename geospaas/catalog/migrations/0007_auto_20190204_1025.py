# Generated by Django 2.1.5 on 2019-02-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20190130_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='source',
        ),
        migrations.RemoveField(
            model_name='source',
            name='specs',
        ),
        migrations.AddField(
            model_name='dataset',
            name='sources',
            field=models.ManyToManyField(to='catalog.Source'),
        ),
    ]
