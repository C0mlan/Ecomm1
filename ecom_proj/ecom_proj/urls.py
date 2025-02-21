
from django.contrib import admin
from django.urls import path, include
from core.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from  drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',CreateUserView, name="register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('rest_framework.urls')),
    path('', include('core.urls')),
    path("api/schema", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name = "schema") )

]
