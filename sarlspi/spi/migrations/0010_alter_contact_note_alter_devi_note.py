# Generated by Django 4.2.5 on 2023-09-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spi', '0009_contact_delete_email_delete_number_devi_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='note',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='devi',
            name='note',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]