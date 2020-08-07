from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Staff, Post, Category, ContactUs, Course, Testimonial, PageInfo


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Staff)
admin.site.register(Category)
admin.site.register(ContactUs)
admin.site.register(Testimonial)
admin.site.register(PageInfo)


class CourseAdmin(SummernoteModelAdmin):
    list_display = ('course_name', 'price', 'course_date', 'skill_required')
    summernote_fields = ('course_info',)


admin.site.register(Course, CourseAdmin)





