# Generated by Django 4.2.5 on 2023-09-11 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spi', '0006_alter_bloc_etat'),
    ]

    operations = [
        migrations.CreateModel(
            name='number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=100)),
            ],
        ),
    ]
