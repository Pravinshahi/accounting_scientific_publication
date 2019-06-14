from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.index, name='index'),
    path('my', views.my_publication, name='my_publication'),
    path('my_monografi', views.my_monografi, name='my_monografi'),
    path('my_monografi/update/<int:id>', views.my_monografi_update, name='my_monografi_update'),
    path('my_monografi/more/<int:id>', views.monografi_more, name='monografi_more'),
    path('my_publication_add_NIR', views.my_publication_add_NIR, name='my_publication_add_NIR'),
    path('my_publication_add_article', views.my_publication_add_article, name='my_publication_add_article'),
    path('my_publication_add_study', views.my_publication_add_study, name='my_publication_add_study'),
    path('download_files', views.download_files, name='download_files'),
    path('download_act_enter', views.download_act_enter, name='download_act_enter'),
    path('profile', views.profile, name='profile'),
    path('admin_index', views.admin_index, name='admin_index'),
    path('biblio', views.bibliographic, name='bibliographic'),
    path('biblio/add', views.biblio_add, name='biblio_add'),
    path('biblio/update/<int:id>', views.biblio_update, name='biblio_update'),
    path('staff', views.staff, name='staff'),
    path('staff/add', views.staff_add, name='staff_add'),
    path('staff/update/<int:id>', views.staff_update, name='staff_update'),
    path('magazines', views.magazines, name='magazines'),
    path('magazines/add', views.magazines_add, name='magazines_add'),
    path('magazines/update/<int:id>', views.magazines_update, name='magazines_update'),
    path('faculty', views.faculty, name='faculty'),
    path('faculty/add', views.faculty_add, name='faculty_add'),
    path('faculty/update/<int:id>', views.faculty_update, name='faculty_update'),
    path('department', views.department, name='department'),
    path('department/add', views.department_add, name='department_add'),
    path('department/update/<int:id>', views.department_update, name='department_update'),

    path('temp_add', views.temp_add, name='temp_add')

]