# Generated by Django 4.1.7 on 2023-03-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=30)),
                ('task_body', models.TextField(blank=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
