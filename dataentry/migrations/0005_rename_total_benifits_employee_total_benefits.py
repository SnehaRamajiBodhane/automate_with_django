# Generated by Django 5.0.1 on 2024-02-21 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0004_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='total_benifits',
            new_name='total_benefits',
        ),
    ]
