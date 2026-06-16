
from django.contrib import admin
from django.urls import path
from core import views as core_views
from contact import views as core_contact
from portfolio import views as portfolio_views

from django.conf import settings

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about-me/', core_views.about, name='about'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('contact/', core_contact.contact, name='contact'),
    path('admin/', admin.site.urls),
]
<<<<<<< HEAD
handler404 = "core.views.error_404"
=======
>>>>>>> 589c48d0be3bb96b111f0586eddfe43ef9c5388a

# para que podamos ver los achivos de imagen de subimos poor le sadministador
if settings.DEBUG:
    from django.conf.urls.static import static
<<<<<<< HEAD
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 589c48d0be3bb96b111f0586eddfe43ef9c5388a
