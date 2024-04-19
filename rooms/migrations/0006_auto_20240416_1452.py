# Generated by Django 3.2.12 on 2024-04-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_rename_total_rooms_roomcategory_nombre_de_personnes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomcategory',
            name='price',
        ),
        migrations.AddField(
            model_name='roomcategory',
            name='motif_de_reservation',
            field=models.CharField(default='Veuillez entrer votre motif de reservation', max_length=50),
        ),
    ]