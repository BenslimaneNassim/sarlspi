# Generated by Django 4.2.5 on 2023-09-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('type_appart', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
