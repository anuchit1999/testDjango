from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Information about page(staff) here
class Staff(models.Model):
    staff_name = models.CharField(max_length=80)
    staff_age = models.IntegerField()
    staff_quote = models.CharField(max_length=200)
    staff_email = models.CharField(max_length=50)
    staff_phone = models.CharField(max_length=10)
    staff_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.staff_name


class PageInfo(models.Model):
    page_description = models.TextField()
    main_header_cover = models.ImageField(upload_to='main_cover/')
    sub_header_cover = models.ImageField(upload_to='sub_cover/')
    box_name1 = models.CharField(max_length=20)
    box_name2 = models.CharField(max_length=20)
    box_name_small = models.CharField(max_length=20)

    def __str__(self):
        return self.box_name1


class Category(models.Model):
    cate_name = models.CharField(max_length=40)
    cate_url = models.URLField(max_length=200)

    def __str__(self):
        return self.cate_name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Import user to create ForeignKey
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date_pub = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    cover_pic = models.ImageField(upload_to='blogcover/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = TaggableManager(blank=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=80, help_text="Name of the sender")
    subject = models.CharField(max_length=100)
    message = models.TextField()
    cont_email = models.EmailField()

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.cont_email


class Course(models.Model):
    course_name = models.CharField(max_length=80)
    course_date = models.DateField()
    end_date = models.DateField()
    course_info = models.TextField()
    skill_required = models.CharField(max_length=150)
    price = models.IntegerField()
    course_photo = models.ImageField(upload_to='course/')
    course_duration = models.CharField(max_length=40)

    def __str__(self):
        return self.course_name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=60)
    quote = models.CharField(max_length=200)
    client_pic = models.ImageField(upload_to='client/')
    pic_avata = models.ImageField(upload_to='avatar/')

    def __str__(self):
        return self.client_name
















