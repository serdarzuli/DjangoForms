# Generated by Django 3.0.2 on 2025-02-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='dept',
            field=models.CharField(choices=[('MF', 'Manufacturing'), ('SH', 'Shipping'), ('AD', 'Administration'), ('HR', 'Human Resources')], default='HR', max_length=2),
        ),
    ]
