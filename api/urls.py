from django.urls import path, include
from rest_framework import routers

from api.views import CompanyViewSet, JobPostingSearchView, JobPostingViewSet

router = routers.DefaultRouter()
router.register(f'company', CompanyViewSet)
router.register(r'job_posting', JobPostingViewSet, basename='job_posting')
# router.register(r'some/url', JobPostingSearchView, basename='search')

urlpatterns = [
    path('', include(router.urls)),
    path('some/url/', JobPostingSearchView.as_view()),
]
