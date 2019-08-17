from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core import serializers
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


@csrf_exempt
def login(request):
    if request.method == 'POST':

        re_data = request.POST
        username = re_data['username']
        passw = re_data['pas']
        user = auth.authenticate(username=username, password=passw)

        if user is not None:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('admin_index')
            else:
                return redirect('index')

    return render(request, 'publication/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

#Главная страница_ Все публикации
@login_required
def index(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/index.html',{'publications': publication,'type_publications':type_publication})


@login_required
def all_article(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/all_article.html',{'publications': publication,'type_publications':type_publication})


@login_required
def all_monografi(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/all_monografi.html',{'publications': publication,'type_publications':type_publication})


@login_required
def all_NIR(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/all_NIR.html',{'publications': publication,'type_publications':type_publication})


@login_required
def all_patent(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/all_patent.html',{'publications': publication,'type_publications':type_publication})

@login_required
def all_software(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/all_software.html',{'publications': publication,'type_publications':type_publication})

@login_required
def all_study(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/all_study.html',{'publications': publication,'type_publications':type_publication})


#Мои публикации
@login_required
@csrf_exempt
def my_publication(request):
    publication = Publication.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "DELETE":
            publication_temp = re_data['publication']
            # print(order)
            data = Publication.objects.get(ID_publication=publication_temp)
            data.delete()
            return redirect('my_publication')

    return render(request, 'publication/my.html',{'publications': publication, 'user':request.user})

#Монографии
@login_required
@csrf_exempt
def my_monografi(request):
    publisher = Publisher.objects.all()
    year = Year.objects.all()
    city = City.objects.all()
    biblio = Bibliographic_database.objects.all()

    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name='Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Монография')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City,ID_city = re_data['city'])
            publisher = get_object_or_404(Publisher,ID_publisher = re_data['publisher'])
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, Name='Отсутствует')
            finance = get_object_or_404(Source_finance, Name='Отсутствует')

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(request.user.username +'/'+uploaded_file.name, uploaded_file)

            Publication.objects.create(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'],ID_publisher = publisher,
                                       Issue_number=re_data['number_pages'], ISBN=re_data['ISBN'], ID_status=status,
                                       Date=a, ID_year =year, ID_city = city, File = uploaded_file.name,
                                       ID_magazine=magezine, ID_type_publication=type_publication,  ID_user_profile=employee,
                                       ID_benefit_type = benefit, ID_vulture = vulture, ID_type_article = type_article,
                                       ID_source_finance = finance
                                       )
            return redirect('my_publication')

        if re_data['_method'] == "PUT":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name='Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Монография')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City, ID_city=re_data['city'])
            publisher = get_object_or_404(Publisher, ID_publisher=re_data['publisher'])

            try:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                fs.save(employee.user.username + '/' + uploaded_file.name, uploaded_file)
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'],ID_status = status,
                                                                                    Date = a, ID_magazine = magezine,
                                                                                    Note=re_data['note'], Link = re_data['Link'],
                                                                                    Issue_number=re_data['number_pages'],
                                                                                    DOI=re_data['DOI'], ISBN=re_data['ISBN'],
                                                                                    ID_type_publication=type_publication,
                                                                                    ID_user_profile = employee, ID_city=city,
                                                                                    ID_year =year, File=uploaded_file.name,
                                                                                    ID_publisher = publisher)
            except:
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'],ID_status=status,
                                                                                    Date=a, ID_magazine=magezine,
                                                                                    Note=re_data['note'],Link=re_data['Link'],
                                                                                    Issue_number=re_data['number_pages'],
                                                                                    DOI=re_data['DOI'], ISBN=re_data['ISBN'],
                                                                                    ID_type_publication=type_publication,
                                                                                    ID_user_profile=employee, ID_city=city,
                                                                                    ID_year=year, ID_publisher=publisher)

            return redirect('my_publication')

    return render(request, 'publication/monografi.html',{'publishers':publisher, 'years':year, 'cities':city, 'biblio':biblio })

@login_required
def my_monografi_update(request,id):
    p = get_object_or_404(Publication, ID_publication=id)
    publisher = Publisher.objects.all()
    year = Year.objects.all()
    city = City.objects.all()
    biblio = Bibliographic_database.objects.all()

    return render(request, 'publication/monografi_update.html', {'publication':p,'publishers':publisher, 'years':year, 'cities':city, 'biblio':biblio})

@login_required
def publication_more(request,id):
    p = get_object_or_404(Publication, ID_publication=id)

    if p.ID_type_publication.Name == "Монография":
        return render(request, 'publication/monografi_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Пособие":
        return render(request, 'publication/study_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Статья":
        return render(request, 'publication/article_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Отчет по НИР":
        return render(request, 'publication/NIR_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Патент":
        return render(request, 'publication/patent_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Свидетельство на ПО":
        return render(request, 'publication/software_more.html', {'publication': p})

#Мое пособие
@login_required
@csrf_exempt
def my_study(request):
    b = Benefit_type.objects.all()
    y = Year.objects.all()
    c = City.objects.all()
    p = Publisher.objects.all()
    v = Vulture.objects.all()
    biblio = Bibliographic_database.objects.all()

    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name='Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Пособие')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City,ID_city = re_data['city'])
            vulture = get_object_or_404(Vulture,ID_vulture = re_data['vulture'])
            publisher = get_object_or_404(Publisher,ID_publisher = re_data['publisher'])
            benefit = get_object_or_404(Benefit_type, ID_benefit_type=re_data['benefit'])
            type_article = get_object_or_404(Type_article, Name='Отсутствует')
            finance = get_object_or_404(Source_finance, Name='Отсутствует')

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(employee.user.username +'/'+uploaded_file.name, uploaded_file)

            Publication.objects.create(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'],ID_publisher = publisher, ID_benefit_type = benefit,
                                       Issue_number=re_data['number_pages'], ISBN=re_data['ISBN'], ID_status=status,
                                       Date=a, ID_year =year, ID_city = city, File = uploaded_file.name,
                                       ID_magazine=magezine, ID_type_publication=type_publication, ID_user_profile=employee,
                                       ID_vulture = vulture, ID_type_article = type_article, ID_source_finance = finance)
            return redirect('my_publication')

        if re_data['_method'] == "PUT":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name='Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Монография')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City, ID_city=re_data['city'])
            publisher = get_object_or_404(Publisher, ID_publisher=re_data['publisher'])
            vulture = get_object_or_404(Vulture, ID_vulture=re_data['vulture'])
            benefit = get_object_or_404(Benefit_type, ID_benefit_type=re_data['benefit'])

            try:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'],ID_publisher = publisher, ID_benefit_type = benefit,
                                       Issue_number=re_data['number_pages'], ISBN=re_data['ISBN'], ID_status=status,
                                       Date=a, ID_year =year, ID_city = city, File = uploaded_file.name,
                                       ID_magazine=magezine, ID_type_publication=type_publication, ID_user_profile=employee,
                                       ID_vulture = vulture)
            except:
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'],ID_publisher = publisher, ID_benefit_type = benefit,
                                       Issue_number=re_data['number_pages'], ISBN=re_data['ISBN'], ID_status=status,
                                       Date=a, ID_year =year, ID_city = city, ID_vulture = vulture,
                                       ID_magazine=magezine, ID_type_publication=type_publication, ID_user_profile=employee)

            return redirect('my_publication')


    return render(request, 'publication/study.html',{'benefits':b, 'years':y, 'cities':c, 'publishers': p, 'vulturies':v, 'biblios': biblio})

