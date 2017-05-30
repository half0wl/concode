from django.conf.urls import url, include
from core.views import UserViewSet, ProjectViewSet

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update'
})

project_list = ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create',
    # 'delete': 'delete'
})

project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
    'patch': 'update'
})

urlpatterns = [
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<username>.+)/$', user_detail, name='user-detail'),
    url(r'^projects/$', project_list, name='project-list'),
    url(r'^projects/(?P<pk>[0-9]+)/$', project_detail, name='project-detail'),
]
