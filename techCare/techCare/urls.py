from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from techCare.userApp.views import SignUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name = 'index.html'), name='home'),
    path('doctors/', TemplateView.as_view(template_name='doctors.html'), name='doctors'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
]
