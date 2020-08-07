from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog_list, name='blog_list'),
    path('blogdetail/<int:id>', views.blog_detail, name='blog_detail'),
    # path('postdetail', views.post_detail, name='post_detail')
    path('slug', views.category_detail, name='category_detail'),
    path('contactus', views.contact_us, name='contact_us'),  # Form submission
    path('course', views.course_list, name='course_list'),
    path('coursedetail/<int:id>', views.course_detail, name='course_detail'),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('update/<int:id>', views.update, name='update'),
    path('contact-us', views.regis, name='regis'),
    path('show-vimeo', views.show_vimeo, name='show_vimeo')
]