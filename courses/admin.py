from django.contrib import admin
from .models import *
# Register your models here.


class Courses_name_admin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Courses_name, Courses_name_admin)


class Java_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Java_courses, Java_courses_admin)

# Python_courses


class Pyhton_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Python_courses, Pyhton_courses_admin)
# End Python_courses

# C_courses


class C_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(C_courses, C_courses_admin)
# End C_courses

# JavaScript_courses


class Js_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(JavaScript_courses, Js_courses_admin)
# End JavaScript_courses

# Laravel_courses


class Laravel_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Laravel_courses, Laravel_courses_admin)
# End Laravel_courses


# Django_courses
class Django_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Django_courses, Django_courses_admin)
# End Django_courses

# Php_courses


class Php_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Php_courses, Php_courses_admin)
# End Php_courses

# Wordpress_courses


class Wp_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Wp_courses, Wp_courses_admin)
# End Wordpress_courses

# Html_courses


class Html_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Html_courses, Html_courses_admin)
# End Html_courses

# Jquery_courses


class Jq_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Jq_courses, Jq_courses_admin)
# End Jquery_courses

# Sql_courses


class Sq_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Sql_courses, Sq_courses_admin)
# End Sql_courses


# Bootstrap_courses
class Bootstrap_courses_admin(admin.ModelAdmin):
    list_display = ['title', 'name', 'pub_date']
    list_filter = ['title', 'name', 'pub_date']
    list_editable = ['name']


admin.site.register(Bootstrap_courses, Bootstrap_courses_admin)
# End Bootstrap_courses

# Java_quize_courses
admin.site.register(Java_quize_courses)
# End Java_quize_courses
# Contact
admin.site.register(Contact)
# End Contact
