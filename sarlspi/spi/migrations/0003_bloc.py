# Generated by Django 4.2.5 on 2023-09-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spi', '0002_rename_devis_devi_rename_emails_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('etat', models.TextField(blank=True, max_length=1500, null=True)),
            ],
        ),
    ]
