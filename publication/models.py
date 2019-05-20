from django.db import models

# Create your models here.

#Cтатус
class Status(models.Model):
    ID_status = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'status'

#Библиографическая база
class Bibliographic_database(models.Model):
    ID_bibliographic_database = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'bibliographic_database'

#Журнал/сборник
class Magazine(models.Model):
    ID_magazine = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'magazine'

#Ученое звание
class Academic_title(models.Model):
    ID_academic_title = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'academic_title'

#Ученая степень
class Academic_degree(models.Model):
    ID_academic_degree = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'academic_degree'

#Должность
class Position(models.Model):
    ID_position = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'position'

#Факультет
class Faculty(models.Model):
    ID_faculty = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'faculty'

#Кафедра
class Department(models.Model):
    ID_department = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    ID_faculty = models.ForeignKey(Faculty, models.DO_NOTHING)

    class Meta:
        db_table = 'department'