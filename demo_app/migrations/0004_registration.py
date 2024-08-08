# Generated by Django 4.2.11 on 2024-08-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0003_product_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
            ],
        ),
    ]
