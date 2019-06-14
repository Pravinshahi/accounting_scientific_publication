from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core import serializers
from django.core.files.storage import FileSystemStorage
import os
from django.http import HttpResponse

# Create your views here.

# Session of users
user_employee = "0"
username_global = ''

@csrf_exempt
def temp_add(request):
    d = Bibliographic_database.objects.all()
    opt_json = serializers.serialize('json', d)
    if request.method == 'POST':
        print("dfsfdas")
        re_data = request.POST
        print(re_data)

    return render(request, 'publication/temp_add.html',{'databases':d, 'opt':opt_json})


@csrf_exempt
def login(request):
    global user_employee
    user_employee = "0"
    if request.method == 'POST':

        re_data = request.POST
        username = re_data['username']
        passw = re_data['pas']

        if username == "000":
            return redirect('admin_index')

        temp = get_object_or_404(Employee, login=username, password=passw)



        if temp.FIO != None:
            user_employee = temp.ID_employee
            global username_global
            username_global = username
            return redirect('index')


    return render(request, 'publication/login.html')

#Главная страница_ Все публикации
def index(request):
    publication = Publication.objects.all()
    type_publication = Type_publication.objects.all()
    return render(request, 'publication/index.html',{'publications': publication,'type_publications':type_publication})


#Мои публикации
@csrf_exempt
def my_publication(request):
    publication = Publication.objects.all()
    if request.method == 'POST':
        re_data = request.POST

        # Удаление
        if re_data['_method'] == "DELETE":
            publication_temp = re_data['publication']
            #print(order)
            data = Publication.objects.get(ID_publication=publication_temp)
            data.delete()
    return render(request, 'publication/my.html',{'publications': publication})

#Монографии
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
            employee = get_object_or_404(Employee, FIO='Елисеев Петр Витальевич')
            year = get_object_or_404(Year, ID_year=re_data['year'])
            city = get_object_or_404(City,ID_city = re_data['city'])
            publisher = get_object_or_404(Publisher,ID_city = re_data['publisher'])

            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            fs.save(employee.login+'/'+uploaded_file.name, uploaded_file)

            Publication.objects.create(Name=re_data['name'], Note=re_data['note'], Link=re_data['Link'],
                                       DOI=re_data['DOI'],ID_publisher = publisher,
                                       Issue_number=re_data['number_pages'], ISBN=re_data['ISBN'], ID_status=status,
                                       Date=a, ID_year =year, ID_city = city, File = uploaded_file.name,
                                       ID_magazine=magezine, ID_type_publication=type_publication, ID_employee=employee,
                                       )
            return redirect('my_publication')



    return render(request, 'publication/monografi.html',{'publishers':publisher, 'years':year, 'cities':city, 'biblio':biblio })

def my_monografi_update(request,id):
    p = get_object_or_404(Publication, ID_publication=id)
    publisher = Publisher.objects.all()
    year = Year.objects.all()
    city = City.objects.all()
    biblio = Bibliographic_database.objects.all()

    return render(request, 'publication/monografi_update.html', {'publication':p,'publishers':publisher, 'years':year, 'cities':city, 'biblio':biblio})

def monografi_more(request,id):
    p = get_object_or_404(Publication, ID_publication=id)
    return render(request, 'publication/monografi_more.html', {'publication':p})

#Мои публикации
def my_publication_add_NIR(request):
    return render(request, 'publication/NIR.html',{})

#Мои публикации
def my_publication_add_study(request):
    return render(request, 'publication/study.html',{})

#Мои публикации
def my_publication_add_article(request):
    return render(request, 'publication/article.html',{})

#Мои публикации
def profile(request):
    global username_global
    prof = get_object_or_404(Employee, login=username_global)
    return render(request, 'publication/profile.html',{'profile':prof})

############################################################################
############################################################################
############################       АДМИН    ################################
############################################################################
############################################################################

#Главная страница администратора
def admin_index(request):
    publication = Publication.objects.all()
    return render(request, 'publication/admin_main.html',{'publication':publication})

############################################################################
############################################################################
############################       Справочники    ################################
############################################################################
############################################################################

@csrf_exempt
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

