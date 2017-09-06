from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import include, url

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from django.contrib import admin

from rucken_todo.actions import AccountProfileUpdateAction
from rucken_todo.viewsets import router

admin.autodiscover()

urlpatterns = [
    url(r'^api/account/login', obtain_jwt_token),
    url(r'^api/account/info', verify_jwt_token),
    url(r'^api/account/update', AccountProfileUpdateAction.as_view()),
    url(r'^api/', include(router.urls)),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static('/upload/details/images/', document_root='upload/details/images/')
    urlpatterns += static('/css/', document_root='app/staticfiles/css/')
    urlpatterns += static('/img/', document_root='app/staticfiles/img/')
    urlpatterns += static('/js/', document_root='app/staticfiles/js/')
