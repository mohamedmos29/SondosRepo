# Generated by Django 4.2.4 on 2024-06-30 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erd', '0002_login_medicine_drugid_alter_reminder_drugname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='DrugID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
