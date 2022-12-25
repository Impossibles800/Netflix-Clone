from django.urls import path
from core.views import Home, ProfileList, ProfileCreate, Watch

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/', Watch.as_view(), name='watch'),
]