@login_required
def my_study_update(request,id):
    b = Benefit_type.objects.all()
    y = Year.objects.all()
    c = City.objects.all()
    p = Publisher.objects.all()
    v = Vulture.objects.all()
    biblio = Bibliographic_database.objects.all()
    publication = get_object_or_404(Publication, ID_publication=id)
    return render(request, 'publication/study_update.html', {'benefits':b, 'years':y, 'cities':c, 'publishers': p,
                                                             'vulturies':v, 'biblios': biblio, 'publication': publication})

#Моя статья
@login_required
@csrf_exempt
def my_article(request):
    m = Magazine.objects.all()
    y = Year.objects.all()
    p = Publisher.objects.all()
    b = Bibliographic_database.objects.all()
    t = Type_article.objects.all()

    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine,ID_magazine = re_data['magazine'])
            type_publication = get_object_or_404(Type_publication, Name='Статья')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, ID_type_article = re_data['type'])
            publisher = get_object_or_404(Publisher, ID_publisher=re_data['publisher'])
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            finance = get_object_or_404(Source_finance, Name='Отсутствует')

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)

            Publication.objects.create(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'], ID_publisher=publisher, ID_status=status,
                                       Date=a, ID_year=year, ID_city=city, File=uploaded_file.name,
                                       ID_magazine=magezine, ID_type_publication=type_publication, ID_user_profile=employee,
                                       ID_type_article = type_article, Tom = re_data['tom'], Initial_page = re_data['begin'],
                                       Page_final = re_data['end'],Issue_number = re_data['number'],ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance)
            return redirect('my_publication')

        if re_data['_method'] == "PUT":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine,ID_magazine = re_data['magazine'])
            type_publication = get_object_or_404(Type_publication, Name='Статья')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, ID_type_article=re_data['type'])
            publisher = get_object_or_404(Publisher, ID_publisher=re_data['publisher'])
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')

            try:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'], ID_publisher=publisher, ID_status=status,
                                       Date=a, ID_year=year, ID_city=city, File=uploaded_file.name,
                                       ID_magazine=magezine, ID_type_publication=type_publication, ID_user_profile=employee,
                                       ID_type_article = type_article, Tom = re_data['tom'], Initial_page = re_data['begin'],
                                       Page_final = re_data['end'],Issue_number = re_data['number'],ID_benefit_type = benefit,
                                       ID_vulture = vulture)
            except:
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'], ID_publisher=publisher, ID_status=status,
                                       Date=a, ID_year=year, ID_city=city,ID_magazine=magezine,
                                       ID_type_publication=type_publication, ID_user_profile=employee,ID_type_article = type_article,
                                       Tom = re_data['tom'], Initial_page = re_data['begin'],
                                       Page_final = re_data['end'],Issue_number = re_data['number'],ID_benefit_type = benefit,
                                       ID_vulture = vulture)

            return redirect('my_publication')

    return render(request, 'publication/article.html',{'magazines':m, 'years':y, 'publishers':p, 'biblio':b, 'type': t})

