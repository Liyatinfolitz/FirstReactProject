# Generated by Django 4.2.4 on 2023-10-13 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=200)),
                ('img', models.URLField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('status', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=225)),
                ('empID', models.CharField(max_length=225, null=True)),
                ('desigination', models.CharField(default='', max_length=225)),
                ('username', models.CharField(default='', max_length=225)),
                ('email', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('role', models.CharField(default='Employee', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='', max_length=200)),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projects')),
                ('userID', models.ManyToManyField(to='app.user')),
            ],
        ),
    ]
