# Generated by Django 3.2.6 on 2021-09-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_categorie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]