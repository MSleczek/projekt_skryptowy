# Generated by Django 2.1 on 2020-04-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inne', '0003_auto_20200402_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='plik_1',
            field=models.FileField(default='default.pdf', upload_to='upload_file/'),
        ),
        migrations.AddField(
            model_name='post',
            name='plik_2',
            field=models.FileField(default='default.pdf', upload_to='upload_file/'),
        ),
        migrations.AddField(
            model_name='post',
            name='plik_3',
            field=models.FileField(default='default.pdf', upload_to='upload_file/'),
        ),
        migrations.AddField(
            model_name='post',
            name='plik_4',
            field=models.FileField(default='default.pdf', upload_to='upload_file/'),
        ),
        migrations.AddField(
            model_name='post',
            name='zdjecie_1',
            field=models.ImageField(default='default.jpg', upload_to='upload_img/'),
        ),
        migrations.AddField(
            model_name='post',
            name='zdjecie_2',
            field=models.ImageField(default='default.jpg', upload_to='upload_img/'),
        ),
        migrations.AddField(
            model_name='post',
            name='zdjecie_3',
            field=models.ImageField(default='default.jpg', upload_to='upload_img/'),
        ),
    ]
