# Generated by Django 3.2.12 on 2024-05-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='isSecretary',
            field=models.BooleanField(default=False),
        ),
    ]
