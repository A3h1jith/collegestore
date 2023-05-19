# Generated by Django 4.2.1 on 2023-05-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='materials_provide',
        ),
        migrations.AddField(
            model_name='order',
            name='materials_needed',
            field=models.TextField(blank=True, default='pen', null=True),
        ),
    ]