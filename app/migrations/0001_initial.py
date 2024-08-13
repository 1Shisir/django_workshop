# Generated by Django 5.1 on 2024-08-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('faculty', models.CharField(choices=[('Management', 'Management'), ('Science & Technology', 'Science & Technology')], max_length=50)),
                ('programme', models.CharField(choices=[('BBA', 'BBA'), ('BCA', 'BCA'), ('MCA', 'MCA'), ('MBA', 'MBA')], max_length=20)),
            ],
        ),
    ]
