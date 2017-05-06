from django.conf.urls import url, include

urlpatterns = [
    url(r'^auth/', include('rest_social_auth.urls_jwt')),
]
