from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import get_language_from_request
from django.shortcuts import redirect


def redirect_to_default_language(request):
    """Force redirect to Georgian ('ka') unless another language is explicitly set."""
    language = get_language_from_request(request) or 'ka'
    # language = 'en'

    # Override browser preference and force 'ka' if no language cookie exists
    if 'django_language' not in request.COOKIES:
        language = 'ka'  # Force default language

    response = redirect(f'/{language}/')
    response.set_cookie('django_language', language)  # Store language preference
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_default_language),  # Redirect `/` to preferred or default language
]

urlpatterns += i18n_patterns(
    path('', include('homepage.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
