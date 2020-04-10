from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
# Create your views here.


# Home
def home(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.warning(
                request, 'এই  ব্যবহারকারী নাম আগেই রেজিস্ট্রেশন করা হয়েছে ')
        elif User.objects.filter(email=email).exists():
            messages.warning(
                request, 'এই ইমেইল আগেই রেজিস্ট্রেশন করা হয়েছে ')
        else:
            user = User.objects.create_user(
                username=username, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(
                request, 'আমাদের রেজিস্ট্রেশন করার জন্য ধন্যবাদ')
            return redirect('/courses')
    courses_names = Courses_name.objects.all()
    courses_list = Java_courses.objects.all()
    context = {
        'courses_names': courses_names,
        'courses_list': courses_list
    }
    return render(request, 'index.html', context)
# End Home

# Course Name
def courses(request):
    courses_names = Courses_name.objects.all()
    courses_list = Java_courses.objects.all()
    query = request.GET.get("q")
    if query:
        courses_names = Courses_name.objects.filter(
            Q(title__icontains=query) | Q(
                name__icontains=query) | Q(details__icontains=query)
        )
    context = {
        'courses_names': courses_names,
        'courses_list': courses_list
    }
    return render(request, 'courses.html', context)
# End Course Name

# Java Single
def Java_single(request, slug):
    single = get_object_or_404(Java_courses, slug=slug)
    first = Java_courses.objects.first()
    last = Java_courses.objects.last()
    courses_list = Java_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Java Single

# Python Single
def Pyhton_single(request, slug):
    single = get_object_or_404(Python_courses, slug=slug)
    first = Python_courses.objects.first()
    last = Python_courses.objects.last()
    courses_list = Python_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Python Single

#  C Single
def C_single(request, slug):
    single = get_object_or_404(C_courses, slug=slug)
    first = C_courses.objects.first()
    last = C_courses.objects.last()
    courses_list = C_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
# End C Single

# JavaScript_single
def JavaScript_single(request, slug):
    single = get_object_or_404(JavaScript_courses, slug=slug)
    first = JavaScript_courses.objects.first()
    last = JavaScript_courses.objects.last()
    courses_list = JavaScript_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
# JavaScript_single

# Laravel_single
def Laravel_single(request, slug):
    single = get_object_or_404(Laravel_courses, slug=slug)
    first = Laravel_courses.objects.first()
    last = Laravel_courses.objects.last()
    courses_list = Laravel_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Laravel_single

#Django_single
def Django_single(request, slug):
    single = get_object_or_404(Django_courses, slug=slug)
    first = Django_courses.objects.first()
    last = Django_courses.objects.last()
    courses_list = Django_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Django_single

#Php_single
def Php_single(request, slug):
    single = get_object_or_404(Php_courses, slug=slug)
    first = Php_courses.objects.first()
    last = Php_courses.objects.last()
    courses_list = Php_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Php_single

#Php_single
def Html_single(request, slug):
    single = get_object_or_404(Html_courses, slug=slug)
    first = Html_courses.objects.first()
    last = Html_courses.objects.last()
    courses_list = Html_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Html_single

#Jq_single
def Jq_single(request, slug):
    single = get_object_or_404(Jq_courses, slug=slug)
    first = Jq_courses.objects.first()
    last = Jq_courses.objects.last()
    courses_list = Jq_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Jq_single


#Wp_single
def Wp_single(request, slug):
    single = get_object_or_404(Wp_courses, slug=slug)
    first = Wp_courses.objects.first()
    last = Wp_courses.objects.last()
    courses_list = Wp_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Wp_single


#Sql_single
def Sql_single(request, slug):
    single = get_object_or_404(Sql_courses, slug=slug)
    first = Sql_courses.objects.first()
    last = Sql_courses.objects.last()
    courses_list = Sql_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
#End Sql_single

# Bootstrap_single

def Bootstrap_single(request, slug):
    single = get_object_or_404(Bootstrap_courses, slug=slug)
    first = Bootstrap_courses.objects.first()
    last = Bootstrap_courses.objects.last()
    courses_list = Bootstrap_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
        'first': first,
        'last': last
    }

    return render(request, "course-details.html", context)
# Bootstrap_single

def about(request):
    return render(request, "about-us.html")



# Contact
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
        messages.success(request, 'আমাদের যোগাযোগ করার জন্য ধন্যবাদ')
        return redirect("/")
    return render(request, "contact.html")
#End Contact

# Java_single_quize
def Java_single_quize(request, slug):
    single = get_object_or_404(Java_quize_courses, slug=slug)
    courses_list = Django_courses.objects.all()
    courses_names = Courses_name.objects.all()
    context = {
        'single': single,
        'courses_list': courses_list,
        'courses_names': courses_names,
    }
    return render(request, "quize.html", context)
#End Java_single_quize
