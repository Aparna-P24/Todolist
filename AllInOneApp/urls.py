from django.contrib import admin
from django.urls import path, include
from todolist import views as todolist_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls')),
    path('account/', include('users_app.urls')),
    path('contactus/', todolist_views.contactus, name='contactus'),
    path('activity/', todolist_views.activity, name='activity'),
    path('', todolist_views.index, name='index'),
]
