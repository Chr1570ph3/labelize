# Generated by Django 4.2 on 2023-04-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageClassification', '0003_classe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='raw/'),
        ),
    ]