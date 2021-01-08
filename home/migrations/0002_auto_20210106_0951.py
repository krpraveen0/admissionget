# Generated by Django 3.0 on 2021-01-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnggCollege',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LawCollege',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCollege',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MmgCollege',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='College',
        ),
    ]
