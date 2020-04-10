
from django.urls import path
from .views import home, courses, Java_single, Pyhton_single, C_single, JavaScript_single, Laravel_single, Django_single, about, contact, Java_single_quize, Php_single, Html_single, Wp_single, Sql_single, Jq_single, Bootstrap_single
urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('java/<slug:slug>/', Java_single, name='Java_single'),
    path('python/<slug:slug>/', Pyhton_single, name='Pyhton_single'),
    path('c/<slug:slug>/', C_single, name='C_single'),
    path('JavaScript/<slug:slug>/', JavaScript_single,
         name='JavaScript_single'),
    path('laravel/<slug:slug>/', Laravel_single, name='Laravel_single'),
    path('django/<slug:slug>/', Django_single, name='Django_single'),
    path('php/<slug:slug>/', Php_single, name='Php_single'),
    path('html/<slug:slug>/', Html_single, name='Html_single'),
    path('wordpress/<slug:slug>/', Wp_single, name='Wp_single'),
    path('sql/<slug:slug>/', Sql_single, name='Sql_single'),
    path('jquery/<slug:slug>/', Jq_single, name='Jq_single'),
    path('bootstrap/<slug:slug>/', Bootstrap_single, name='Bootstrap_single'),



    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    path('java/quize/<slug:slug>/', Java_single_quize, name='Java_single_quize'),

]
