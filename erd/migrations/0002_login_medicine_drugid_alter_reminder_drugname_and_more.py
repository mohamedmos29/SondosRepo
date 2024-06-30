# Generated by Django 4.2.4 on 2024-06-30 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.AddField(
            model_name='medicine',
            name='DrugID',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='DrugName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erd.medicine'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
