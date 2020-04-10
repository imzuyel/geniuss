from django.db import models
from tinymce import *
from django.utils.timezone import datetime
from django.template.defaultfilters import slugify
# Create your models here.


# Courses_name
class Courses_name(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='', blank=True)
    pic = models.ImageField(upload_to='images/')
    details = models.TextField()

    def __str__(self):
        return self.name

    def summary(self):
        return self.details[:80]+"..."
#End Courses_name

# Java_courses
class Java_courses(models.Model):
    course_name = models.CharField(max_length=100, default='java')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Java_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
#End Java_courses

# Java_quize_courses
class Java_quize_courses(models.Model):
    course_name = models.CharField(max_length=100, default='python')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    question1 = models.CharField(max_length=100, default='', blank=True)
    op1 = models.CharField(max_length=100, default='', blank=True)
    op11 = models.CharField(max_length=100, default='', blank=True)
    ans1 = models.CharField(max_length=100, default='', blank=True)
    ans11 = models.CharField(max_length=100, default='', blank=True)

    question2 = models.CharField(max_length=100, default='', blank=True)
    op2 = models.CharField(max_length=100, default='', blank=True)
    op22 = models.CharField(max_length=100, default='', blank=True)
    op222 = models.CharField(max_length=100, default='', blank=True)
    op2222 = models.CharField(max_length=100, default='', blank=True)
    ans2 = models.CharField(max_length=100, default='', blank=True)
    ans22 = models.CharField(max_length=100, default='', blank=True)
    ans222 = models.CharField(max_length=100, default='', blank=True)
    ans2222 = models.CharField(max_length=100, default='', blank=True)

    question3 = models.CharField(max_length=100, default='', blank=True)
    op3 = models.CharField(max_length=100, default='', blank=True)
    op33 = models.CharField(max_length=100, default='', blank=True)
    op333 = models.CharField(max_length=100, default='', blank=True)
    op3333 = models.CharField(max_length=100, default='', blank=True)
    ans3 = models.CharField(max_length=100, default='', blank=True)
    ans33 = models.CharField(max_length=100, default='', blank=True)
    ans333 = models.CharField(max_length=100, default='', blank=True)
    ans3333 = models.CharField(max_length=100, default='', blank=True)

    question4 = models.CharField(max_length=100, default='', blank=True)
    op4 = models.CharField(max_length=100, default='', blank=True)
    op44 = models.CharField(max_length=100, default='', blank=True)
    ans4 = models.CharField(max_length=100, default='', blank=True)
    ans44 = models.CharField(max_length=100, default='', blank=True)

    question5 = models.CharField(max_length=100, default='', blank=True)
    op5 = models.CharField(max_length=100, default='', blank=True)
    op55 = models.CharField(max_length=100, default='', blank=True)
    op555 = models.CharField(max_length=100, default='', blank=True)
    op5555 = models.CharField(max_length=100, default='', blank=True)
    ans5 = models.CharField(max_length=100, default='', blank=True)
    ans55 = models.CharField(max_length=100, default='', blank=True)
    ans555 = models.CharField(max_length=100, default='', blank=True)
    ans5555 = models.CharField(max_length=100, default='', blank=True)
# Java_quize_courses

#Python_courses
class Python_courses(models.Model):
    course_name = models.CharField(max_length=100, default='python')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Python_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
#End Python_courses

#C_courses
class C_courses(models.Model):
    course_name = models.CharField(max_length=100, default='c')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(C_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
#End C_courses

# JavaScript_courses
class JavaScript_courses(models.Model):
    course_name = models.CharField(max_length=100, default='JavaScript')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(JavaScript_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# End JavaScript_courses

# Laravel_courses
class Laravel_courses(models.Model):
    course_name = models.CharField(max_length=100, default='laravel')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Laravel_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# End Laravel_courses

# Django_courses
class Django_courses(models.Model):
    course_name = models.CharField(max_length=100, default='django')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Django_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
#End Django_courses

# Php_courses
class Php_courses(models.Model):
    course_name = models.CharField(max_length=100, default='php')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Php_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# Php_courses


# Html_courses
class Html_courses(models.Model):
    course_name = models.CharField(max_length=100, default='html')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Html_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# Html_courses

# Jq_courses
class Jq_courses(models.Model):
    course_name = models.CharField(max_length=100, default='jquery')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jq_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# Jq_courses


# Wp_courses
class Wp_courses(models.Model):
    course_name = models.CharField(max_length=100, default='wordpress')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Wp_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# End Wp_courses



# MySql_courses
class Sql_courses(models.Model):
    course_name = models.CharField(max_length=100, default='mysql')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Sql_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# End MySql_courses


# Bootstrap_courses
class Bootstrap_courses(models.Model):
    course_name = models.CharField(max_length=100, default='bootstrap')
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    published = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Bootstrap_courses, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
#End Bootstrap_courses


# Contact
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
#EndContact
