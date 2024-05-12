"""
URL configuration for ProjektWSB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from personal.views import home_screen_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from zdarzenia.views import ZasobListView, usun_zasob, ZdarzenieListView, zdarzenie_list

from account.views import (
    login_view,
    logout_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name="home"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('lista_zasobow/', ZasobListView.as_view(), name="zasob_list"),
    path('lista_zdarzen/', ZdarzenieListView.as_view(), name="zdarzenie_list"),
    path('usun_zasob/<int:zasob_id>', usun_zasob, name="usun_zasob"),
    path('api_zdarzenie/', zdarzenie_list, name="lista_zdarzen_json"),

# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
        name='password_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
