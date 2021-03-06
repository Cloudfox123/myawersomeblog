# Generated by Django 4.0.2 on 2022-02-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=150)),
                ('blog_date', models.DateField(auto_now_add=True)),
                ('blog_text', models.TextField(verbose_name=300)),
                ('blog_image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]
