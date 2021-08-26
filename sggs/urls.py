from django.contrib import admin
from django.urls import path,include
from school import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('IT.urls')),
    path('CS/', include('CS.urls')),
    path('CIVIL/', include('CIVIL.urls')),
    path('ETC/', include('ETC.urls')),
    path('func/',views.myview, name='func'),
    path('cl/',views.Myview.as_view(), name='cl'),
]