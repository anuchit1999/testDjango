from django.shortcuts import render, get_object_or_404, redirect
from .models import Staff, Post, Category, Course, Testimonial, ContactUs, PageInfo
from taggit.models import Tag
from .forms import ContactUsForm  # CommentForm,
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator


def home(request):
    obj1 = Post.objects.all()
    con_obj1 = obj1

    return render(request, 'blog/home.html', {'pst': con_obj1})


def about(request):
    obj2 = Staff.objects.all()
    obj3 = PageInfo.objects.all()
    con_obj2 = obj2
    con_boj3 = obj3

    return render(request, 'blog/about.html', {'stf': con_obj2, 'pi': con_boj3})


def contact(request):
    return render(request, 'blog/contact.html')


def blog_list(request):
    obj3 = Post.objects.all()
    paginator = Paginator(obj3, 9)  # Show 3 posts

    page_number = request.GET.get('page')
    context3 = paginator.get_page(page_number)
    return render(request, 'blog/blog-list.html', {'bl': context3})


def blog_detail(request, id):
    obj4 = Post.objects.get(id=id)
    con_obj4 = obj4

    return render(request, 'blog/blog-detail.html', {'bd': con_obj4})


def category_detail(request):
    obj5 = Category.objects.all()
    con_obj5 = obj5

    return render(request, 'blog/category.html', {'ct': con_obj5})


def contact_us(request):
    if request.method == 'POST':
        f = ContactUsForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted')
            return redirect('home')

        else:
            f = ContactUsForm()
        return render(request, 'blog/contact.html', {'form': f})


# Submit form
def regis(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ContactUsForm()
    return render(request, 'blog/contact.html', {'form': form,
                                                 'site_key': settings.RECAPTCHA_SITE_KEY})


"""
def edit(request, id):
    course_registration_edit = ContactUs.objects.get(id=id)
    return render(request, 'blog/contact.html', {'course_registration_edit': course_registration_edit})


# Update information form(For user)
def update(request, id):
    course_registration_update = ContactUs.objects.get(id=id)
    form = ContactUsForm(request.POST, instance=course_registration_update)

    if form.is_valid():
        form.sava()
        return redirect("/")
    return render(request, 'blog/contact.html', {'course_registration_update': course_registration_update})
"""


def course_list(request):
    obj6 = Course.objects.all()
    con_obj6 = obj6

    return render(request, 'blog/course.html', {'cl': con_obj6})


def course_detail(request, id):
    obj7 = Course.objects.get(id=id)
    con_obj7 = obj7

    return render(request, 'blog/course-detail.html', {'cd': con_obj7})


def client_say(request):
    obj8 = Testimonial.objects.all()
    cont_obj8 = obj8

    return render(request, 'blog/home.html', {'cs': cont_obj8})


def error_404(request, exception):
    """Return 404 page not found if a requested url isn't found"""

    return render(request, 'blog/error-404.html')


def show_vimeo(request):
    """Embed, and show a video (Vimeo)"""

    return render(request, 'blog/show-vimeo.html')





