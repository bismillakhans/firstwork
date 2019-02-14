# Generated by Django 2.1.2 on 2019-02-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('img', models.ImageField(upload_to='images')),
                ('text', models.CharField(blank=True, max_length=70)),
                ('ocrtext', models.CharField(blank=True, max_length=70)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True, verbose_name='Approve')),
            ],
        ),
    ]