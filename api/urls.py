from django.urls import path, include
from rest_framework import routers

from api.views import CompanyViewSet, JobPostingViewSet

router = routers.DefaultRouter()
router.register(f'company', CompanyViewSet)
router.register(r'job_posting', JobPostingViewSet, basename='job_posting')

urlpatterns = [
    path('', include(router.urls)),
]
