# Generated by Django 2.1 on 2020-04-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprawdzian', '0005_auto_20200403_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='plik_1',
            field=models.FileField(upload_to='upload/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='zdjecie_1',
            field=models.ImageField(default='default.jpg', upload_to='upload/'),
        ),
    ]
