# Generated by Django 3.2 on 2022-02-05 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_post_bvn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=300)),
                ('Phone_number', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Home.post')),
            ],
        ),
    ]