@login_required
def my_article_update(request,id):
    m = Magazine.objects.all()
    y = Year.objects.all()
    p = Publisher.objects.all()
    b = Bibliographic_database.objects.all()
    t = Type_article.objects.all()


    publication = get_object_or_404(Publication, ID_publication=id)
    return render(request, 'publication/article_update.html', {'magazines':m, 'years':y, 'publishers':p, 'biblio':b,
                                                               'type': t, 'publication': publication})



#Мой отчет по НИР
@login_required
@csrf_exempt
def my_NIR(request):
    y = Year.objects.all()
    s = Source_finance.objects.all()
    b = Bibliographic_database.objects.all()

    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name = 'Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Отчет по НИР')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, Name ='Отсутствует')
            publisher = get_object_or_404(Publisher, Name='Отсутствует')
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            finance = get_object_or_404(Source_finance, ID_source_finance = re_data['finance'])

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)

            Publication.objects.create(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       File=uploaded_file.name, ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number']
                                       )
            return redirect('my_publication')

        if re_data['_method'] == "PUT":
            print('fdsfsdsdfg')
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name='Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Отчет по НИР')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, Name='Отсутствует')
            publisher = get_object_or_404(Publisher, Name='Отсутствует')
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            finance = get_object_or_404(Source_finance, ID_source_finance=re_data['finance'])

            try:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       File=uploaded_file.name, ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number'])
            except:
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number'])

            return redirect('my_publication')

    return render(request, 'publication/NIR.html',{'finance':s, 'year':y, 'biblio':b})

@login_required
def my_NIR_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    y = Year.objects.all()
    s = Source_finance.objects.all()
    b = Bibliographic_database.objects.all()

    return render(request, 'publication/NIR_update.html',{'finance':s, 'year':y, 'biblio':b, 'publication':publication})

#Мой патент
@csrf_exempt
@login_required
def my_patent(request):
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name = 'Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Патент')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year,Name='Отсутствует')
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, Name ='Отсутствует')
            publisher = get_object_or_404(Publisher, Name='Отсутствует')
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            finance = get_object_or_404(Source_finance, Name='Отсутствует')

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)

            Publication.objects.create(Name=re_data['name'], Note=re_data['note'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       File=uploaded_file.name, ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number']
                                       )
            return redirect('my_publication')

        if re_data['_method'] == "PUT":
            a = re_data['date']
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name='Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Патент')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year,Name='Отсутствует')
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, Name='Отсутствует')
            publisher = get_object_or_404(Publisher, Name='Отсутствует')
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            finance = get_object_or_404(Source_finance,Name='Отсутствует')

            try:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       File=uploaded_file.name, ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number'])
            except:
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number'])

            return redirect('my_publication')

    return render(request, 'publication/patent.html',{})

