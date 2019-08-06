from django.contrib import admin
from django.urls import path
from basic_app import views
app_name='basic_app'
urlpatterns = [
#    path('admin/', admin.site.urls),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
    #path('basic_app/',include('basic_app.urls'))
]
