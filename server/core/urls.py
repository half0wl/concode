from django.conf.urls import url, include
from core.views import UserViewSet, ProjectList

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update'
})

urlpatterns = [
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<username>.+)/$', user_detail, name='user-detail'),
    url(r'^projects/$', ProjectList.as_view(), name='project-list'),
    # url(r'^projects/(?P<pk>[0-9]+)/$', project_detail, name='project-detail'),
]