@login_required
def my_patent_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    return render(request, 'publication/patent_update.html',{'publication':publication})

#Мое свидетельство на ПО
@login_required
@csrf_exempt
def my_software(request):
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":
            a = datetime.datetime.today().strftime("%Y-%m-%d")
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name = 'Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Свидетельство на ПО')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year,Name='Отсутствует')
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, Name ='Отсутствует')
            publisher = get_object_or_404(Publisher, Name='Отсутствует')
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            finance = get_object_or_404(Source_finance, Name='Отсутствует')

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)

            Publication.objects.create(Name=re_data['name'], Note=re_data['note'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       File=uploaded_file.name, ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number']
                                       )
            return redirect('my_publication')

        if re_data['_method'] == "PUT":
            a = re_data['date']
            status = get_object_or_404(Status, Name='Ожидает подтверждения')
            magezine = get_object_or_404(Magazine, Name='Отсутствует')
            type_publication = get_object_or_404(Type_publication, Name='Свидетельство на ПО')
            employee = get_object_or_404(UserProfile, user=request.user)
            year = get_object_or_404(Year,Name='Отсутствует')
            city = get_object_or_404(City, Name='Отсутствует')
            type_article = get_object_or_404(Type_article, Name='Отсутствует')
            publisher = get_object_or_404(Publisher, Name='Отсутствует')
            benefit = get_object_or_404(Benefit_type, Name='Отсутствует')
            vulture = get_object_or_404(Vulture, Name='Отсутствует')
            finance = get_object_or_404(Source_finance,Name='Отсутствует')

            try:
                uploaded_file = request.FILES['document']
                fs = FileSystemStorage()
                fs.save(employee.user.username  + '/' + uploaded_file.name, uploaded_file)
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       File=uploaded_file.name, ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number'])
            except:
                Publication.objects.filter(ID_publication=re_data['new_id']).update(Name=re_data['name'], Note=re_data['note'],
                                       ID_publisher=publisher, ID_status=status, Date=a, ID_year=year, ID_city=city,
                                       ID_magazine=magezine, ID_type_publication=type_publication,
                                       ID_user_profile=employee, ID_type_article = type_article,ID_benefit_type = benefit,
                                       ID_vulture = vulture, ID_source_finance = finance, State_registration_number = re_data['number'])

            return redirect('my_publication')
    return render(request, 'publication/software.html',{})

@login_required
def my_software_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    return render(request, 'publication/software_update.html',{'publication':publication})

#Мои публикации
@login_required
def profile(request):
    prof = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'publication/profile.html',{'profile':prof})

############################################################################
############################################################################
############################       АДМИН    ################################
############################################################################
############################################################################

#Главная страница администратора
@login_required
def admin_index(request):
    publication = Publication.objects.all()
    return render(request, 'publication/admin_main.html',{'publications':publication})

@login_required
def admin_index_ready(request):
    publication = Publication.objects.all()
    return render(request, 'publication/admin_main_ready.html',{'publications':publication})

@login_required
def admin_index_none(request):
    publication = Publication.objects.all()
    return render(request, 'publication/admin_main_none.html',{'publications':publication})

############################################################################
############################################################################
############################       Справочники    ################################
############################################################################
############################################################################

@csrf_exempt
@login_required
def bibliographic(request):
    biblio = Bibliographic_database.objects.all()

    if request.method == 'POST':
        re_data = request.POST
        # Редактирование
        if re_data['_method'] == "PUT":
            Bibliographic_database.objects.filter(ID_bibliographic_database=re_data['new_id']).update(Name=re_data['name'])
            return redirect('bibliographic')

        if re_data['_method'] == "POST":
            Bibliographic_database.objects.create(Name=re_data['name'])
            return redirect('bibliographic')

    return render(request, 'publication/biblio.html',{'biblio': biblio})

@login_required
def biblio_add(request):

    return render(request, 'publication/biblio_add.html')

@login_required
def biblio_update(request,id):
    b = get_object_or_404(Bibliographic_database, ID_bibliographic_database=id)
    return render(request, 'publication/biblio_update.html', {'biblio':b})

