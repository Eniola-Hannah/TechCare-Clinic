from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('doctors/', TemplateView.as_view(template_name='doctors.html'), name='doctors'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
]
