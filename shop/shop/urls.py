from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('apps.carts.urls')),
    path('order/', include('apps.orders.urls')),
    path('payment/', include('apps.payments.urls')),
    path('', include('apps.products.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