@login_required
@csrf_exempt
def staff(request):
    #em = Employee.objects.all()
    u = UserProfile.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":

            d = get_object_or_404(Department, ID_department=re_data['department'])
            p = get_object_or_404(Position,ID_position=re_data['position'])
            t = get_object_or_404(Academic_title, ID_academic_title =re_data['title'])
            deg = get_object_or_404(Academic_degree, ID_academic_degree=re_data['degree'])
            user = User.objects.create_user(username=re_data['login'], email=re_data['email'], password=re_data['password'])
            UserProfile.objects.create(user=user, FIO = re_data['name'],ID_department = d, ID_position = p, ID_academic_title = t,
                                       ID_academic_degree = deg)

            return redirect('staff')

        if re_data['_method'] == "PUT":
            d = get_object_or_404(Department, ID_department=re_data['department'])
            p = get_object_or_404(Position, ID_position=re_data['position'])
            t = get_object_or_404(Academic_title, ID_academic_title=re_data['title'])
            deg = get_object_or_404(Academic_degree, ID_academic_degree=re_data['degree'])
            UserProfile.objects.filter(ID_user_profile=re_data['new_id']).update(
                FIO=re_data['name'],login=re_data['login'],password = re_data['password'],Date=re_data['date'],ID_department=d,
            ID_position = p,ID_academic_title = t, ID_academic_degree = deg)

            return redirect('staff')

    return render(request, 'publication/admin_employee.html',{'employees': u})

@login_required
def staff_add(request):
    d = Department.objects.all()
    p = Position.objects.all()
    t = Academic_title.objects.all()
    deg = Academic_degree.objects.all()
    return render(request, 'publication/admin_employee_add.html',{'depatrments': d, 'positions': p, 'title':t, 'degrees':deg})

@login_required
def staff_update(request,id):
    em = get_object_or_404(UserProfile, ID_user_profile=id)
    d = Department.objects.all()
    p = Position.objects.all()
    t = Academic_title.objects.all()
    deg = Academic_degree.objects.all()
    return render(request, 'publication/admin_employee_update.html',{'employee': em,'depatrments': d, 'positions': p, 'title':t, 'degrees':deg})

@login_required
@csrf_exempt
def magazines(request):
    mag = Magazine.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        # Редактирование
        if re_data['_method'] == "PUT":
            Magazine.objects.filter(ID_magazine=re_data['new_id']).update(
                Name=re_data['name'])
            return redirect('magazines')

        if re_data['_method'] == "POST":
            Magazine.objects.create(Name=re_data['name'], Confirmed=True)
            return redirect('magazines')

    return render(request, 'publication/admin_mag.html',{'magazines': mag})

@login_required
def magazines_add(request):
    return render(request, 'publication/admin_mag_add.html')

@login_required
def magazines_update(request,id):
    mag = get_object_or_404(Magazine, ID_magazine=id)
    return render(request, 'publication/admin_mag_update.html',{'magazine': mag,})


@login_required
@csrf_exempt
def faculty(request):
    f = Faculty.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        # Редактирование
        if re_data['_method'] == "PUT":
            Faculty.objects.filter(ID_faculty=re_data['new_id']).update(
                Name=re_data['name'])
            return redirect('faculty')

        if re_data['_method'] == "POST":
            Faculty.objects.create(Name=re_data['name'])
            return redirect('faculty')

    return render(request, 'publication/admin_faculty.html',{'faculties': f})

@login_required
def faculty_add(request):
    return render(request, 'publication/admin_faculty_add.html')

@login_required
def faculty_update(request,id):
    f = get_object_or_404(Faculty, ID_faculty=id)
    return render(request, 'publication/admin_faculty_update.html',{'faculty': f,})

@login_required
@csrf_exempt
def department(request):
    d = Department.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        # Редактирование
        if re_data['_method'] == "PUT":
            f = get_object_or_404(Faculty, ID_faculty=re_data['faculty'])
            Department.objects.filter(ID_department=re_data['new_id']).update(
                Name=re_data['name'],ID_faculty=f )
            return redirect('department')

        if re_data['_method'] == "POST":
            f = get_object_or_404(Faculty, ID_faculty=re_data['faculty'])
            Department.objects.create(Name=re_data['name'],ID_faculty=f)
            return redirect('department')

    return render(request, 'publication/admin_department.html',{'departments': d})

@login_required
def department_add(request):
    f = Faculty.objects.all()
    return render(request, 'publication/admin_department_add.html', {'faculty':f})

