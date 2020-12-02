from rest_framework import routers
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from user_account.views import UserViewSet, UserAccountViewSet
from category.views import CategoryViewSet, AccountViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet, basename='User')
router.register('user_account', UserAccountViewSet, basename='UserAccount')
router.register('category', CategoryViewSet, basename='Category')
router.register('account', AccountViewSet, basename='Account')

urlpatterns = router.urls
urlpatterns += (
    path('docs/', include_docs_urls(title='Secureraz API')),
    path('auth/', obtain_jwt_token),
    path('auth/', include('rest_framework.urls')),
)