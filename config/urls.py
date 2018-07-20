from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

handler403 = TemplateView.as_view(template_name='errors/403.html')
handler404 = TemplateView.as_view(template_name='errors/404.html')
handler500 = TemplateView.as_view(template_name='errors/500.html')