@login_required
def department_update(request,id):
    d = get_object_or_404(Department, ID_department=id)
    f = Faculty.objects.all()
    return render(request, 'publication/admin_department_update.html',{'department': d,'faculty':f})

@csrf_exempt
@login_required
def show_report_of_department(request):
    p = Publication.objects.all()
    year = Year.objects.all()
    department = Department.objects.all()
    return render(request, 'publication/show_report_of_department.html',{'department': department,'publications': p,'year': year})

@csrf_exempt
@login_required
def report_on_the_departments(request):
    f = Faculty.objects.all()
    d = Department.objects.all()
    y= Year.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        department = re_data['id_department']
        year = re_data['id_year']
        #redirect('show_report_of_department', department, year)
        redirect('show_report_of_department')

    return render(request, 'publication/report_on_the_departments.html',{'departments': d,'faculties': f,'year': y})


@login_required
@csrf_exempt
def admin_publication_more(request,id):
    p = get_object_or_404(Publication, ID_publication=id)

    if p.ID_type_publication.Name == "Монография":
        return render(request, 'publication/admin_monografi_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Пособие":
        return render(request, 'publication/admin_study_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Статья":
        return render(request, 'publication/admin_article_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Отчет по НИР":
        return render(request, 'publication/admin_NIR_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Патент":
        return render(request, 'publication/admin_patent_more.html', {'publication': p})

    if p.ID_type_publication.Name == "Свидетельство на ПО":
        return render(request, 'publication/admin_software_more.html', {'publication': p})


@login_required
@csrf_exempt
def admin_software_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    status = Status.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "PUT":
            status = get_object_or_404(Status, ID_status=re_data['status'])
            Publication.objects.filter(ID_publication=re_data['new_id']).update(Note=re_data['note'], ID_status=status)
            return redirect('admin_index')

    return render(request, 'publication/admin_update_software.html',{'publication':publication, 'statuss':status})

@login_required
@csrf_exempt
def admin_patent_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    status = Status.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "PUT":
            status = get_object_or_404(Status, ID_status=re_data['status'])
            Publication.objects.filter(ID_publication=re_data['new_id']).update(Note=re_data['note'], ID_status=status)
            return redirect('admin_index')

    return render(request, 'publication/admin_update_patent.html',{'publication':publication, 'statuss':status})

@login_required
@csrf_exempt
def admin_monografi_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    status = Status.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "PUT":
            status = get_object_or_404(Status, ID_status=re_data['status'])
            Publication.objects.filter(ID_publication=re_data['new_id']).update(Note=re_data['note'], ID_status=status)
            return redirect('admin_index')

    return render(request, 'publication/admin_update_monografi.html',{'publication':publication, 'statuss':status})

@login_required
@csrf_exempt
def admin_study_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    status = Status.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "PUT":
            status = get_object_or_404(Status, ID_status=re_data['status'])
            Publication.objects.filter(ID_publication=re_data['new_id']).update(Note=re_data['note'], ID_status=status)
            return redirect('admin_index')

    return render(request, 'publication/admin_update_study.html',{'publication':publication, 'statuss':status})

@login_required
@csrf_exempt
def admin_article_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    status = Status.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "PUT":
            status = get_object_or_404(Status, ID_status=re_data['status'])
            Publication.objects.filter(ID_publication=re_data['new_id']).update(Note=re_data['note'], ID_status=status)
            return redirect('admin_index')

    return render(request, 'publication/admin_update_article.html',{'publication':publication, 'statuss':status})

@login_required
@csrf_exempt
def admin_NIR_update(request,id):
    publication = get_object_or_404(Publication, ID_publication=id)
    status = Status.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "PUT":
            status = get_object_or_404(Status, ID_status=re_data['status'])
            Publication.objects.filter(ID_publication=re_data['new_id']).update(Note=re_data['note'], ID_status=status)
            return redirect('admin_index')

    return render(request, 'publication/admin_update_NIR.html',{'publication':publication, 'statuss':status})

@login_required
@csrf_exempt
def download_act_enter(request):
    if request.method == 'POST':
        re_data = request.POST
        id = re_data['id_file']
        p = get_object_or_404(Publication, ID_publication=id)
        file_path = 'publication/static/publication/documents/' + p.ID_user_profile.user.username + '/' + p.File
        data = open(file_path, "rb").read()
        response = HttpResponse(data, content_type='application;')
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = 'attachment; filename=%s' % p.File

        return response
