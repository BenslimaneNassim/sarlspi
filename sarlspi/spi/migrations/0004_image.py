# Generated by Django 4.2.5 on 2023-09-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spi', '0003_bloc'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]