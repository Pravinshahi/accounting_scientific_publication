# Generated by Django 2.2.1 on 2019-05-20 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_degree',
            fields=[
                ('ID_academic_degree', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'academic_degree',
            },
        ),
        migrations.CreateModel(
            name='Academic_title',
            fields=[
                ('ID_academic_title', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'academic_title',
            },
        ),
        migrations.CreateModel(
            name='Bibliographic_database',
            fields=[
                ('ID_bibliographic_database', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'bibliographic_database',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('ID_faculty', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'faculty',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('ID_magazine', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'magazine',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('ID_position', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('ID_status', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('ID_department', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('ID_faculty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='publication.Faculty')),
            ],
            options={
                'db_table': 'department',
            },
        ),
    ]
