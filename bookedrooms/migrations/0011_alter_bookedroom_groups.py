# Generated by Django 3.2.12 on 2024-05-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookedrooms', '0010_alter_bookedroom_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedroom',
            name='groups',
            field=models.CharField(choices=[('CReSTIC', 'CReSTIC'), ('Lab-i*', 'Lab-i*'), ('LICIIS', 'LICIIS'), ('Autre', 'Autre')], max_length=100),
        ),
    ]
