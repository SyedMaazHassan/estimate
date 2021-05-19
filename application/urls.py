from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('get_estimate', views.get_estimate, name="get_estimate"),
    path('check_site', views.check_site, name="check_site"),
    path('history', views.history, name="history"),
    path('result/<id>', views.result, name="result")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
