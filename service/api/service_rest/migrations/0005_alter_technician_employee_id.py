# Generated by Django 4.0.3 on 2023-04-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0004_alter_technician_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technician',
            name='employee_id',
            field=models.IntegerField(unique=True),
        ),
    ]
