from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.conf.urls.static import static

from throwbox_project import settings


def get_host(request):
    host = request.META.get("HTTP_ORIGIN") or request.get_host()
    # if ":" not in host:
    #     port = request.META.get("SERVER_PORT")
    #     host += f":{port}"
    return host


class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super(CustomSchemaGenerator, self).get_schema(request, public)
        schema.host = self.get_host(request)
        schema.schemes = ["http", "https"]
        return schema

    # TODO: найти более изящное решение
    @staticmethod
    def get_host(request):
        return get_host(request)


schema_view = get_schema_view(
    openapi.Info(title="Telemed", default_version="v0.1"),
    public=True,
    generator_class=CustomSchemaGenerator,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/', include('throwbox_app.urls')),
    re_path(
        r"swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
