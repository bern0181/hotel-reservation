# Generated by Django 3.2.12 on 2024-06-14 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0003_alter_equipmentcategory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentcategory',
            name='nbrEquipments',
        ),
    ]
