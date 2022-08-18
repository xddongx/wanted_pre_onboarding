from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'job_posting', views.JobPostingViewSet, basename='job_posting')
router.register(r'user', views.UserViewSet)
router.register(r'application', views.ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
    path('some/url/', views.JobPostingSearchView.as_view()),
]
