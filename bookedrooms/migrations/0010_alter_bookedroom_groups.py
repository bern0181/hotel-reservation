# Generated by Django 3.2.12 on 2024-05-17 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookedrooms', '0009_alter_bookedroom_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedroom',
            name='groups',
            field=models.CharField(choices=[('CReSTIC', 'CReSTIC'), ('Lab-i*', 'Lab-i*'), ('LICIIS', 'LICIIS')], max_length=100),
        ),
    ]
