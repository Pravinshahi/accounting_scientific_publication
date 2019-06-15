from django.db import models

# Create your models here.

#Cтатус
class Status(models.Model):
    ID_status = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'status'

#Тип пособия
class Benefit_type(models.Model):
    ID_benefit_type = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'benefit_type'

#Тип статьи
class Type_article(models.Model):
    ID_type_article = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'type_article'

#Библиографическая база
class Bibliographic_database(models.Model):
    ID_bibliographic_database = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'bibliographic_database'

#Издательство
class Publisher(models.Model):
    ID_publisher = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Confirmed = models.BooleanField()

    class Meta:
        db_table = 'publisher'

#Журнал/сборник
class Magazine(models.Model):
    ID_magazine = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Confirmed = models.BooleanField()

    class Meta:
        db_table = 'magazine'

#Гриф
class Vulture (models.Model):
    ID_vulture = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'vulture'

#Город
class City(models.Model):
    ID_city = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Confirmed = models.BooleanField()

    class Meta:
        db_table = 'city'

#Год
class Year(models.Model):
    ID_year = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'year'

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

#Тип публикация
class Type_publication(models.Model):
    ID_type_publication = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    class Meta:
        db_table = 'type_publication'

#Сотрудник
class Employee(models.Model):
    ID_employee = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    FIO = models.CharField(max_length=255)
    Date = models.DateField()
    ID_department = models.ForeignKey(Department, models.DO_NOTHING)
    ID_position = models.ForeignKey(Position, models.DO_NOTHING)
    ID_academic_title = models.ForeignKey(Academic_title, models.DO_NOTHING)
    ID_academic_degree = models.ForeignKey(Academic_degree, models.DO_NOTHING)


    class Meta:
        db_table = 'employee'

#Публикация
class Publication(models.Model):
    ID_publication = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    ID_status = models.ForeignKey(Status, models.DO_NOTHING)
    Date = models.DateField()
    ID_magazine = models.ForeignKey(Magazine, models.DO_NOTHING)
    Note = models.CharField(max_length=255)
    Link = models.CharField(max_length=255)
    Initial_page = models.CharField(max_length=255)
    Page_final = models.CharField(max_length=255)
    Tom = models.CharField(max_length=255)
    Issue_number = models.CharField(max_length=255)
    DOI = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    ID_type_publication = models.ForeignKey(Type_publication, models.DO_NOTHING)
    ID_employee = models.ForeignKey(Employee, models.DO_NOTHING)
    ID_city = models.ForeignKey(City, models.DO_NOTHING)
    ID_year = models.ForeignKey(Year, models.DO_NOTHING)
    File = models.CharField(max_length=255)
    ID_publisher = models.ForeignKey(Publisher, models.DO_NOTHING)
    ID_benefit_type = models.ForeignKey(Benefit_type, models.DO_NOTHING)
    ID_vulture = models.ForeignKey(Vulture, models.DO_NOTHING)
    ID_type_article = models.ForeignKey(Type_article, models.DO_NOTHING)

    class Meta:
        db_table = 'publication'


#ПубликацияСотрудник
class PublicationEmployee(models.Model):
    ID_publication_employee = models.AutoField(primary_key=True)
    ID_publication = models.ForeignKey(Publication, models.DO_NOTHING)
    ID_employee = models.ForeignKey(Employee, models.DO_NOTHING)

    class Meta:
        db_table = 'publication_employee'

#ПубликацияБиблиографическаябаза
class PublicationBibliographic_database(models.Model):
    ID_publication_bibliographic = models.AutoField(primary_key=True)
    ID_publication = models.ForeignKey(Publication, models.DO_NOTHING)
    ID_bibliographic_database = models.ForeignKey(Bibliographic_database, models.DO_NOTHING)

    class Meta:
        db_table = 'publication_bibliographic'