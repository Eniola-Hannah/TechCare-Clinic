from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from techCare.userApp.views import SignUpView
from techCare.servicesApp.views import indexService
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', indexService, name='home'),
    path('doctors/', TemplateView.as_view(template_name='doctors.html'), name='doctors'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
    re_path(r'^userApp/', include('techCare.userApp.urls')),
    re_path(r'^servicesApp/', include('techCare.servicesApp.urls')),
    re_path(r'^paymentApp/', include('techCare.paymentApp.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)