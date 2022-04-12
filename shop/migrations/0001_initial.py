# Generated by Django 4.0.3 on 2022-04-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='shop/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
