# Generated by Django 4.0.1 on 2022-01-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('blog_id', models.IntegerField()),
                ('blog_description', models.TextField(max_length=1000)),
                ('blog_title', models.CharField(max_length=200)),
                ('author_id', models.IntegerField()),
                ('author_name', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
