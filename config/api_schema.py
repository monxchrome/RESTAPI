from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v0.0.1',
      description="Test API DESC",
      contact=openapi.Contact(email="TEST@test.mail"),
      license=openapi.License(name="TEST License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
