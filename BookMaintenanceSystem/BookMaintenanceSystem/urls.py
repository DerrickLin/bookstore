"""
URL configuration for BookMaintenanceSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import settings
from django.conf.urls.static import static
import accounts.views as aviews
import books.views as bviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", aviews.sign_in, name='Login'),
    path("login/", aviews.sign_in, name='Login'),
    path("book/", bviews.Book, name='Book'),
    path("logout/", aviews.log_out, name='Logout'),
    path("register/", aviews.register, name='Register'),
    path('book/<int:book_id>/', bviews.book_detail, name='book_detail'),
    path("book/create/", bviews.book_create, name='Create'),
    path("book_lend_records/<int:book_id>", bviews.book_lend_records, name='BookLendRecords'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
