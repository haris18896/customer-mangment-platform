# Generated by Django 3.0.7 on 2020-07-29 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200729_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cusotmer',
            new_name='customer',
        ),
    ]