def biblio_add(request):
    return render(request, 'publication/biblio_add.html')

def biblio_update(request,id):
    b = get_object_or_404(Bibliographic_database, ID_bibliographic_database=id)
    return render(request, 'publication/biblio_update.html', {'biblio':b})

@csrf_exempt
def staff(request):
    em = Employee.objects.all()
    if request.method == 'POST':
        re_data = request.POST
        if re_data['_method'] == "POST":
            d = get_object_or_404(Department, ID_department=re_data['department'])
            p = get_object_or_404(Position,ID_position=re_data['position'])
            t = get_object_or_404(Academic_title, ID_academic_title =re_data['title'])
            deg = get_object_or_404(Academic_degree, ID_academic_degree=re_data['degree'])

            Employee.objects.create(login=re_data['login'], password=re_data['password'],FIO=re_data['name'],
                                    Date=re_data['date'],ID_department=d,ID_position=p,ID_academic_title=t,
                                    ID_academic_degree=deg)

            return redirect('staff')

        if re_data['_method'] == "PUT":
            d = get_object_or_404(Department, ID_department=re_data['department'])
            p = get_object_or_404(Position, ID_position=re_data['position'])
            t = get_object_or_404(Academic_title, ID_academic_title=re_data['title'])
            deg = get_object_or_404(Academic_degree, ID_academic_degree=re_data['degree'])
            Employee.objects.filter(ID_employee=re_data['new_id']).update(
                FIO=re_data['name'],login=re_data['login'],password = re_data['password'],Date=re_data['date'],ID_department=d,
            ID_position = p,ID_academic_title = t, ID_academic_degree = deg)

            return redirect('staff')

    return render(request, 'publication/admin_employee.html',{'employees': em})

def staff_add(request):
    d = Department.objects.all()
    p = Position.objects.all()
    t = Academic_title.objects.all()
    deg = Academic_degree.objects.all()
    return render(request, 'publication/admin_employee_add.html',{'depatrments': d, 'positions': p, 'title':t, 'degrees':deg})

def staff_update(request,id):
    em = get_object_or_404(Employee, ID_employee=id)
    d = Department.objects.all()
    p = Position.objects.all()
    t = Academic_title.objects.all()
    deg = Academic_degree.objects.all()
    return render(request, 'publication/admin_employee_update.html',{'employee': em,'depatrments': d, 'positions': p, 'title':t, 'degrees':deg})

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

def magazines_add(request):
    return render(request, 'publication/admin_mag_add.html')

def magazines_update(request,id):
    mag = get_object_or_404(Magazine, ID_magazine=id)
    return render(request, 'publication/admin_mag_update.html',{'magazine': mag,})


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

def faculty_add(request):
    return render(request, 'publication/admin_faculty_add.html')

def faculty_update(request,id):
    f = get_object_or_404(Faculty, ID_faculty=id)
    return render(request, 'publication/admin_faculty_update.html',{'faculty': f,})

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

def department_add(request):
    f = Faculty.objects.all()
    return render(request, 'publication/admin_department_add.html', {'faculty':f})

def department_update(request,id):
    d = get_object_or_404(Department, ID_department=id)
    f = Faculty.objects.all()
    return render(request, 'publication/admin_department_update.html',{'department': d,'faculty':f})


def report_on_the_departments(request):
    f = Faculty.objects.all()
    d = Department.objects.all()
    y= Year.objects.all()
    return render(request, 'publication/admin_department.html',{'departments': d,'faculties': f,'year': y})

def download_files(request):
    print("pашли")
    if request.method == 'POST':
        re_data = request.POST
        id = re_data['id_file']
        p = get_object_or_404(Publication, ID_publication=id)
        file_path = 'publication/static/publication/documents/'+p.ID_employee.login+'/'+p.File
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response

@csrf_exempt
def download_act_enter(request):
    print("pашли")
    filename ='publication/static/publication/documents/4/33ca0d707a0867ad39d253b4b98fb177.jpg'
    data = open(filename, "rb").read()
    response = HttpResponse(data, content_type='application;')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename=%s' % '33ca0d707a0867ad39d253b4b98fb177.jpg'

    return response
   