from django.conf.urls import url, include
from core.views import UserList

urlpatterns = [
    url(r'^users/', UserList.as_view(), name='users'),
]
