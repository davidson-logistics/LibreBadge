from django.conf.urls import include
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "LibreBadge"
def applicationAdminURLS(modelName):
    return[
        path('create/', eval('views.' + modelName + 'Views' + ".get('CreateView').as_view()"), name= modelName + 'Create'),
        path('', eval('views.' + modelName + 'Views' + ".get('ListView').as_view()"), name= modelName + 'List'),
        path('update/<int:pk>/', eval('views.' + modelName + 'Views' + ".get('UpdateView').as_view()"), name= modelName + 'Update'),
        path('delete/<int:pk>/', eval('views.' + modelName + 'Views' + ".get('DeleteView').as_view()"), name= modelName + 'Delete'),
        ]
    
applicationadminpatterns = [
    path('', views.applicationadmin, name='applicationadmin'),
    path('alertmessages/', include(applicationAdminURLS('AlertMessage')), name='alertmessages'),
    path('badgetemplates/', include(applicationAdminURLS('BadgeTemplate')), name='badgetemplates'),
]
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login'),
    path("logout/", views.logout_request, name="logout"),
    re_path(r'^production/(?P<slug>[-\w]+)/$', views.production, name="production"),
    re_path(r'^production/(?P<slug>[-\w]+)/cardholders/$', views.productionCardholders, name="productionCardholders"),
    re_path(r'^production/(?P<slug>[-\w]+)/render/$', views.productionRender, name="productionRender"),
    re_path(r'^production/(?P<slug>[-\w]+)/update/$', views.productionUpdate, name="productionUpdate"),
    path('applicationadmin/', include(applicationadminpatterns), name='applicationadmin'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)