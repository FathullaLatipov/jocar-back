from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from cars.views import HomeView, ModelsView, add_to_wishlist

urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('models/', include('cars.urls', namespace='products')),
    path('', HomeView.as_view())
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
