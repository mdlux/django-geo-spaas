# Generated by Django 2.1.4 on 2019-01-01 10:54

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_entry_id_null'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='access_constraints',
            field=models.CharField(blank=True, choices=[('accessLevel0', 'Limited'), ('accessLevel1', 'In-house'), ('accessLevel2', 'Public')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='entry_id',
            field=models.CharField(default=uuid.uuid4, max_length=80, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_.-]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='dataseturi',
            name='uri',
            field=models.URLField(validators=[django.core.validators.URLValidator(schemes=['http', 'https', 'ftp', 'ftps', 'file'])]),
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('Investigator', 'Investigator'), ('Technical Contact', 'Technical Contact'), ('DIF Author', 'DIF Author')], max_length=20),
        ),
        migrations.AlterField(
            model_name='source',
            name='specs',
            field=models.CharField(default='', help_text='Further specifications of the source.', max_length=50),
        ),
    ]
