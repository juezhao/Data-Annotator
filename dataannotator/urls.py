from signup import urls
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('setup/', include('setup.urls')),
    path('doc/', include('doc.urls')),
    path('annotate/', include('annotate.urls')),
    path('login/', include('login.urls')),
    path('TestingPage/', include('TestingPage.urls')),
    path('AboutUs/', include('AboutUs.urls')),
    path('signup/',include('signup.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT
    }),
]
