# Generated by Django 2.2 on 2021-09-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='cell_phone',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='department',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True),
        ),
    ]
