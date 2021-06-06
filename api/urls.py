from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from category.views import CategoryViewSet, AccountViewSet
from khazen.views import FileViewSet
from media.views import MediaViewSet
from user_account.views import UserViewSet, UserAccountViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='User')
router.register('user_account', UserAccountViewSet, basename='UserAccount')
router.register('category', CategoryViewSet, basename='Category')
router.register('account', AccountViewSet, basename='Account')
router.register('media', MediaViewSet, basename='Media')
router.register('file', FileViewSet, basename='File')

urlpatterns = router.urls
urlpatterns += (
    path('docs/', include_docs_urls(title='Secureraz API')),
    path('auth/', obtain_jwt_token),
    path('auth/', include('rest_framework.urls')),
)

urlpatterns += static('/khazen_local/', document_root=settings.MEDIA_ROOT)
