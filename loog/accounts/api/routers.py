from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProfilesViewSet, UsersViewSet, InvitedUsersViewSet, WaitListAPI

api_router = DefaultRouter()
api_router.register('users', UsersViewSet, 'users')
api_router.register('profiles', ProfilesViewSet, 'profiles')
api_router.register('invited-users', InvitedUsersViewSet, 'invited_users')

urlpatterns = [
    path('v1/', include(api_router.urls)),
    path('v1/waitlist/', WaitListAPI.as_view(), name='wait_list_api')
]
