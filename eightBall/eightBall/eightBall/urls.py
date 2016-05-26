"""eightBall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^questionApp/', include("questionApp.urls")),
	url(r'^login/$', views.login, {'template_name': 'registration/login.html'}),
	url(r'^logout/$', views.logout, {'next_page': '/questionApp/'}),
	url(r'^register/', CreateView.as_view(
		template_name='registration/register.html',
		form_class=UserCreationForm,
		success_url='/questionApp/'
	)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
