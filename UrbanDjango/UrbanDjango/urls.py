from django.contrib import admin
from django.urls import path
from task5.views import sign_up_by_django, sign_up_by_html

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_up_by_html, name='sign_up_by_html'),
    path('django_sign_up/', sign_up_by_django, name='sign_up_by_django'),
]
