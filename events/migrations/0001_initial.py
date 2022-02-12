# Generated by Django 4.0.2 on 2022-02-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='event_images/')),
                ('event_text', models.CharField(max_length=300)),
            ],
        ),
    ]