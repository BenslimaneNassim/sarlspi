# Generated by Django 4.2.5 on 2023-09-17 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spi', '0008_alter_devi_note_alter_devi_type_appart'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('telephone', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='email',
        ),
        migrations.DeleteModel(
            name='number',
        ),
        migrations.AddField(
            model_name='devi',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
